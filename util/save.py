from flask import Flask
import sqlite3

DB_FILE = "data/database.db"

def add_place(user,times,lat,long,address):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command ="INSERT INTO places (user,times,lat,long,address) VALUES (?,?,?,?,?)"
    args = (user,times,lat,long,address)
    c.execute(command,args)
    db.commit()
    db.close()

def add_weather(user,times,summary,high,low,alerts):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "INSERT INTO weather (user,times,summary,high,low,address) VALUES (?,?,?,?,?,?)"
    args = (user,times,summary,high,low,address)
    c.execute(command,args)
    db.commit()
    db.close()

def add_attraction(user,times,attraction):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "INSERT INTO attract (user,times,attraction) VALUES (?,?,?)"
    args = (user,times,attraction)
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
