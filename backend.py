import sqlite3

def connect():
    #creates database
    conn = sqlite3.connect('books.db')
    #creates a cursor object to scroll through table
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
    conn.commit()
    conn.close()

def insert(title, author, year, isbn):
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)", (title,author,year,isbn))
    conn.commit()
    conn.close()

#fetch all rows of the database's table
def view():
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(title="",author="",year="",isbn=""):
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title,author,year,isbn))
    rows =cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?", (id,))
    conn.commit()
    conn.close()


def update(id,title,author,year,isbn):
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute("UPDATE book SET title=?,author=?,year=?,isbn=? WHERE id=?", (title,author,year,isbn,id))
    conn.commit()
    conn.close()

connect()
#insert('The Sun', 'John Smith', 1918, 913123132)
#print(view())
#delete(3)
#update(2, 'The moon', 'John Smooth',1917,999999)
#print(search(author="John Smith"))
#print(search(author="John Smith"))
