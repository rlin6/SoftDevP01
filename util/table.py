import sqlite3

DB_FILE = "data/database.db"

db = sqlite3.connect(DB_FILE)
c = db.cursor()

command = "CREATE TABLE IF NOT EXISTS accts(id INTEGER PRIMARY KEY, user TEXT, password TEXT);"
c.execute(command)

command = "CREATE TABLE IF NOT EXISTS places(user TEXT, time TEXT, lat FLOAT, long FLOAT, address TEXT);"
c.execute(command)

command = "CREATE TABLE IF NOT EXISTS weather(user TEXT, time TEXT, summary TEXT, high FLOAT, low FLOAT, alerts TEXT);"
c.execute(command)

command = "CREATE TABLE IF NOT EXISTS attract(user TEXT, times TEXT, attraction TEXT);"
c.execute(command)

command = "CREATE TABLE IF NOT EXISTS achievements(user TEXT, accomplishment TEXT);"
c.execute(command)

db.commit()
db.close()
