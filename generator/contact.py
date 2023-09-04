import sys
import getopt
import random
import string
import jsonpickle
import os.path

from model.contact import Contact


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_string_for_name(prefix, maxlen):
    symbols = string.ascii_letters
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


# string.punctuation +  +  " "*10
def random_string_for_phone(maxlen):
    symbols = string.digits + "- ()+"
    return  "".join([random.choice(symbols) for i in range(random.randrange(4, maxlen))])


def random_string_for_email(maxlen):
    symbols = string.ascii_letters + string.digits
    return "".join([random.choice(symbols) for i in range(random.randrange(2, maxlen))]) + "@" + "".join([random.choice(symbols) for i in range(random.randrange(2, maxlen))]) + ".com"


testdata = [Contact(firstname="", lastname="", homephone="", mobilephone="", workphone="", secondaryphone="", address="",
                 email1="", email2="", email3="")] + [
        Contact(firstname=random_string_for_name("firstname", 10), lastname=random_string_for_name("lastname", 10),
                homephone=random_string_for_phone(10),  mobilephone=random_string_for_phone(10),
                workphone=random_string_for_phone(10), secondaryphone=random_string_for_phone(10),
                address=random_string("address", 20), email1=random_string_for_email(7),
                email2=random_string_for_email(7), email3=random_string_for_email(7))

        for i in range(n)
    ]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    # out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))