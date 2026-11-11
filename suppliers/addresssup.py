
# ADDRESS SUPPLIER BACKEND

def get_address_supplier_record(cursor):
    cursor.execute("SELECT * FROM suppliers ORDER BY id ASC")
    rows = cursor.fetchall()
    return rows


def address_supplier_record(cursor):

    # LIST SUPPLIERS FULL ADDRESS DETAILS

    rows = get_address_supplier_record(cursor)

   # COLUMN HEADINGS
    print(
        f"\n{'ID':<5}"
        f"{'Supplier Name':<30}"
        f"{'Street':<25}"
        f"{'Town':<16}"
        f"{'City':<16}"
        f"{'Postcode':<9}"
    )

    # SUPPLIER RECORDS
    for row in rows:
        print(
            f"{row[0]:<5}"
            f"{row[1]:<30}"
            f"{row[4]:<25}"
            f"{row[5]:<16}"
            f"{row[6]:<16}"
            f"{row[7]:<9}"
        )
