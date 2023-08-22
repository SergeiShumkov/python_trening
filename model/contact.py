from sys import maxsize
class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, company_name=None, home_phone_number=None, id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.company_name = company_name
        self.home_phone_number = home_phone_number
        self.id = id

    def __repr__(self):
        return f"{self.id}:{self.firstname}"

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

