# P.D.C.Ponciano, E.Serrano, D.E.G.Ty, F.S.Tale BES241
# plYellowProject December 3, 2020

#  Starting point for the Core of the Program:
import datetime
import pickle
from collections import defaultdict

def readmode(data):
    return open(data, "rb")


def writemode(data):
    return open(data, "wb")


def loadspeciallists(dx):  #  Used for d5 and above rank dictionaries.
    defaultdict(list, dx)


def main():
    while True:
        #  Preload the databanks (read-only mode):
        dat1 = readmode("bookXauthor.dat")
        dat2 = readmode("bookXpbdate.dat")
        dat3 = readmode("bookXavail.dat")
        dat4 = readmode("bookXcustloc.dat")
        dat5 = readmode("bookXbrwusers.dat")
        dat6 = readmode("bookXfrzusers.dat")
        dat7 = readmode("bookXbrwdate.dat")
        dat8 = readmode("bookXrtndate.dat")
        #  Declare individual databanks as variable:
        d1 = pickle.load(dat1)  # Author
        d2 = pickle.load(dat2)  # Published Date
        d3 = pickle.load(dat3)  # Numbers of Available Books
        d4 = pickle.load(dat4)  # Location
        d5 = pickle.load(dat5)  # Borrower Usernames
        d6 = pickle.load(dat6)  # Returnee Usernames
        d7 = pickle.load(dat7)  # Borrower Date
        d8 = pickle.load(dat8)  # Returnee Date
        #  Banner:
        print("\n\033[1mWelcome To Library\033[0m")
        print("How can we help you? \n")
        print("Please choose from the following commands below: ")
        print("֎ DISPLAY Book details(display), \n֎ ADD New Book(add), \n֎ CHANGE Book details(change)")
        print("֎ BORROW Book(borrow), \n֎ RETURN Book(return), \n֎ DELETE a Book(delete) ")
        print("or EXIT program(quit) \n")
        #  Initialize date acquisition script:
        Datenow = datetime.date.today().strftime("%B-%d-%Y")

        #  Definition for closing all currently-accessed databanks:
        def closedatabank():
            dat1.close()
            dat2.close()
            dat3.close()
            dat4.close()
            dat5.close()
            dat6.close()
            dat7.close()
            dat8.close()

        def repetition():
            return int(input("Please specify how many repetitions for this action: "))

        def nameinput():
            return str(input("Please input the name of the borrower: "))

        def bookinput():
            return str(input("Please input the book you want to borrow: "))

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
                    print(f"\033[1mBook Title:\033[0m ֎{i}֎ \n"
                          f"\033[1mBorrowed by:\033[0m © {d5[i]} \n"
                          f"\033[1mBorrowed on:\033[0m © {d6[i]} \n")
                elif x == "returnee":
                    print(f"\033[1mBook Title:\033[0m ֎{i}֎ \n"
                          f"\033[1mReturned by:\033[0m © {d5[i]} \n"
                          f"\033[1mReturned on:\033[0m © {d6[i]} \n")
                input("Press any key to continue.")
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
                # add into dictionary
                d1.update(e)
                d2.update(f)
                d3.update(g)
                d4.update(h)
                d5.update(i)
                d6.update(j)
                d7.update(k)
                d8.update(l)
                #  Store data to databank file:
                dat1 = writemode("bookXauthor.dat")
                dat2 = writemode("bookXpbdate.dat")
                dat3 = writemode("bookXavail.dat")
                dat4 = writemode("bookXcustloc.dat")
                dat5 = writemode("bookXbrwusers.dat")
                dat6 = writemode("bookXbrwdate.dat")
                dat7 = writemode("bookXfrzuser.dat")
                dat8 = writemode("bookXrtndate.dat")
                pickle.dump(d1, dat1)  # Author
                pickle.dump(d2, dat2)  # Published Date
                pickle.dump(d3, dat3)  # Numbers of Available Books
                pickle.dump(d4, dat4)  # Location
                pickle.dump(d5, dat5)  # Borrower Name
                pickle.dump(d6, dat6)  # Borrower Date
                pickle.dump(d7, dat7)  # Returnee Name
                pickle.dump(d8, dat8)  # Returnee Date
                for key in e:
                    print(f"The book '{key}' by {e[key]} is now added to the library.")
                    closedatabank()
                    input("Press any key to continue.")
        elif x == "change":
            q = repetition()
            print("Please enter 'B' for Book Title, 'A' for Author, 'D' for Date, "
                  "\n'S' for specifying the Location, 'N' for number of Books."
                  "\n'BN' for changing Borrower Name, 'BD' for Borrower Date."
                  "\n'RN' for changing Returnee Name, and 'RD' for Returnee Date.\n")
            for _ in range(0, q):
                q = str.upper(input("What would you like to change? "))
                if q == "B":
                    c = str(input("Please specify the name of the book you want to change the title: "))
                    # to check if input is in dictionary
                    d1[c] = d1[c]
                    d = str(input("Please specify the new title of the book: "))
                    d1[d] = d1.pop(c)
                    d2[d] = d2.pop(c)
                    d3[d] = d3.pop(c)
                    d4[d] = d4.pop(c)
                    d5[d] = d5.pop(c)
                    d6[d] = d6.pop(c)
                    d7[d] = d7.pop(c)
                    d8[d] = d8.pop(c)

                    #  Store data to databank file:
                    dat1 = writemode("bookXauthor.dat")
                    dat2 = writemode("bookXpbdate.dat")
                    dat3 = writemode("bookXavail.dat")
                    dat4 = writemode("bookXcustloc.dat")
                    pickle.dump(d1, dat1)  # Author
                    pickle.dump(d2, dat2)  # Published Date
                    pickle.dump(d3, dat3)  # Numbers of Available Books
                    pickle.dump(d4, dat4)  # Location
                    print(f"The name of the book '{c}' has been changed to '{d}'.")
                    closedatabank()
                    input("Press any key to continue.")
                elif q == "A":
                    c = str(input("Please specify the Book you want to change the author: "))
                    # to check if input is in dictionary
                    d1[c] = d1[c]
                    # change the value of the specific key
                    d1[c] = str(input("Book author: "))

                    #  Store data to databank file:
                    dat1 = writemode("bookXauthor.dat")
                    pickle.dump(d1, dat1)  # Author
                    print("{} author is {}".format(c, d1[c]))
                    closedatabank()
                    input("Press any key to continue.")
                elif q == "D":
                    c = str(input("Please specify the Book you want to change the date: "))
                    # to check if input is in dictionary
                    d2[c] = d2[c]
                    # change the value of the specific key
                    d2[c] = str(input("New time: "))

                    #  Store data to databank file:
                    dat2 = writemode("bookXpbdate.dat")
                    pickle.dump(d2, dat2)  # Published Date
                    print("The book '{}' publishing date is changed to {}.".format(c, d2[c]))
                    closedatabank()
                    input("Press any key to continue.")
                elif q == "N":
                    c = str(input("Please specify the Book you want to change the quantity of available books: "))
                    # to check if input is in dictionary
                    d3[c] = d3[c]
                    # change the value of the specific key
                    d3[c] = int(input("Number of books: "))

                    #  Store data to databank file:
                    dat3 = writemode("bookXavail.dat")
                    pickle.dump(d3, dat3)  # Numbers of Available Books
                    print("The book '{}' now has {} available cop(y/ies) in the library.".format(c, d3[c]))
                    closedatabank()
                    input("Press any key to continue.")
                elif q == "S":
                    c = str(input("Please specify the book you want to change: "))
                    # to check if input is in dictionary
                    d4[c] = d4[c]
                    # input the location directly into the dictionary.
                    loc = str(input("Please specify the location of the book (e.g. Horror): "))
                    d4[c] = loc

                    #  Store data to databank file:
                    dat4 = writemode("bookXcustloc.dat")
                    pickle.dump(d4, dat4)  # Location
                    print(f"The book '{c}' is now located at {loc} section.")
                    closedatabank()
                    input("Press any key to continue.")
                elif q == "BN":
                    name = str(input("Please specify the name of the borrower you want the name changed: "))
                    e = str(input("Please specify the book this person borrowed: "))
                    for key in dict(d1):
                        if key == e:
                            print(d5[e])
                            if name in d5[e]:
                                newname = str(input("Please specify the correct name for the borrower: "))
                                g = d5[e].index(name)
                                h = d5[e][g]
                                d5[e].remove(name)
                                d5[e].insert(g, newname)
                                print(d5[e][g])
                                #  Store data to databank file:
                                dat5 = writemode("bookXbrwusers.dat")
                                pickle.dump(d5, dat5)  # Borrowers Name
                                print("{} borrower {}'s name has been changed to {}".format(e, h, d5[e][g]))
                                closedatabank()
                                input("Press any key to continue.")
                else:
                    print("Book not found. Please try again!")
                    input("Press any key to continue.")
        elif x == "borrow":
            q = repetition()
            for _ in range(0, q):
                e = str(input("Please input the book you want to borrow: "))
                d3[e] = d3[e]
                if d3[e] > 0:
                    d3[e] -= 1
                    b = str(input("Please input the name of the borrower: "))
                    brwusers = {e.replace(" ", "_"): {'usn': b, 'date': Datenow}}
                    print(user[e.replace(" ", "_")]['usn'])
                    print(user[e.replace(" ", "_")]['date'])
                    user.append({brwusers})

                    #  Store data to databank file:
                    dat3 = writemode("bookXavail.dat")
                    dat5 = writemode("bookXbrwusers.dat")
                    pickle.dump(d3, dat3)  # Numbers of Available Books
                    pickle.dump(user, dat5)
                    print(f"The book '{e}' is borrowed by {b} at this library on {Datenow}.")
                    closedatabank()
                    input("Press any key to continue.")
                else:
                    print(f"No more remaining cop(y/ies) for '{e}' book available.")
                    input("Press any key to continue.")
        elif x == "return":
            q = repetition()
            for _ in range(0, q):
                e = bookinput()
                name = nameinput()
                for key in dict(d1):
                    if key == e:
                        d3[e] += 1
                        print(d5[e])
                        print(d5)
                        d5[e].remove(name)
                        print(d5[e])

                        #  Store data to databank file:
                        dat3 = writemode("bookXavail.dat")
                        dat5 = writemode("bookXbrwusers.dat")
                        pickle.dump(d3, dat3)  # Numbers of Available Books
                        pickle.dump(d5, dat5)
                        print(f"The book '{e}' has just been returned to this library by {name} on {Datenow}.")
                        closedatabank()
                        input("Press any key to continue.")
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
                input("Press any key to continue.")
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
        print("Book currently not available. Please check if there are spelling mistakes, "
              "\nor you might need to add this book to the system.")
        input("Press any key to continue.")
    except ValueError:
        print("Wrong input. Please check your inputs and retry.")
        input("Press any key to continue.")
        continue
      
#  Framework of the Program ends here!
