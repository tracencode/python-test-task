class Lead:
    def __init__(self, name=None, email=None, phone=None):
        self.name = name
        self.email = email
        self.phone = phone

    def __repr__(self):
        return f"Lead(name={self.name}, email={self.email}, phone={self.phone})"

    def update(self, registrant):
        # Update contact with registrant details if missing
        if not self.name and registrant['name']:
            self.name = registrant['name']
        if not self.email and registrant['email']:
            self.email = registrant['email']
        if not self.phone and registrant['phone']:
            self.phone = registrant['phone']