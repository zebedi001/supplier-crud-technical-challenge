
# DELETE SUPPLIER BACKEND

def get_delete_supplier_record(cursor, supplier_id):

    # CHECK SUPPLIER ID IS NOT BLANK
    if supplier_id == "":
        return None, "Supplier ID cannot be blank."


    # FIND THE SUPPLIER
    cursor.execute(
        "SELECT * FROM suppliers WHERE id = %s",
        (supplier_id,)
    )

    row = cursor.fetchone()

    # CHECK WHETHER THE ID EXISTS
    if row is None:
        return None, "Supplier ID not found. Please try again."
    
    return row, None



def delete_supplier_record(cursor, conn, supplier_id):

    cursor.execute(
        "DELETE FROM suppliers WHERE id = %s",
        (supplier_id,)
    )

    conn.commit()

    return("Supplier deleted.")
