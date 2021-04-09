import sqlite3
import os
from datetime import datetime

# Connecting python program to database
pathname = __file__
pathname = pathname[:-8]

conn = sqlite3.connect(
     pathname + 'cov.db')
c = conn.cursor()


class Person(object):

    def __init__(self, dateTime, id, last_name, first_name, address, contact_number, last_location):
        self.id = id
        self.dateTime = dateTime
        self.last_name = last_name
        self.first_name = first_name
        self.address = address
        self.contact_number = contact_number
        self.last_location = last_location

        insert_db(self.id, self.dateTime, self.last_name, self.first_name,
                  self.address, self.contact_number, self.last_location)

#Add ka dito ng function na kukuha ng data from database tapos icchart gamit matplot lib tapos route mo siya papunta sa view file
#then yung view file yung mag format kung anong itsura ng chart na trip mo palabasin then add ka ng option sa controller para sa user if gusto niya makita charts

def get_all():
    c.execute("SELECT * FROM cov_tracker ")
    fetched_list = c.fetchall()
    conn.commit()

    return fetched_list


def create_person():
    Person(str(datetime.now()),input("Enter ID: "), input("Enter Last name: "), input("Enter First name: "), input(
        "Enter Address: "),  input("Enter Contact number: "), input("Enter Last location: "))


def insert_db(id, dateTime, last_name, first_name, address, contact_number, last_location):
    c.execute("INSERT INTO cov_tracker VALUES (:id, :datetime, :lastn, :firstn, :address, :cn, :lastloc )", {
              'id': id, 'datetime' :dateTime, 'lastn': last_name, 'firstn': first_name, 'address': address, 'cn': contact_number, 'lastloc': last_location})
    conn.commit()



def search_db(id):
    c.execute("SELECT * FROM cov_tracker WHERE ID = :id", {'id': id})
    fetched_list = c.fetchall()
    conn.commit()

    return fetched_list


def search_db_bykeyword(keyword):
    c.execute("SELECT * FROM cov_tracker WHERE FIRST_NAME LIKE ?",
              ('%'+keyword+'%',))
    fetched_list = c.fetchall()
    conn.commit()

    return fetched_list

def del_entry(id):
    c.execute("DELETE FROM cov_tracker WHERE ID = :id", {'id': id})
    conn.commit()


def close_connection():
    conn.close()
