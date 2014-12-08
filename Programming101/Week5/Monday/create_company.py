import sqlite3


database = sqlite3.connect("company.db")
cursor = database.cursor()
cursor.execute("""CREATE TABLE users(id INTEGER PRIMARY KEY,
    name TEXT, monthly_salary INTEGER, yearly_bonus INTEGER, position TEXT)""")
database.commit()


name1 = "Ivan Ivanov"
monthly_salary1 = 5000
yearly_bonus1 = 10000
position1 = "Software Developer"

name2 = "Rado Rado"
monthly_salary2 = 500
yearly_bonus2 = 0
position2 = "Tech Support"

name3 = "Ivo Ivo"
monthly_salary3 = 10000
yearly_bonus3 = 100000
position3 = "CEO"

name4 = "Petar Petrov"
monthly_salary4 = 3000
yearly_bonus4 = 1000
position4 = "Marketing Manager"

name5 = "Maria Georgieva"
monthly_salary5 = 8000
yearly_bonus5 = 10000
position5 = "COO"

employees = [(name1, monthly_salary1, yearly_bonus1, position1),
             (name2, monthly_salary2, yearly_bonus2, position2),
             (name3, monthly_salary3, yearly_bonus3, position3),
             (name4, monthly_salary4, yearly_bonus4, position4),
             (name5, monthly_salary5, yearly_bonus5, position5)]
cursor.executemany(""" INSERT INTO users(name, monthly_salary, yearly_bonus, position)
    VALUES(?,?,?,?)""", employees)
database.commit()
