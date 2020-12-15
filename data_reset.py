import pickle
import datetime
from collections import defaultdict

Datenow = datetime.date.today().strftime("%B-%d-%Y")

d1 = {"Yakusoku no Neverland": "Kaiu Shirai", "The Little Prince": "Antoine de Saint-Exupéry", "Naruto":
      "Masashi Kishimoto", "KonoSuba": "Natsume Akatsuki", "Avengers": "Stan Lee", "Harry Potter":
      "J.K. Rowling", "Carrie": "Stephen King", "Gone with the Wind": "Margaret Mitchell",
      "Noli Me Tangere": "Dr. Jose Rizal", "El Filibusterismo": "Dr.Jose Rizal"}  # Author
d2 = {"Yakusoku no Neverland": "August 1, 2016", "The Little Prince": "April 6, 1943", "Naruto": "September 21, 1999",
      "KonoSuba": "September 9, 2014", "Avengers": "September 1963", "Harry Potter":
      "June 26, 1997 - July 21, 2007", "Carrie": "April 5,1974", "Gone with the Wind": "June 30, 1936",
      "Noli Me Tangere": "1887", "El Filibusterismo": "1891"}  # Published Date
d3 = {"Yakusoku no Neverland": 1, "The Little Prince": 10, "Naruto": 7, "KonoSuba": 1, "Avengers": 3,
      "Harry Potter": 7, "Carrie": 2, "Gone with the Wind": 3, "Noli Me Tangere": 6,
      "El Filibusterismo": 6}  # Numbers of Available Books
d4 = {"Yakusoku no Neverland": "Anime", "The Little Prince": "Children's Book", "Naruto": "Anime",
      "KonoSuba": "Anime", "Avengers": "Comics", "Harry Potter": "Fantasy Fiction", "Carrie":
      "Horror Fiction", "Gone with the Wind": "Romance", "Noli Me Tangere": "Novel", "El Filibusterismo": "Novel"}

brwuser = {"Yakusoku no Neverland": ["Ryan", "Josephine"],
                              "The Little Prince": ["Joy", "Josephine"],
                              "Naruto": ["Ryan", "Heathcliff"],
                              "KonoSuba": ["Killua", "Yukino"],
                              "Avengers":["Hikigaya", "Setsuna"],
                              "Harry Potter": ["Ryan", "Josephine"],
                              "Carrie": ["Ryan", "Josephine"],
                              "Gone with the Wind": ["Ryan", "Josephine"],
                              "Noli Me Tangere": ["Ryan", "Josephine"],
                              "El Filibusterismo": ["Ryan", "Josephine"]}

brwdate = {"Yakusoku no Neverland": ["Dec. 1, 2020", "Dec. 8, 2020"],
                              "The Little Prince": ["July 9, 2020", "June 13, 2020"],
                              "Naruto": ["August 5, 2020", "May 22, 2020"],
                              "KonoSuba": ["April 10, 2020", "February 22, 2020"],
                              "Avengers":["May 22, 2020", "May 22, 2020"],
                              "Harry Potter": ["May 22, 2020", "May 22, 2020"],
                              "Carrie": ["May 22, 2020", "May 22, 2020"],
                              "Gone with the Wind": ["May 22, 2020", "May 22, 2020"],
                              "Noli Me Tangere": ["May 22, 2020", "May 22, 2020"],
                              "El Filibusterismo": ["May 22, 2020", "May 22, 2020"]}

rtnuser = {"Yakusoku no Neverland": [],
                              "The Little Prince": [],
                              "Naruto": [],
                              "KonoSuba": [],
                              "Avengers":[],
                              "Harry Potter": [],
                              "Carrie": [],
                              "Gone with the Wind": [],
                              "Noli Me Tangere": [],
                              "El Filibusterismo": []}

rtndate = {"Yakusoku no Neverland": [],
                              "The Little Prince": [],
                              "Naruto": [],
                              "KonoSuba": [],
                              "Avengers":[],
                              "Harry Potter": [],
                              "Carrie": [],
                              "Gone with the Wind": [],
                              "Noli Me Tangere": [],
                              "El Filibusterismo": []}

def nameinput():
    return str(input("Please input the name of the borrower: "))


def bookinput():
    return str(input("Please input the book you want to borrow: "))


"""name = nameinput()
e = bookinput()
for key in dict(d1):
    if key == e:
        print(bookuser[e])
        if name in bookuser[e]:
            bookuser[e].remove(name)
            print(bookuser[e])
            print(bookuser)"""


#with open("bookXusers.dat", 'a+') as usrfile:
    #user.append(pickle.load(usrfile))


def writemode(data):
    return open(data, "wb")


print(brwuser)

pickle.dump(d1, (writemode("bookXauthor.dat")))
pickle.dump(d2, (writemode("bookXpbdate.dat")))
pickle.dump(d3, (writemode("bookXavail.dat")))
pickle.dump(d4, (writemode("bookXcustloc.dat")))
pickle.dump(brwuser, (writemode("bookXbrwusers.dat")))
pickle.dump(rtnuser, (writemode("bookXfrzusers.dat")))
pickle.dump(brwdate, (writemode("bookXbrwdate.dat")))
pickle.dump(rtndate, (writemode("bookXrtndate.dat")))





