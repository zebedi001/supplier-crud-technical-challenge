
# SEARCH POSTGRESQL USING FULL OR PARTIAL SUPPLIER NAME
# CASE-INSENSITIVE SEARCH

def get_search_supplier_record(cursor, supplier_name):

    # CHECK SUPPLIER NAME HAS BEEN ENTERED
    if supplier_name is None or supplier_name.strip() == "":
        return [], "Supplier Name cannot be blank."

    # FIND ALL MATCHING SUPPLIERS
    cursor.execute(
        "SELECT * FROM suppliers WHERE name ILIKE %s ORDER BY name ASC",
        (f"%{supplier_name.strip()}%",)
    )

    rows = cursor.fetchall()

    # CHECK IF ANY SUPPLIERS WERE FOUND
    if not rows:
        return [], "No matching suppliers found."

    return rows, None
