from flask import Flask
import sqlite3

DB_FILE = "data/database.db"

def get_places(user):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command ="SELECT * FROM places WHERE user = ?"
    args = user
    c.execute(command,args)
    db.close()

def get_weathers(user):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "SELECT * FROM weather WHERE user = ?"
    args = user
    c.execute(command,user)
    db.close()

def add_attraction(user,times,attraction):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "SELECT * FROM attract WHERE user = ?"
    args = user
    c.execute(command,args)
    db.close()

def add_achievement(user,accomplishment):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "SELECT * FROM achievements WHERE user = ?"
    args = user
    c.execute(command,args)
    db.close()
