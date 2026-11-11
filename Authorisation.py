
import os
import re
from functools import wraps

import psycopg
from psycopg.rows import dict_row
from psycopg.errors import UniqueViolation

from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError, VerificationError, InvalidHashError

from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from flask_login import UserMixin, current_user, login_user, logout_user, login_required

# Authentication blueprint and password hasher
auth = Blueprint("auth", __name__)
hasher = PasswordHasher()

# Security levels
ROLES = {
    "Viewer": 0,
    "Support": 1,
    "Admin": 2,
    "Supervisor": 3,
    "Management": 4,
    "Leader": 5,
    }

# Connect to PostgreSQL
def get_connection():
    return psycopg.connect(
        host="localhost",
        dbname="supplier_crud",
        user="postgres",
        row_factory=dict_row
    )


# Find a user by username or ID
def get_user(identifier, by_id=False):
    column = "id" if by_id else "username"
    with get_connection() as conn:
        return conn.execute(
            f"SELECT id, username, email, password_hash, security_level, is_active "
            f"FROM users WHERE {column} = %s",
            (identifier,),
        ).fetchone()


# Flask-Login user
class User(UserMixin):
    def __init__(self, record):
        self.id = str(record["id"])
        self.username = record["username"]
        self.email = record["email"]
        self.security_level = int(record["security_level"])
        self._is_active = bool(record["is_active"])

    @property
    def is_active(self):
        return self._is_active

# Restore users from sessions
def init_auth(login_manager):
    @login_manager.user_loader
    def load_user(user_id):
        try:
            record = get_user(int(user_id), by_id=True)
        except (ValueError, TypeError):
            return None
        return User(record) if record and record["is_active"] else None


# Register new users as Viewers
@auth.post("/register")
def register():
    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        data = request.form

    username = data.get("username", "")
    email = data.get("email", "")
    password = data.get("password", "")

    if not all(isinstance(v, str) for v in (username, email, password)):
        return jsonify(error="Invalid registration details"), 400

    username = username.strip()
    email = email.strip().lower()

    if not re.fullmatch(r"[A-Za-z0-9_.-]{3,100}", username):
        return jsonify(error="Invalid username"), 400
    if len(email) > 254 or not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email):
        return jsonify(error="Invalid email"), 400
    if not 12 <= len(password) <= 128:
        return jsonify(error="Password must be 12-128 characters"), 400

    try:
        with get_connection() as conn:
            conn.execute(
                "INSERT INTO users (username, email, password_hash, security_level) "
                "VALUES (%s, %s, %s, 0)",
                (username, email, hasher.hash(password)),
            )
    except UniqueViolation:
        return jsonify(error="Username or email already exists"), 409

    return jsonify(message="Registration successful", security_level=0), 201


# Log in

@auth.get("/login")
def login_page():
    return render_template("login.html")

@auth.post("/login")
def login():
    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        data = request.form

    username = data.get("username", "")
    password = data.get("password", "")

    if not isinstance(username, str) or not isinstance(password, str):
        return jsonify(error="Invalid username or password"), 401
    if not username.strip() or len(password) > 128:
        return jsonify(error="Invalid username or password"), 401

    record = get_user(username.strip())
    if not record:
        return jsonify(error="Invalid username or password"), 401

    try:
        hasher.verify(record["password_hash"], password)
    except (VerifyMismatchError, VerificationError, InvalidHashError):
        return jsonify(error="Invalid username or password"), 401

    if not record["is_active"]:
        return jsonify(error="Account is disabled"), 403

    # Upgrade outdated password hashes
    if hasher.check_needs_rehash(record["password_hash"]):
        with get_connection() as conn:
            conn.execute(
                "UPDATE users SET password_hash = %s WHERE id = %s",
                (hasher.hash(password), record["id"]),
            )

    # Start a fresh session
    logout_user()
    login_user(User(record), fresh=True)

    if not request.is_json:
        return redirect(url_for("home"))

    return jsonify(
        message="Login successful",
        username=record["username"],
        security_level=record["security_level"],
    ), 200


# Log out
@auth.post("/logout")
@login_required

def logout():
    logout_user()
    
    return jsonify(message="Logout successful"), 200


# Get current user
@auth.get("/me")
@login_required
def me():
    return jsonify(
        id=current_user.id,
        username=current_user.username,
        email=current_user.email,
        security_level=current_user.security_level,
    ), 200


# Protect routes by security level
def require_level(level):
    if type(level) is not int or level not in range(6):
        raise ValueError("Invalid security level")

    def decorator(view):
        @wraps(view)
        @login_required
        def wrapped(*args, **kwargs):
            if current_user.security_level < level:
                return jsonify(error="Insufficient permissions"), 403
            return view(*args, **kwargs)
        return wrapped
    return decorator


# Only Leaders can change security levels
@auth.post("/admin/users/<int:user_id>/security-level")
@require_level(ROLES["Leader"])
def set_security_level(user_id):
    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        return jsonify(error="JSON body required"), 400

    level = data.get("security_level")
    if type(level) is not int or level not in range(6):
        return jsonify(error="Invalid security level"), 400

    with get_connection() as conn:
        result = conn.execute(
            "UPDATE users SET security_level = %s WHERE id = %s RETURNING id",
            (level, user_id),
        ).fetchone()

    if not result:
        return jsonify(error="User not found"), 404

    return jsonify(message="Security level updated"), 200
