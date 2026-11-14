
# PYTHON

import psycopg

from suppliers.accountsup import get_account_supplier_record
from suppliers.addresssup import get_address_supplier_record
from suppliers.searchsup import get_search_supplier_record

from dotenv import load_dotenv
load_dotenv()

def supplier_database():
    # CONNECT TO THE DATABASE
    conn = psycopg.connect(host="localhost", dbname="supplier_crud", user="postgres")

    # CREATE A DATABASE CURSOR
    cursor = conn.cursor()

    return conn, cursor


def get_account_details():
    conn, cursor = supplier_database()
    rows = get_account_supplier_record(cursor)
    conn.close()
    return rows


def get_address_details():
    conn, cursor = supplier_database()
    rows = get_address_supplier_record(cursor)
    conn.close()
    return rows

def get_search_supplier(supplier_name):
    conn, cursor = supplier_database()
    rows, message = get_search_supplier_record(cursor, supplier_name)
    conn.close()
    return rows, message

