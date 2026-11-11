
# AMEND SUPPLIER BACKEND

# GET SUPPLIER RECORD TO AMEND
def get_amend_supplier_record(cursor, supplier_id):

    # CHECK SUPPLIER ID HAS BEEN ENTERED
    if supplier_id is None or supplier_id.strip() == "":
        return None, "Supplier ID cannot be blank."

    # CHECK SUPPLIER ID IS A NUMBER
    if not supplier_id.isdigit():
        return None, "Supplier ID must be a number."

    # FIND SUPPLIER
    cursor.execute(
        "SELECT * FROM suppliers WHERE id = %s",
        (supplier_id,)
    )

    row = cursor.fetchone()

    # CHECK SUPPLIER EXISTS
    if row is None:
        return None, "Supplier ID not found."
    return row, None


def amend_supplier_record(
        cursor, conn, supplier_id, name, account, terms, 
        street, town, city, postcode, contactname, contactnum
):
    

    # AMEND SUPPLIER

    cursor.execute(
        "SELECT * FROM suppliers WHERE id = %s",
        (supplier_id,)
    )

    row = cursor.fetchone()

    # CHECK SUPPLIER EXISTS
    if row is None:
        return("Supplier ID not found.")
     

    # VALIDATE NEW SUPPLIER NAME
    name = name.strip()

    if name == "":
        return("Supplier name cannot be blank.")
    
    
    # VALIDATE NEW ACCOUNT NUMBER
    account = account.strip()

    if account == "":
        return("Supplier account number cannot be blank.")
    
    
    # VALIDATE NEW PAYMENT TERMS
    terms = terms.strip()

    if terms == "":
        return("Payment terms cannot be blank.")
    
    elif not terms.isdigit():
        return("Payment terms must be a number.")
    
    else:
        terms = int(terms)
    
    
    # VALIDATE NEW STREET
    street = street.strip()

    if street == "":
        return("Street cannot be blank.")
    
    
    # VALIDATE NEW TOWN
    town = town.strip()

    if town == "":
        return("Supplier town cannot be blank.")
    
    
    # ENTER NEW CITY
    city = city.strip()

    if city == "":
        return("Supplier city cannot be blank.")


    # ENTER NEW SUPPLIER POSTCODE
    postcode = postcode.strip().upper()
    postcode = postcode.replace(" ", "")

    if postcode == "":
        return("Supplier postcode cannot be blank.")

    elif not postcode.isalnum():
        return("Postcode must contain only letters and numbers.")

    elif len(postcode) < 5 or len(postcode) > 7:
        return("Postcode must be between 5 and 7 characters.")


    # ENTER NEW CONTACTNAME
    contactname = contactname.strip()

    if contactname == "":
        return("Supplier contact name cannot be blank.")


    # ENTER NEW CONTACTNUM
    contactnum = contactnum.strip()

    if contactnum == "":
        return("Contact number cannot be blank.")

    elif not contactnum.isdigit():
        return("Contact number must be a number.")

    elif len(contactnum) < 11 or len(contactnum) > 11:
        return("Contact number must be 11 number.")


    # UPDATE SUPPLIER IN DATABASE
    cursor.execute(
        """
        UPDATE suppliers
        SET name = %s, account = %s, terms = %s, street = %s,
            town = %s, city = %s, postcode = %s,
            contactname = %s, contactnum = %s,
            updated_at = CURRENT_TIMESTAMP
        WHERE id = %s
        """,
        (
            name,
            account,
            terms,
            street,
            town,
            city,
            postcode,
            contactname,
            contactnum,
            supplier_id
        )
    )

    conn.commit()

    return("\nSupplier amended.")
