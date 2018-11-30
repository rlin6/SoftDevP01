import sqlite3

DB_FILE = "data/database.db"

db = sqlite3.connect(DB_FILE)
c = db.cursor()

command = "CREATE TABLE IF NOT EXISTS accts(userid INTEGER PRIMARY KEY AUTOINCREMENT, user TEXT, password TEXT)"
c.execute(command)

command = "CREATE TABLE IF NOT EXISTS saves(saveid INTEGER PRIMARY KEY AUTOINCREMENT, userid INTEGER, times TEXT, type TEXT)"
c.execute(command)

command = "CREATE TABLE IF NOT EXISTS places(saveid INTEGER, lat FLOAT, long FLOAT, address TEXT)"
c.execute(command)

command = "CREATE TABLE IF NOT EXISTS weather(saveid INTEGER, summary TEXT, high FLOAT, low FLOAT, alerts TEXT)"
c.execute(command)

command = "CREATE TABLE IF NOT EXISTS attract(saveid INTEGER, attraction TEXT)"
c.execute(command)

command = "CREATE TABLE IF NOT EXISTS achievements(saveid INTEGER, accomplishment TEXT)"
c.execute(command)

db.commit()
db.close()
