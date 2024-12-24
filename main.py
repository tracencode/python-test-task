from contact import Contact
from lead import Lead
from utils import match_and_add_contact
from register import register_user

# Initial/Demo contacts data
contacts = [
    Contact("Alice Brown", None, "1231112223"),
    Contact("Bob Crown", "bob@crowns.com", None),
    Contact("Carlos Drew", "carl@drewess.com", "3453334445"),
    Contact("Doug Emerty", None, "4564445556"),
    Contact("Egan Fair", "eg@fairness.com", "5675556667")
]

# Initial/Demo leads data
leads = [
    Lead(None, "kevin@keith.com", None),
    Lead("Lucy", "lucy@liu.com", "3210001112"),
    Lead("Mary Middle", "mary@middle.com", "3331112223"),
    Lead(None, None, "4442223334"),
    Lead(None, "ole@olson.com", None)
]

def process_registration(contacts, leads):
    # Allow the user to register and then process the registration
    while True:
        print("\nRegister for the Webinar!")
        registrant = register_user()
        if registrant == {}:
            continue
        contacts, leads = match_and_add_contact(contacts, leads, registrant)

        # Ask if the user wants to register more people
        another = input("\nDo you want to register another user? (yes/no): ").strip().lower()
        if another != "yes":
            break

    # Output the final contacts list
    print("\nFinal Contacts List:")
    for contact in contacts:
        print(contact)

# Start the registration process
process_registration(contacts, leads)

