import sqlite3


database = sqlite3.connect("cinema.db")
cursor = database.cursor()
cursor.execute("PRAGMA FOREIGN_KEY = ON")
database.commit()
cursor.execute("""CREATE TABLE IF NOT EXISTS projections (id INTEGER PRIMARY KEY,
    movie_id INTEGER REFERENCES movies(id), type TEXT, pdate TEXT, time TEXT)""")
database.commit()

movie_id1 = 1
type1 = "3D"
date1 = "2014-04-01"
time1 = "19:10"
movie_id2 = 1
type2 = "2D"
date2 = "2014-04-01"
time2 = "19:00"
movie_id3 = 1
type3 = "4DX"
date3 = "2014-04-02"
time3 = "21:00"
movie_id4 = 3
type4 = "2D"
date4 = "2014-04-05"
time4 = "20:20"
movie_id5 = 2
type5 = "3D"
date5 = "2014-04-02"
time5 = "22:00"
movie_id6 = 2
type6 = "2D"
date6 = "2014-04-02"
time6 = "19:30"

projections = [(movie_id1, type1, date1, time1),
               (movie_id2, type2, date2, time2),
               (movie_id3, type3, date3, time3),
               (movie_id4, type4, date4, time4),
               (movie_id5, type5, date5, time5),
               (movie_id6, type6, date6, time6)]
cursor.executemany("INSERT INTO projections(movie_id, type, pdate, time) VALUES (?,?,?,?)",
                   projections)
database.commit()
