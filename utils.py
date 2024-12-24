from contact import Contact

def match_and_add_contact(contacts, leads, registrant):
    # Try to match registrant's email to our list of contacts
    for contact in contacts:
        if contact.email == registrant['email'] and contact.email != None:
            contact.update(registrant)
            return contacts, leads

    # Try to match registrant's phone to our contacts
    for contact in contacts:
        if contact.phone == registrant['phone'] and contact.phone != None:
            contact.update(registrant)
            return contacts, leads

    # Try to match leads with email
    for lead in leads:
        if lead.email == registrant['email'] and lead.email != None:
            lead.update(registrant)
            contacts.append(Contact(lead.name, lead.email, lead.phone))
            leads.remove(lead)
            return contacts, leads

    # Try to match leads with phone
    for lead in leads:
        if lead.phone == registrant['phone'] and lead.phone != None:
            lead.update(registrant)
            contacts.append(Contact(lead.name, lead.email, lead.phone))
            leads.remove(lead)
            return contacts, leads


    # If no match is found, add to contacts
    contacts.append(Contact(registrant['name'], registrant['email'], registrant['phone']))
    return contacts, leads