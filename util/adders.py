from flask import Flask
import sqlite3

DB_FILE = "data/database.db"

def add_save(user,times,lat,long,address,summary,high,low,alerts,attraction):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command ="INSERT INTO saves (user,times,lat,long,address,summary,high,low,alerts,attraction) VALUES (?,?,?,?,?,?,?,?,?,?)"
    args = (user,times,lat,long,address,summary,high,low,alerts,attraction)
    c.execute(command,args)
    db.commit()
    db.close()

def add_achievement(user,accomplishment):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "INSERT INTO achievements (user,accomplishment) VALUES (?,?)"
    args = (user,accomplishment)
    c.execute(command,args)
    db.commit()
    db.close()
