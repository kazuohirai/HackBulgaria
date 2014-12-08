import sqlite3


database = sqlite3.connect("cinema.db")
cursor = database.cursor()
cursor.execute("PRAGMA FOREIGN_KEY = ON")
database.commit()
cursor.execute("""CREATE TABLE IF NOT EXISTS reservations (id INTEGER PRIMARY KEY, name TEXT,
    projection_id INTEGER REFERENCES projections(id), row INTEGER, col INTEGER)""")
database.commit()

name1 = "RadoRado"
proj_id1 = 1
row1 = 2
col1 = 1

name2 = "RadoRado"
proj_id2 = 1
row2 = 3
col2 = 5

name3 = "RadoRado"
proj_id3 = 1
row3 = 7
col3 = 8

name4 = "Ivo"
proj_id4 = 3
row4 = 1
col4 = 1

name5 = "Ivo"
proj_id5 = 3
row5 = 2
col5 = 3

name6 = "Mysterious"
proj_id6 = 5
row6 = 2
col6 = 3

name7 = "Mysterious"
proj_id7 = 5
row7 = 2
col7 = 4

reservations = [(name1, proj_id1, row1, col1),
                (name2, proj_id2, row2, col2),
                (name3, proj_id3, row3, col3),
                (name4, proj_id4, row4, col4),
                (name5, proj_id5, row5, col5),
                (name6, proj_id6, row1, col6),
                (name7, proj_id7, row7, col7)]
cursor.executemany("INSERT INTO reservations(name, projection_id, row, col) VALUES (?,?,?,?)",
                   reservations)
database.commit()
