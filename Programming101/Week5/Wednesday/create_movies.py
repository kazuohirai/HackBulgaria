import sqlite3


database = sqlite3.connect("cinema.db")
cursor = database.cursor()
cursor.execute("PRAGMA FOREIGN_KEY = ON")
database.commit()
cursor.execute("CREATE TABLE IF NOT EXISTS movies (id INTEGER PRIMARY KEY, name TEXT, rating REAL)")
database.commit()

name1 = "The Hunger Games"
rating1 = 7.9
name2 = "Wreck-It Ralph"
rating2 = 7.8
name3 = "Her"
rating3 = 8.3

movies = [(name1, rating1),
          (name2, rating2),
          (name3, rating3)]
cursor.executemany("INSERT INTO movies(name, rating) VALUES (?,?)", movies)
database.commit()
