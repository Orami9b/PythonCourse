import psycopg2

def create_table():
   connection = psycopg2.connect(
      dbname = 'database1',
      user = 'postgres',
      password = 'PostPass92',
      host = 'localhost',
      port = '5432')
   cursor = connection.cursor()
   cursor.execute("CREATE TABLE IF NOT EXISTS store(item TEXT, quantity INTEGER, price REAL)")
   cursor.execute("INSERT INTO store VALUES('Wine Glass', 8, 10.50)")
   connection.commit()
   connection.close()

def insert(item, quantity, price):
   connection = psycopg2.connect(
      dbname = 'database1',
      user = 'postgres',
      password = 'PostPass92',
      host = 'localhost',
      port = '5432')
   cursor = connection.cursor()
   cursor.execute("INSERT INTO store VALUES(%s, %s, %s)", (item, quantity, price))
   connection.commit()
   connection.close()

def update(quantity, price, item):
   connection = psycopg2.connect(
      dbname = 'database1',
      user = 'postgres',
      password = 'PostPass92',
      host = 'localhost',
      port = '5432')
   cursor = connection.cursor()
   cursor.execute("UPDATE store SET quantity = %s, price = %s WHERE item = %s",
      (quantity, price, item))
   connection.commit()
   connection.close()

def delete(item):
   connection = psycopg2.connect(
      dbname = 'database1',
      user = 'postgres',
      password = 'PostPass92',
      host = 'localhost',
      port = '5432')
   cursor = connection.cursor()
   cursor.execute("DELETE FROM store WHERE item = %s", (item,))
   connection.commit()
   connection.close()

def view():
   connection = psycopg2.connect(
      dbname = 'database1',
      user = 'postgres',
      password = 'PostPass92',
      host = 'localhost',
      port = '5432')
   cursor = connection.cursor()
   cursor.execute("SELECT * FROM store")
   rows = cursor.fetchall()
   connection.commit()
   connection.close()

   return rows

update(2, 5, "Apple")
print(view())