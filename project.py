import datetime

d1 = {"red": "taylor swift", "attack on tale": "francis", "the life of ty": "boss philip"}  # author
d2 = {"red": "June 21,2001", "attack on dolomite": "November 28,2021",
      "the life of ty": "December 1,2001"}  # published date
d3 = {"red": 1, "attack on dolomite": 13, "the life of ty": 200}  # numbers of available books

print("\nWelcome To Library")
print("How can we help you? \n")
print("Please choose the following: display book details(display), add new book(add), change details(change)")
print("borrow book(borrow), return book(return), delete a book(delete) or exit program(quit) \n")

Datenow = datetime.date.today().strftime("%B-%d-%Y")


def main():
    while True:
        x = str(input("Please input the course of action to do: "))
        if x == "display":
            # input for the key
            i = str(input("Please specify the book title: "))
            # display output
            print(f"The book '{i}' by {d1[i]} is published in {d2[i]}, this book still has {d3[i]} available in the "
                  f"library.")
        elif x == "add":
            print("Add new Book. Please specify the necessary information on the input to be followed: ")
            a = str(input("Book title: "))
            b = str(input("Book author: "))
            c = str(input("Published date(M/D/Y): "))
            d = int(input("How many books will be available?: "))
            e = {a: b}
            f = {a: c}
            g = {a: d}
            # add into dictionary
            d1.update(e)
            d2.update(f)
            d3.update(g)
            for key in e:
                print(f"The book '{key}' by {e[key]} is now added to the library.")
        elif x == "change":
            print("Please enter 'A' for Author, 'D' for Date, and 'N' for number of books.")
            q = str(input("What would you like to change? "))
            if q == "B":
                c = str(input("Please specify the name of the book you want to change the title: "))
                # to check if input is in dictionary
                d1[c] = d1[c]
                d = str(input("Please specify the new title of the book: "))
                d1[d] = d1.pop(c)
                d2[d] = d2.pop(c)
                d3[d] = d3.pop(c)
                print(f"The name of the book '{c}' has been changed to '{d}'.")
            elif q == "A":
                c = str(input("Please specify the Book you want to change the author: "))
                # to check if input is in dictionary
                d1[c] = d1[c]
                # change the value of the specific key
                d1[c] = str(input("Book author: "))
                print("{} author is {}".format(c, d1[c]))
            elif q == "D":
                c = str(input("Please specify the Book you want to change the date: "))
                # to check if input is in dictionary
                d2[c] = d2[c]
                # change the value of the specific key
                d2[c] = str(input("New time: "))
                print("The book '{}' publishing date is changed to {}.".format(c, d2[c]))
            elif q == "N":
                c = str(input("Please specify the Book you want to change the quantity of available books: "))
                # to check if input is in dictionary
                d3[c] = d3[c]
                # change the value of the specific key
                d3[c] = int(input("Number of books: "))
                print("The book '{}' now has {} books available.".format(c, d3[c]))
            else:
                print("Book not found. Please try again!")
        elif x == "borrow":
            e = str(input("Input the book you want to borrow: "))
            d3[e] = d3[e]
            if d3[e] > 0:
                d3[e] -= 1
                print(f"The book '{e}' is borrowed at this library on {Datenow}.")
            else:
                print(f"No more remaining {e} available.")
        elif x == "return":
            e = str(input("Please specify the book you want to return: "))
            d3[e] = d3[e]
            d3[e] += 1
            print(f"The book '{e}' has just been returned to this library on {Datenow}.")
        elif x == "delete":
            print("Delete a book")
            d = str(input("Input the book you want to delete: "))
            # to check if input is in dictionary
            d1[d] = d1[d]
            # delete a key:value pair
            d1.pop(d)
            d2.pop(d)
            d3.pop(d)
            print("The book '{}' is deleted from the library.".format(d))
        elif x == "quit":
            print("Thank You!")
            # close the program
            exit()
        else:
            print("Please select the following course of action.")


while True:
    try:
        main()
    except KeyError:
        print("Book currently not available. Please try again!")
