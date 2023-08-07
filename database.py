import sqlite3

connection = sqlite3.connect('data.db', check_same_thread=False)
cursor = connection.cursor()



