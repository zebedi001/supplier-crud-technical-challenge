
# PYTHON

# import sqlite3
from supplierdb import supplier_database

from suppliers.addsup import add_supplier_record
from suppliers.accountsup import account_supplier_record, get_account_supplier_record
from suppliers.addresssup import address_supplier_record, get_address_supplier_record
from suppliers.amendsup import amend_supplier_record
from suppliers.deletesup import delete_supplier_record
from suppliers.searchsup import get_search_supplier_record

def add_supplier_details(
    name, account, terms,
    street, town, city, postcode,
    contactname, contactnum
):
    conn, cursor = supplier_database()

    result = add_supplier_record(
        cursor, conn,
        name, account, terms,
        street, town, city, postcode,
        contactname, contactnum
    )

    conn.close()

    return result


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

def get_search_supplier():
    conn, cursor = supplier_database()
    rows = get_search_supplier_record(cursor)
    conn.close()
    return rows


def supplier_menu():

    conn, cursor = supplier_database()

    # DISPLAY PROGRAM
    pur_ledger = "PURCHASE LEDGER"
    width = 71
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print(pur_ledger.center(width, "-"))
    print("\n\n\n\n\n")

    # SUPPLIER MAIN MENU
    while True:

        menu_supplier = "SUPPLIER MENU"
        menuline_supplier = "============="
        add_supplier = "1. Create Supplier"
        account_supplier = "2. Account Details"
        address_supplier = "3. Address Details"
        amend_supplier = "4. Amend Supplier"
        delete_supplier = "5. Delete Supplier"
        exit_supplier = "9. Exit"

        print(f"{menu_supplier:^71}")
        print(f"{menuline_supplier:^71}")
        print(f"{add_supplier:<25}".center(71))
        print(f"{account_supplier:<25}".center(71))
        print(f"{address_supplier:<25}".center(71))
        print(f"{amend_supplier:<25}".center(71))
        print(f"{delete_supplier:<25}".center(71))
        print(f"{exit_supplier:<25}".center(71))

        choice = input("\n\nEnter your choice: ").strip()

        if choice == "":
            print("Please enter a menu option.")
            continue

        if choice == "1":
            # ADD SUPPLIER
            add_supplier_record(cursor, conn)

        elif choice == "2":
            # LIST ACCOUNT DETAILS
            account_supplier_record(cursor)

        elif choice == "3":
            # LIST ADDRESS DETAILS
            address_supplier_record(cursor)

        elif choice == "4":
            # AMEND SUPPLIER
            amend_supplier_record(cursor, conn)

        elif choice == "5":
            # DELETE SUPPLIER
            delete_supplier_record(cursor, conn)

        elif choice == "9":
            break

        else:

            print("Invalid choice. Please try again")

    # CLOSE THE DATABASE CONNECTION
    conn.close()


if __name__ == "__main__":
    supplier_menu()
