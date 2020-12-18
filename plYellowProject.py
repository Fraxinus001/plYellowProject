# P.D.C.Ponciano, E.Serrano, D.E.G.Ty, F.S.Tale BES241
# plYellowProject December 3, 2020

#  Starting point for the Core of the Program:
import datetime
import pickle
from collections import defaultdict

'''import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.login("notifieremail", "password")

msg = f"Hello! Your book titled {BookName} is due return on {ReturnDate}.\n" \
      f"-{OrganizationName}"
server.sendmail("usermail@donbosco.edu.ph", "usermail@donbosco.edu.ph", msg)'''

def readmode(data):
    return open(data, "rb")


def writemode(data):
    return open(data, "wb")


def loadspeciallists(dx):  # Used for d5 and above rank dictionaries.
    return defaultdict(list, dx)


def err_booknotfound():
    a = print("Book not found in the records. Please check if there are spelling mistakes, "
              "\nor you might need to add this book to the system first.")
    b = input("Press enter key to continue.")
    return a, b


def err_brwrmissing():
    a = print("There was no record that the borrower borrowed this book. Please recheck.")
    b = input("Press enter key to continue.")
    return a, b


def main():
    while True:
        #  Preload the databanks (read-only mode):
        dat1 = readmode("bookXauthor.dat")
        dat2 = readmode("bookXpbdate.dat")
        dat3 = readmode("bookXavail.dat")
        dat4 = readmode("bookXcustloc.dat")
        dat5 = readmode("bookXbrwusers.dat")
        dat6 = readmode("bookXbrwdate.dat")  # Error Corrected
        dat7 = readmode("bookXfrzusers.dat")  # Error Corrected
        dat8 = readmode("bookXrtndate.dat")
        dat5b = readmode("bookXbrwmail.dat")
        #  Declare individual databanks as variable:
        d1 = pickle.load(dat1)  # Author
        d2 = pickle.load(dat2)  # Published Date
        d3 = pickle.load(dat3)  # Numbers of Available Books
        d4 = pickle.load(dat4)  # Location
        d5 = pickle.load(dat5)  # Borrower Usernames
        d6 = pickle.load(dat6)  # Borrower Date  # Error Corrected
        d7 = pickle.load(dat7)  # Returnee Usernames  # Error Corrected
        d8 = pickle.load(dat8)  # Returnee Date
        d5b = pickle.load(dat5b)  # Borrower E-Mail Addresses
        #  Banner:
        print("\n\033[1mWelcome To Library\033[0m")
        print("How can we help you? \n")
        print("Please choose from the following commands below: ")
        print("֎ DISPLAY Book details(display), \n֎ ADD New Book(add), \n֎ CHANGE Book details(change)")
        print("֎ BORROW Book(borrow), \n֎ RETURN Book(return), \n֎ DELETE a Book(delete) ")
        print("or QUIT program(quit) \n")
        #  Initialize date acquisition script:
        Datenow = datetime.date.today().strftime("%B %d, %Y")

        #  Definition for closing all currently-accessed databanks:
        def closedatabank():
            dat1.close(), dat2.close(), dat3.close(), dat4.close(), dat5.close(), dat6.close(), dat7.close(), \
                dat8.close(), dat5b.close()

        def repetition():
            return int(input("Please specify how many repetitions for this action: "))

        def nameinputr():
            return str(input("Please input the name of the borrower: "))

        def bookinputr():
            return str(input("Please input the book that has been borrowed: "))

        #  Core Program ends here!

        #  Starting point for the framework:
        x = str.lower(input("Please input the course of action to do: "))
        if x == "display":
            q = repetition()
            for _ in range(0, q):
                # input for the key
                i = str(input("Please specify the book title: "))
                # display output
                print(f"\033[1mBook Title:\033[0m ֎ {i} ֎ \n"
                      f"\033[1mBook Author:\033[0m © {d1[i]} \n"
                      f"\033[1mBook Publishing Date:\033[0m {d2[i]} \n"
                      f"\033[1mBook Location:\033[0m {d4[i]} Section \n"
                      f"\033[1mBook Cop(y/ies) Remaining:\033[0m {d3[i]} \n")
                print("Please choose from the following commands below: ")
                print("֎ BORROWER Display details of who borrowed this book and when(borrower), \n")
                print("֎ RETURNEE Display details of who returned this book and when(returnee) \n")
                x = str.lower(input("Please input the course of action to do: "))
                if x == "borrower":
                    d5 = loadspeciallists(d5)
                    d6 = loadspeciallists(d6)
                    d5b = loadspeciallists(d5b)
                    for key in dict(d1):
                        if key == i:
                            print(f"\033[1mBook Title:\033[0m ֎ {i} ֎ \n"
                                  f"\033[1mBorrowed by:\033[0m {d5[i]} \n"
                                  f"\033[1mBorrowed on:\033[0m {d6[i]} \n"
                                  f"\033[1mContact Email:\033[0m {d5b[i]} \n")
                elif x == "returnee":
                    d7 = loadspeciallists(d7)
                    d8 = loadspeciallists(d8)
                    for key in dict(d1):
                        if key == i:
                            print(f"\033[1mBook Title:\033[0m ֎ {i} ֎ \n"
                                  f"\033[1mReturned by:\033[0m {d7[i]} \n"
                                  f"\033[1mReturned on:\033[0m {d8[i]} \n")
                input("Press enter key to continue.")
        elif x == "add":
            q = repetition()
            for _ in range(0, q):
                print("Add new Book. Please specify the necessary information on the queries to follow: ")
                a = str(input("Book title: "))
                b = str(input("Book author: "))
                c = str(input("Published date(MM/DD/YYYY): "))
                loc = str(input("In what shelf should the book be stored?: "))
                d = int(input("How many cop(y/ies) of this book will be available?: "))
                e = {a: b}
                f = {a: c}
                g = {a: d}
                h = {a: loc}
                i = {a: ''}
                j = {a: ''}
                k = {a: ''}
                l = {a: ''}
                m = {a: ''}
                # add into dictionary
                d1.update(e)
                d2.update(f)
                d3.update(g)
                d4.update(h)
                d5.update(i)
                d6.update(j)
                d7.update(k)
                d8.update(l)
                d5b.update(m)
                #  Store data to databank file:
                dat1 = writemode("bookXauthor.dat")
                dat2 = writemode("bookXpbdate.dat")
                dat3 = writemode("bookXavail.dat")
                dat4 = writemode("bookXcustloc.dat")
                dat5 = writemode("bookXbrwusers.dat")
                dat6 = writemode("bookXbrwdate.dat")
                dat7 = writemode("bookXfrzuser.dat")
                dat8 = writemode("bookXrtndate.dat")
                dat5b = writemode("bookXbrwmail.dat")
                pickle.dump(d1, dat1)  # Author
                pickle.dump(d2, dat2)  # Published Date
                pickle.dump(d3, dat3)  # Numbers of Available Books
                pickle.dump(d4, dat4)  # Location
                pickle.dump(d5, dat5)  # Borrower Name
                pickle.dump(d6, dat6)  # Borrower Date
                pickle.dump(d7, dat7)  # Returnee Name
                pickle.dump(d8, dat8)  # Returnee Date
                pickle.dump(d5b, dat5b)  # Borrower Email
                for key in e:
                    print(f"The book '{key}' by {e[key]} is now added to the library.")
                    closedatabank()
                    input("Press enter key to continue.")
        elif x == "change":
            q = repetition()
            print("Please enter 'B' for Book Title, 'A' for Author, 'D' for Date, "
                  "\n'S' for specifying the Location, 'N' for number of Books,"
                  "\n'BN' for changing Borrower Name, 'BD' for Borrower Date,"
                  "\n'BM' for changing Borrower's Email Address,"
                  "\n'RN' for changing Returnee Name, and 'RD' for Returnee Date.\n")
            for _ in range(0, q):
                q = str.upper(input("What would you like to change? "))
                if q == "B":
                    c = str(input("Please specify the name of the book you want to change the title: "))
                    # to check if input is in dictionary
                    if c in dict(d1):
                        d = str(input("Please specify the new title of the book: "))
                        d1[d] = d1.pop(c)
                        d2[d] = d2.pop(c)
                        d3[d] = d3.pop(c)
                        d4[d] = d4.pop(c)
                        d5[d] = d5.pop(c)
                        d6[d] = d6.pop(c)
                        d7[d] = d7.pop(c)
                        d8[d] = d8.pop(c)
                        d5b[d] = d5b.pop(c)

                        #  Store data to databank file:
                        dat1 = writemode("bookXauthor.dat")
                        dat2 = writemode("bookXpbdate.dat")
                        dat3 = writemode("bookXavail.dat")
                        dat4 = writemode("bookXcustloc.dat")
                        dat5 = writemode("bookXbrwusers.dat")
                        dat6 = writemode("bookXbrwdate.dat")
                        dat7 = writemode("bookXfrzuser.dat")
                        dat8 = writemode("bookXrtndate.dat")
                        dat5b = writemode("bookXbrwmail.dat")
                        pickle.dump(d1, dat1)  # Author
                        pickle.dump(d2, dat2)  # Published Date
                        pickle.dump(d3, dat3)  # Numbers of Available Books
                        pickle.dump(d4, dat4)  # Location
                        pickle.dump(d5, dat5)  # Borrower Name
                        pickle.dump(d6, dat6)  # Borrower Date
                        pickle.dump(d7, dat7)  # Returnee Name
                        pickle.dump(d8, dat8)  # Returnee Date
                        pickle.dump(d5b, dat5b)  # Borrower Email
                        print(f"The name of the book '{c}' has been changed to '{d}'.")
                        closedatabank()
                        input("Press enter key to continue.")
                    else:
                        err_booknotfound()
                elif q == "A":
                    c = str(input("Please specify the Book you want to change the author: "))
                    # to check if input is in dictionary
                    if c in dict(d1):
                        u = d1[c]
                        # change the value of the specific key
                        d1[c] = str(input("Book author: "))

                        #  Store data to databank file:
                        dat1 = writemode("bookXauthor.dat")
                        pickle.dump(d1, dat1)  # Author
                        print(f"'{c}' book author has been changed from '{u}' to '{d1[c]}'")
                        closedatabank()
                        input("Press enter key to continue.")
                    else:
                        err_booknotfound()
                elif q == "D":
                    c = str(input("Please specify the Book you want to change the date: "))
                    # to check if input is in dictionary
                    if c in dict(d1):
                        # change the value of the specific key
                        u = d2[c]
                        d2[c] = str(input("New time: "))

                        #  Store data to databank file:
                        dat2 = writemode("bookXpbdate.dat")
                        pickle.dump(d2, dat2)  # Published Date
                        print("The book '{}' publishing date is changed from '{}' to '{}'.".format(c, u, d2[c]))
                        closedatabank()
                        input("Press enter key to continue.")
                    else:
                        err_booknotfound()
                elif q == "N":
                    c = str(input("Please specify the Book you want to change the quantity of available books: "))
                    # to check if input is in dictionary
                    if c in dict(d1):
                        # change the value of the specific key
                        d3[c] = int(input("Number of books: "))

                        #  Store data to databank file:
                        dat3 = writemode("bookXavail.dat")
                        pickle.dump(d3, dat3)  # Numbers of Available Books
                        print("The book '{}' now has {} available cop(y/ies) in the library.".format(c, d3[c]))
                        closedatabank()
                        input("Press enter key to continue.")
                    else:
                        err_booknotfound()
                elif q == "S":
                    c = str(input("Please specify the book you want to change: "))
                    # to check if input is in dictionary
                    if c in dict(d1):
                        # input the location directly into the dictionary.
                        loc = str(input("Please specify the location of the book (e.g. Horror): "))
                        d4[c] = loc

                        #  Store data to databank file:
                        dat4 = writemode("bookXcustloc.dat")
                        pickle.dump(d4, dat4)  # Location
                        print(f"The book '{c}' is now located at {loc} section.")
                        closedatabank()
                        input("Press enter key to continue.")
                    else:
                        err_booknotfound()
                elif q == "BN":
                    name = str(input("Please specify the name of the borrower you want the name changed: "))
                    e = str(input("Please specify the book this person borrowed: "))
                    d5 = loadspeciallists(d5)
                    if e in dict(d1):
                        if name in d5[e]:
                            newname = str(input("Please specify the correct name for the borrower: "))
                            g = d5[e].index(name)
                            h = d5[e][g]
                            d5[e].remove(name)
                            d5[e].insert(g, newname)
                            #  Store data to databank file:
                            dat5 = writemode("bookXbrwusers.dat")
                            pickle.dump(d5, dat5)  # Borrowers Name
                            print(f"{e} borrower {h}'s name has been changed from {h} to {d5[e][g]}.")
                            closedatabank()
                            input("Press enter key to continue.")
                        else:
                            err_brwrmissing()
                elif q == "BD":
                    name = str(input("Please specify the name of the borrower you want the borrowing date changed: "))
                    e = str(input("Please specify the book this person borrowed: "))
                    d5 = loadspeciallists(d5)
                    d6 = loadspeciallists(d6)
                    if e in dict(d1):
                        if name in d5[e]:
                            newdate = str(input("Please follow the following example in entering the proper date;\n"
                                                "Example: 'December 18, 2020'\n"
                                                "Please specify the correct date of borrowing for the borrower: "))
                            g = d5[e].index(name)
                            h = d5[e][g]
                            i = d6[e][g]
                            d6[e].remove(i)
                            d6[e].insert(g, newdate)

                            #  Store data to databank file:
                            dat6 = writemode("bookXbrwdate.dat")
                            pickle.dump(d6, dat6)  # Borrowers Date
                            print(f"{e} borrower {h}'s borrowing date has been changed to {d6[e][g]}.")
                            closedatabank()
                            input("Press enter key to continue.")
                        else:
                            err_brwrmissing()
                    else:
                        err_booknotfound()
                elif q == "BM":
                    name = str(input("Please specify the name of the borrower you want the Email changed: "))
                    e = str(input("Please specify the book this person borrowed: "))
                    d5 = loadspeciallists(d5)
                    d6 = loadspeciallists(d6)
                    if e in dict(d1):
                        if name in d5[e]:
                            newmail = str(input("Please specify the correct Email for the borrower: "))
                            g = d5[e].index(name)
                            h = d5[e][g]
                            i = d5b[e][g]
                            d5b[e].remove(i)
                            d5b[e].insert(g, newmail)
                            print(d6[e])  # Debug

                            #  Store data to databank file:
                            dat6 = writemode("bookXbrwdate.dat")
                            pickle.dump(d6, dat6)  # Borrowers Date
                            print("{} borrower {}'s Email has been changed from {} to {}".format(e, h, i, d5b[e][g]))
                            closedatabank()
                            input("Press enter key to continue.")
                        else:
                            err_brwrmissing()
                    else:
                        err_booknotfound()
                elif q == "RN":
                    name = str(input("Please specify the name of the borrower you want the name changed: "))
                    e = str(input("Please specify the book this person borrowed: "))
                    d7 = loadspeciallists(d7)
                    if e in dict(d1):
                        if name in d7[e]:
                            newname = str(input("Please specify the correct name for the borrower: "))
                            g = d7[e].index(name)
                            h = d7[e][g]
                            d7[e].remove(name)
                            d7[e].insert(g, newname)
                            #  Store data to databank file:
                            dat7 = writemode("bookXfrzusers.dat")
                            pickle.dump(d7, dat7)  # Returnees Name
                            print("{} past borrower {}'s name has been changed to {}".format(e, h, d7[e][g]))
                            closedatabank()
                            input("Press enter key to continue.")
                        else:
                            err_brwrmissing()
                    else:
                        err_booknotfound()
                elif q == "RD":
                    name = str(input("Please specify the name of the borrower you want the date changed: "))
                    e = str(input("Please specify the book this person borrowed: "))
                    d7 = loadspeciallists(d7)
                    d8 = loadspeciallists(d8)
                    if e in dict(d1):
                        if name in d7[e]:
                            newdate = str(input("Please specify the correct date of borrowing for the borrower: "))
                            g = d7[e].index(name)
                            h = d7[e][g]
                            i = d8[e][g]
                            d8[e].remove(i)
                            d8[e].insert(g, newdate)

                            #  Store data to databank file:
                            dat8 = writemode("bookXrtndate.dat")
                            pickle.dump(d8, dat8)  # Returnees Date
                            print("{} borrower {}'s borrowing date has been changed to {}".format(e, h, d8[e][g]))
                            closedatabank()
                            input("Press enter key to continue.")
                        else:
                            err_brwrmissing()
                    else:
                        err_booknotfound()
        elif x == "borrow":
            q = repetition()
            for _ in range(0, q):
                e = str(input("Please input the book that will be borrowed: "))
                if d3[e] > 0:
                    d3[e] -= 1
                    print("Please specify the following queries regarding the borrower carefully: ")
                    b = str(input("Name: "))
                    c = str(input("E-Mail Address: "))
                    d5 = loadspeciallists(d5)
                    d6 = loadspeciallists(d6)
                    d5b = loadspeciallists(d5b)
                    if e in d1:
                        d5[e].insert(-1, b)
                        d6[e].insert(-1, Datenow)
                        d5b[e].insert(-1, c)

                        #  Store data to databank file:
                        dat3 = writemode("bookXavail.dat")
                        dat5 = writemode("bookXbrwusers.dat")
                        dat6 = writemode("bookXbrwdate.dat")
                        dat5b = writemode("bookXbrwmail.dat")
                        pickle.dump(d3, dat3)  # Numbers of Available Books
                        pickle.dump(d5, dat5)  # Borrower Name
                        pickle.dump(d6, dat6)  # Borrowing Date
                        pickle.dump(d5b, dat5b)  # Borrower Email
                        print(f"A copy of book '{e}' has been borrowed by {b} at this library on {Datenow}.")
                        closedatabank()
                        input("Press enter key to continue.")
                else:
                    print(f"No more remaining cop(y/ies) for '{e}' book available.")
                    input("Press enter key to continue.")
        elif x == "return":
            q = repetition()
            for _ in range(0, q):
                e = bookinputr()
                name = nameinputr()
                d5 = loadspeciallists(d5)
                d6 = loadspeciallists(d6)
                if e in dict(d1):
                    if name in d5[e]:
                        d3[e] += 1
                        r = d5[e].index(name)
                        d5[e].remove(name)
                        d6[e].pop(r)
                        d7[e].insert(-1, name)
                        d8[e].insert(-1, Datenow)

                        #  Store data to databank file:
                        dat3 = writemode("bookXavail.dat")
                        dat5 = writemode("bookXbrwusers.dat")
                        dat6 = writemode("bookXbrwdate.dat")
                        dat7 = writemode("bookXfrzusers.dat")
                        dat8 = writemode("bookXrtndate.dat")
                        pickle.dump(d3, dat3)  # Numbers of Available Books
                        pickle.dump(d5, dat5)  # Borrowers Name
                        pickle.dump(d6, dat6)  # Borrowing Date
                        pickle.dump(d7, dat7)  # Returnees Name
                        pickle.dump(d8, dat8)  # Return Date
                        print(f"The book '{e}' has just been returned to this library by {name} on {Datenow}.")
                        closedatabank()
                        input("Press enter key to continue.")
                    else:
                        err_brwrmissing()
        elif x == "delete":
            print("Delete a book")
            q = repetition()
            for _ in range(0, q):
                d = str(input("Input the book you want to delete: "))
                # to check if input is in dictionary
                d1[d] = d1[d]
                # delete a key:value pair
                d1.pop(d)
                d2.pop(d)
                d3.pop(d)
                d4.pop(d)
                q = str.lower(input("Do you also want to delete the book borrow and return history? (Y)es or (N)o?"))
                if q == "y":
                    d5 = loadspeciallists(d5)
                    d6 = loadspeciallists(d6)
                    d7 = loadspeciallists(d7)
                    d8 = loadspeciallists(d8)
                    d5b = loadspeciallists(d5b)
                    d5.pop(d)
                    d6.pop(d)
                    d7.pop(d)
                    d8.pop(d)
                    d5b.pop(d)
                    dat5 = readmode("bookXbrwusers.dat")
                    dat6 = readmode("bookXbrwdate.dat")
                    dat7 = readmode("bookXfrzusers.dat")
                    dat8 = readmode("bookXrtndate.dat")
                    dat5b = readmode("bookXbrwmail.dat")
                    pickle.dump(d5, dat5)  # Author
                    pickle.dump(d6, dat6)  # Published Date
                    pickle.dump(d7, dat7)  # Numbers of Available Books
                    pickle.dump(d8, dat8)  # Location
                    pickle.dump(d5b, dat5b)
                    print("The histories were also deleted.")
                if q != "y":
                    print("The histories were not deleted.")

                #  Store data to databank file:
                dat1 = writemode("bookXauthor.dat")
                dat2 = writemode("bookXpbdate.dat")
                dat3 = writemode("bookXavail.dat")
                dat4 = writemode("bookXcustloc.dat")
                pickle.dump(d1, dat1)  # Author
                pickle.dump(d2, dat2)  # Published Date
                pickle.dump(d3, dat3)  # Numbers of Available Books
                pickle.dump(d4, dat4)  # Location
                print("The book '{}' is deleted from the library.".format(d))
                closedatabank()
                input("Press enter key to continue.")
        elif x == "quit":
            print("Thank You!")
            # close the program
            closedatabank()
            exit()
        else:
            print("Please select from course of actions above.")


while True:
    try:
        main()
    except KeyError:
        err_booknotfound()
    except ValueError:
        print("Wrong input. Please double-check your inputs and retry.")
        input("Press enter key to continue.")
        continue
      
#  Framework of the Program ends here!
