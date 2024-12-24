def validate_phone_number(phone_number):
    if phone_number is None:
        return True

    # Check if the phone number contains only digits and has exactly 10 characters
    return phone_number.isdigit() and len(phone_number) == 10


def register_user():
    # Taking input from the user (simulating registration)
    name = input("Enter your name: ").strip()
    email = input("Do you have an email? (yes/no): ").strip().lower()
    email = input("Enter your email: ").strip() if email == "yes" else None
    phone = input("Do you have a phone number? (yes/no): ").strip().lower()
    phone = input("Enter your phone number: ").strip() if phone == "yes" else None

    if not validate_phone_number(phone):
        print("Phone number is invalid. It must be exactly 10 digits and contain no other characters.")
        return {}

    if phone == None and email == None:
        print("Phone and Email both can not be empty!")
        return {}
    else:
        return {"name": name, "email": email, "phone": phone}
