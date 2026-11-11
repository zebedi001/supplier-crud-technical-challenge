
# ============================================================
# IMPORTS
# ============================================================

import os
from flask import Flask, render_template, request

# from flask_login import LoginManager, login_required
# from Authorisation import auth, init_auth

import supplierdb

from suppliers.addsup import add_supplier_record
from suppliers.amendsup import get_amend_supplier_record, amend_supplier_record
from suppliers.deletesup import get_delete_supplier_record, delete_supplier_record


# ============================================================
# SESSION SECURITY
# ============================================================

app = Flask(__name__)
# app.config["SECRET_KEY"] = os.environ.get("PURCHASE_WEB_SECRET_KEY") or "temporary-local-development-key"

# ============================================================
# FLASK LOGIN / AUTHENTIFICATION
# ============================================================

# login_manager = LoginManager()
# login_manager.init_app(app)
# init_auth(login_manager)

# app.register_blueprint(auth, url_prefix="/auth")
# login_manager.login_view = "auth.login_page"

# ============================================================
# MAIN PURCHASE LEDGER
# ============================================================

@app.route("/")
# @login_required
def home():
    return render_template("index_main.html")

# ============================================================
# 1. SUPPLIERS
# ============================================================

# ADD SUPPLIER

@app.route("/index_supplier")
def supplierhome():
    return render_template("index_supplier.html")

@app.route("/add_supplier", methods=["GET", "POST"])
def add_supplier():

    if request.method == "GET":
        return render_template("add_supplier.html")

    name = request.form["name"]
    account = request.form["account"]
    terms = request.form["terms"]
    street = request.form["street"]
    town = request.form["town"]
    city = request.form["city"]
    postcode = request.form["postcode"]
    contactname = request.form["contactname"]
    contactnum = request.form["contactnum"]
    
    conn, cursor = supplierdb.supplier_database()

    result = add_supplier_record(
        cursor, conn,
        name, account, terms,
        street, town, city, postcode,
        contactname, contactnum
    )

    conn.close()

    return render_template("add_supplier.html", message=result)


# AMEND SUPPLIER

@app.route("/amend_supplier", methods=["GET", "POST"])
def amend_supplier():

    # POST - AMEND SUPPLIER RECORD - CHECK IF AMENDED SUPPLIER DETAILS HAVE BEEN SENT FROM THE HTML FORM
    if request.method == "POST":

        # GET AMENDED SUPPLIER DETAILS FROM HTML FORM
        supplier_id = request.form["supplier_id"]
        name = request.form["name"]
        account = request.form["account"]
        terms = request.form["terms"]
        street = request.form["street"]
        town = request.form["town"]
        city = request.form["city"]
        postcode = request.form["postcode"]
        contactname = request.form["contactname"]
        contactnum = request.form["contactnum"]

        # CONNECT TO DATABASE
        conn, cursor = supplierdb.supplier_database()

        # SEND AMENDED SUPPLIER DETAILS TO AMENDSUP.PY
        # AMENDSUP.PY WILL VALIDATE THE DETAILS AND UPDATE THE DATABASE
        result = amend_supplier_record(
            cursor, conn, supplier_id, name, account, terms,
            street, town, city, postcode, contactname, contactnum
        )

        # GET THE SUPPLIER RECORD AGAIN FROM THE DATABASE SO THE HTML DISPLAYS THE UPDATED DETAILS
        row, message = get_amend_supplier_record(
            cursor,
            supplier_id
        )

        # CLOSE DATABASE CONNECTION
        conn.close()

        # SEND UPDATED SUPPLIER RECORD AND RESULT MESSAGE TO HTML
        return render_template(
            "amend_supplier.html",
            row=row,
            message=result
        )

    # GET SUPPLIER ID FROM THE HTML FORM / URL
    supplier_id = request.args.get("supplier_id")

    # FIRST VISIT TO PAGE
    # NO SUPPLIER ID HAS BEEN ENTERED YET
    if supplier_id is None:
        return render_template("amend_supplier.html")

    # CONNECT TO DATABASE
    conn, cursor = supplierdb.supplier_database()

    # SEND SUPPLIER ID TO AMENDSUP.PY
    # AND GET THE EXISTING SUPPLIER RECORD
    row, message = get_amend_supplier_record(
        cursor,
        supplier_id
    )

    # CLOSE DATABASE CONNECTION
    conn.close()

    # SEND SUPPLIER RECORD TO HTML
    # THE EXISTING VALUES WILL APPEAR IN THE INPUT FIELDS
    return render_template(
        "amend_supplier.html",
        row=row,
        message=message
    )


# DELETE SUPPLIER

@app.route("/delete_supplier", methods=["GET", "POST"])
def delete_supplier():

    # CHECK IF DELETED SUPPLIER DETAILS HAVE BEEN SENT
    # FROM THE HTML FORM
    if request.method == "POST":

        # GET DELETED SUPPLIER DETAILS FROM HTML FORM
        supplier_id = request.form["supplier_id"]
        name = request.form["name"]
        account = request.form["account"]
        terms = request.form["terms"]
        street = request.form["street"]
        town = request.form["town"]
        city = request.form["city"]
        postcode = request.form["postcode"]
        contactname = request.form["contactname"]
        contactnum = request.form["contactnum"]

        # CONNECT TO DATABASE
        conn, cursor = supplierdb.supplier_database()

        # SEND DELETED SUPPLIER DETAILS TO DELETESUP.PY
        # DELETESUP.PY WILL VALIDATE THE DETAILS AND UPDATE THE DATABASE
        result = delete_supplier_record(cursor, conn, supplier_id)

        # GET THE SUPPLIER RECORD AGAIN FROM THE DATABASE
        # SO THE HTML DISPLAYS THE DELETED DETAILS
        row, message = get_delete_supplier_record(
            cursor, supplier_id)
        
        # CLOSE DATABASE CONNECTION
        conn.close()

        # SEND DELETED SUPPLIER RECORD AND RESULT MESSAGE TO HTML
        return render_template(
            "delete_supplier.html",
            row=row,
            message=result
        )

    # GET - FIND DELETED SUPPLIER RECORD    
    # GET SUPPLIER ID FROM THE HTML FORM / URL
    supplier_id = request.args.get("supplier_id")

    # FIRST VISIT TO PAGE
    # NO SUPPLIER ID HAS BEEN ENTERED YET
    if supplier_id is None:
        return render_template("delete_supplier.html")

    # CONNECT TO DATABASE
    conn, cursor = supplierdb.supplier_database()

    # SEND SUPPLIER ID TO DELETESUP.PY
    # AND GET THE EXISTING SUPPLIER RECORD
    row, message = get_delete_supplier_record(cursor, supplier_id)

    # CLOSE DATABASE CONNECTION
    conn.close()

    # SEND SUPPLIER RECORD TO HTML
    # THE EXISTING VALUES WILL APPEAR IN THE INPUT FIELDS
    return render_template(
        "delete_supplier.html",
        row=row,
        message=message
    )


# SUPPLIER ACCOUNT DETAILS
@app.route("/account_details")
def account_details():
    rows = supplierdb.get_account_details()
    return render_template("account_details.html", rows=rows)


# SUPPLIER ADDRESS DETAILS
@app.route("/address_details")
def address_details():
    rows = supplierdb.get_address_details()
    return render_template("address_details.html", rows=rows)


# ============================================================
# 2. PURCHASES
# ============================================================

@app.route("/index_purchases")
def purchaseshome():
    return render_template("index_purchases.html")

@app.route("/add_po")
def add_po():
    return render_template("add_po.html")

@app.route("/view_po")
def view_po():
    return render_template("view_po.html")

@app.route("/delete_po")
def delete_po():
    return render_template("delete_po.html")

@app.route("/add_inv")
def add_inv():
    return render_template("add_inv.html")

@app.route("/view_inv")
def view_inv():
    return render_template("view_inv.html")

@app.route("/delete_inv")
def delete_inv():
    return render_template("delete_inv.html")

@app.route("/add_cn")
def add_cn():
    return render_template("add_cn.html")

@app.route("/view_cn")
def view_cn():
    return render_template("view_cn.html")

@app.route("/delete_cn")
def delete_cn():
    return render_template("delete_cn.html")

# ============================================================
# 2. PAYMENTS
# ============================================================

@app.route("/index_payments")
def paymentshome():
    return render_template("index_payments.html")

@app.route("/add_pay")
def add_pay():
    return render_template("add_pay.html")

@app.route("/view_pay")
def view_pay():
    return render_template("view_pay.html")

@app.route("/delete_pay")
def delete_pay():
    return render_template("delete_pay.html")


# ============================================================
# 3. LEDGER ACTIVITY
# ============================================================

@app.route("/index_ledger")
def ledgerhome():
    return render_template("index_ledger.html")

@app.route("/view_acc_all")
def view_acc_all():
    return render_template("view_acc_all.html")

@app.route("/view_transac")
def view_transac():
    return render_template("view_transac.html")

@app.route("/alloc_match")
def alloc_match():
    return render_template("alloc_match.html")

@app.route("/view_out_items")
def view_out_items():
    return render_template("view_out_items.html")

@app.route("/manual_adj")
def manual_adj():
    return render_template("manual_adj.html")


# ============================================================
# 5. REPORTS
# ============================================================

@app.route("/index_reports")
def reportshome():
    return render_template("index_reports.html")

@app.route("/aged_creditors")
def aged_creditors():
    return render_template("aged_creditors.html")

@app.route("/supp_balances")
def supp_balances():
    return render_template("supp_balances.html")

@app.route("/out_invoices")
def out_invoices():
    return render_template("out_invoices.html")

@app.route("/purch_analysis")
def purch_analysis():
    return render_template("purch_analysis.html")

@app.route("/pay_history")
def pay_history():
    return render_template("pay_history.html")


# ============================================================
# 6. SETTINGS
# ============================================================

@app.route("/index_settings")
def settingshome():
    return render_template("index_settings.html")


# ============================================================
# 7. MARA AI ASSISTANT
# ============================================================

@app.route("/index_AI")
def aihome():
    return render_template("index_AI.html")


# ============================================================
# START PURCHASE LEDGER
# ============================================================

if __name__ == "__main__":
    app.run(debug=True, port=5000, use_reloader=False)