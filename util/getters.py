from flask import Flask
import sqlite3

DB_FILE = "data/database.db"

def get_saves(user):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command ="SELECT * FROM saves WHERE user = ?"
    args = user
    all_saves = c.execute(command,args).fetchall()
    db.close()
    return all_saves

def get_achievements(user):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "SELECT * FROM achievements WHERE user = ?"
    args = user
    all_achievements = c.execute(command,args).fetchall()
    db.close()
    return all_achievements
