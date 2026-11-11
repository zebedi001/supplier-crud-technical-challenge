
# ACCOUNT DETAILS BACKEND

def get_account_supplier_record(cursor):
    cursor.execute("SELECT * FROM suppliers ORDER BY id ASC")
    rows = cursor.fetchall()
    return rows


def account_supplier_record(cursor):

    # LIST SUPPLIERS

    rows = get_account_supplier_record(cursor)

   # COLUMN HEADINGS
    print(
        f"\n{'ID':<5}"
        f"{'Supplier Name':<35}"
        f"{'Account':<16}"
        f"{'Terms':<8}"
        f"{'Contact':<18}"
        f"{'Number':<12}"
    )

    # SUPPLIER RECORDS
    for row in rows:
        print(
            f"{row[0]:<5}"
            f"{row[1]:<35}"
            f"{row[2]:<16}"
            f"{row[3]:<8}"
            f"{row[8] or '':<18}"
            f"{row[9] or '':<12}"
        )
        