import pymysql.cursors

from model.group import Group
from model.contact import Contact


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list = []
        with self.connection.cursor() as cursor:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name,header=header, footer=footer))
        return list

    # def get_group_list(self):
    #     cursor = self.connection.cursor()
    #     try:
    #         pass
    #     finally:
    #         cursor.close()

    def get_contact_list(self):
        list = []
        with self.connection.cursor() as cursor:
            cursor.execute("select id, firstname, lastname, address, home, mobile, work, phone2, email, email2, email3 from addressbook where deprecated='000-00-00 00:00:00'")
            # cursor.execute("select id, firstname, lastname from addressbook")
            for row in cursor:
                (id, firstname, lastname, address, home, mobile, work, phone2, email, email2, email3) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname, address=address, homephone=home,
                                    mobilephone=mobile, workphone=work, secondaryphone=phone2, email1=email, email2=email2, email3=email3))
        return list


    def destroy(self):
        self.connection.close()
