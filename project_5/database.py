import sqlite3

def connect():
   connect = sqlite3.connect("books.db")
   cursor = connect.cursor()
   cursor.execute(
      """--sql
      CREATE TABLE IF NOT EXISTS books(
         id     INTEGER PRIMARY KEY,
         title  TEXT,
         author TEXT,
         year   INTEGER,
         isbn   TEXT,
         UNIQUE(title, isbn));""")
   connect.commit()
   connect.close()

def insert(title, author, year, isbn):
   connect = sqlite3.connect("books.db")
   cursor = connect.cursor()
   cursor.execute(
      """--sql
      INSERT OR IGNORE INTO books
      VALUES (NULL, ?, ?, ?, ?);""", (title, author, year, isbn))
   connect.commit()
   connect.close()

def view():
   connect = sqlite3.connect("books.db")
   cursor = connect.cursor()
   cursor.execute(
      """--sql
      SELECT *
        FROM books;""")
   rows = cursor.fetchall()
   connect.close()

   return rows

def search(title = "", author = "", year = "", isbn = ""):
   connect = sqlite3.connect("books.db")
   cursor = connect.cursor()
   cursor.execute(
      """--sql
      SELECT *
        FROM books 
       WHERE title = ?
          OR author = ?
          OR year = ?
          OR isbn = ?;""",
      (title, author, year, isbn))
   rows = cursor.fetchall()
   connect.close()

   return rows

def delete(id):
   connect = sqlite3.connect("books.db")
   cursor = connect.cursor()
   cursor.execute(
      """--sql
      DELETE FROM books
       WHERE id = ?;""",
      (id, ))
   connect.commit()
   connect.close()

def update(id, title, author, year, isbn):
   connect = sqlite3.connect("books.db")
   cursor = connect.cursor()
   cursor.execute(
      """--sql
      UPDATE books
         SET title = ?,
             author = ?,
             year = ?, 
             isbn = ?
       WHERE id = ?;""",
      (title, author, year, isbn, id))
   connect.commit()
   connect.close()

connect()