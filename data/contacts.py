
# import random
# import string
from model.contact import Contact


testdata = [
    Contact(firstname="firstname1", lastname="lastname1", homephone="homephone1", mobilephone="mobilephone1",
             workphone="workphone1", secondaryphone="secondaryphone1", address="address1", email1="email11",
             email2="email21", email3="email31"),
    Contact(firstname="firstname2", lastname="lastname2", homephone="homephone2", mobilephone="mobilephone2",
             workphone="workphone2", secondaryphone="secondaryphone2", address="address2", email1="email12",
             email2="email22", email3="email32")
]


# def random_string(prefix, maxlen):
#     symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
#     return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
#
#
# def random_string_for_name(prefix, maxlen):
#     symbols = string.ascii_letters
#     return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
#
#
# # string.punctuation +  +  " "*10
# def random_string_for_phone(maxlen):
#     symbols = string.digits + "- ()+"
#     return  "".join([random.choice(symbols) for i in range(random.randrange(4, maxlen))])
#
#
# def random_string_for_email(maxlen):
#     symbols = string.ascii_letters + string.digits
#     return "".join([random.choice(symbols) for i in range(random.randrange(2, maxlen))]) + "@" + "".join([random.choice(symbols) for i in range(random.randrange(2, maxlen))]) + ".com"
#
#
# testdata = [Contact(firstname="", lastname="", homephone="", mobilephone="", workphone="", secondaryphone="", address="",
#                  email1="", email2="", email3="")] + [
#         Contact(firstname=random_string_for_name("firstname", 10), lastname=random_string_for_name("lastname", 10),
#                 homephone=random_string_for_phone(10),  mobilephone=random_string_for_phone(10),
#                 workphone=random_string_for_phone(10), secondaryphone=random_string_for_phone(10),
#                 address=random_string("address", 20), email1=random_string_for_email(7),
#                 email2=random_string_for_email(7), email3=random_string_for_email(7))
#
#         for i in range(5)
#     ]