import sqlite3


conn = sqlite3.connect("library.db")

cursor = conn.cursor()

cursor.execute("""INSERT INTO books
                    VALUES ('Python 101', 'Mike Driscoll', '9/10/2020',
                    'Mouse vs Python', 'epub')"""
              )

conn.commit()


books = [('Python Interviews', 'Mike Driscoll',
          '2/1/2018', 'Packt Publishing', 'softcover'),
         ('Automate the Boring Stuff with Python',
          'Al Sweigart', '', 'No Starch Press', 'PDF'),
         ('The Well-Grounded Python Developer',
          'Doug Farrell', '2020', 'Manning', 'Kindle')]
cursor.executemany("INSERT INTO books VALUES (?, ?, ?, ?, ?)", books)

conn.commit()

