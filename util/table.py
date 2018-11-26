import sqlite3

DB_FILE = "database.db"



db = sqlite3.connect(DB_FILE)
c = db.cursor()

command = "CREATE TABLE IF NOT EXISTS accts(id INT PRIMARY KEY, user TEXT, password TEXT);"
c.execute(command)

command = "CREATE TABLE IF NOT EXISTS places(user TEXT, times TEXT, lat TEXT, long TEXT, address TEXT);"
c.execute(command)

command = "CREATE TABLE IF NOT EXISTS weather(user TEXT, times TEXT, summary TEXT, high FLOAT, low FLOAT, alerts TEXT);"
c.execute(command)

command = "CREATE TABLE IF NOT EXISTS attract(user TEXT, times TEXT, attraction TEXT);"
c.execute(command)

command = "CREATE TABLE IF NOT EXISTS achievements(user TEXT, accomplishment TEXT);"
c.execute(command)

db.commit()
db.close()

def register(user, pwd, conf):
    if pwd != conf:
        return "Passwords don't match"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    for i in c.execute("SELECT user FROM accts WHERE username =?",(user,)):
        db.close()
        return "Username already exists"
    args = (user,password)
    command = "INSERT INTO accts VALUES(?,?)"
    c.execute(command, args)
    db.commit()
    db.close()
    return "Account creation successful"

def login(user, pwd):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    for i in c.execute("SELECT user,password FROM accts WHERE username =?",(user,)):
        if pwd == password:
            db.close()
            return "Login successful"
    db.close()
    return "Login failed"
