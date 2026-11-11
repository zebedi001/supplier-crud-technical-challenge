
# ADD SUPPLIER BACKEND

def add_supplier_record(
    cursor, conn,
    name, account, terms,
    street, town, city, postcode,
    contactname, contactnum
):

    name = name.strip()
    if name == "":
        return "Supplier name cannot be blank."
    
    account = account.strip()
    if account == "":
        return "Supplier account number cannot be blank."

    terms = terms.strip()
    if terms == "":
        return "Payment terms cannot be blank."
    elif not terms.isdigit():
        return "Payment terms must be a number."
    else:
        terms = int(terms)

    street = street.strip()
    if street == "":
        return "Supplier street cannot be blank."

    town = town.strip()
    if town == "":
        return "Supplier town cannot be blank."

    city = city.strip()
    if city == "":
        return "Supplier city cannot be blank."

    postcode = postcode.strip().upper()
    postcode = postcode.replace(" ", "")

    if postcode == "":
        return "Supplier postcode cannot be blank."
    elif not postcode.isalnum():
        return "Postcode must contain only letters and numbers."
    elif len(postcode) < 5 or len(postcode) > 7:
        return "Postcode must be between 5 and 7 characters."

    contactname = contactname.strip()
    if contactname == "":
        return "Supplier contact name cannot be blank."

    contactnum = contactnum.strip()
    if contactnum == "":
        return "Supplier contact number cannot be blank."
    elif not contactnum.isdigit():
        return "Contact number must be a number."
    elif len(contactnum) < 11 or len(contactnum) > 11:
        return "Contact number must be 11 number."

    # ADD SUPPLIER TO DATABASE
    cursor.execute(
        "INSERT INTO suppliers "
        "(name, account, terms, street, town, city, postcode, "
        "contactname, contactnum) "
        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
        (
            name,
            account,
            terms,
            street,
            town,
            city,
            postcode,
            contactname,
            contactnum
        )
    )   

    conn.commit()   

    return "Supplier added successfully."


