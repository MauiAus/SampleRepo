import model

def start_View():
    print("Hi! Welcome to my simple covid database program!")
    print("\nYou have a few options to choose from so choose away!")
    print("\nTo View all the content, just enter the number 1.")
    print("\nTo create a new entry, just enter the number 2.")
    print("\nTo search an ID just enter the number 3.")
    print("\nTo look up someone based on their first name just enter the number 4.")
    print("\nTo drop an entry just enter the number 5.")
    print("\nTo visually display the data just enter the number 6.")
    print("\nTo exit, just type exit.")


def end_View():
    print("Goodbye! Thank you for using my program!")
    model.close_connection()


def view_all():
    rawlist = model.get_all()
    cleanList(rawlist)


def view_searchedID(id):
    rawlist = model.search_db(id)
    if not rawlist:
        print ("No results found for ID: "+ id)
    else:
        cleanList(rawlist)


def view_searchedbykeyword(keyword):
    rawlist = model.search_db_bykeyword(keyword)
    if not rawlist:
        print ("No results found for keyword: "+ keyword)
    else:
        cleanList(rawlist)

def view_del_entry(id):
    model.del_entry(id)
    print ("Entry with ID " + id + " has now been deleted.")

def cleanList(rawlist):
    for i in rawlist:
        print (i)