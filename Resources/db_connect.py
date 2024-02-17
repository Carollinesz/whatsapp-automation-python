import sqlite3 

def connection():
    conn = sqlite3.connect('Assets\db.sqlite3')
    cursor = conn.cursor()
    return cursor, conn