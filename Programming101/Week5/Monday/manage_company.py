import sqlite3

NUMBER_OF_MONTHS = 12
database = sqlite3.connect("company.db")
database.row_factory = sqlite3.Row
cursor = database.cursor()


def list_all():
    result = cursor.execute("SELECT name, position FROM users")
    for row in result:
        print ("{} - {}".format(row["name"], row["position"]))


def total_month_expense():
    result = cursor.execute("SELECT sum(monthly_salary) FROM users")
    sum_monthy_salary = result.fetchone()
    return(sum_monthy_salary[0])


def total_year_expense():
    year_bonus = cursor.execute("SELECT sum(yearly_bonus) FROM users")
    month_expense = total_month_expense()
    return month_expense * NUMBER_OF_MONTHS + year_bonus


def input_data():
    name = input("Employee Name: ")
    salary = input("Monthly Salary: ")
    bonus = input("Yearly Bonus: ")
    position = input("Position: ")
    return (name, salary, bonus, position)


def add_employee():
    new_info = input_data()
    cursor.execute("""INSERT INTO users(name, monthly_salary, yearly_bonus, position)
        VALUES (?,?,?,?)""", (new_info[0], new_info[1], new_info[2], new_info[3]))
    database.commit()


def delete_employee(id):
    cursor.execute("""DELETE FROM users WHERE id = ?""", (id,))
    database.commit()


def update_employee(id):
    update_info = input_data()
    cursor.execute("""UPDATE users SET name = ?, monthly_salary = ?,
        yearly_bonus = ?, position = ? WHERE id = ?""",
                   (update_info[0], update_info[1], update_info[2], update_info[3], id))
    database.commit()


def main():
    exit = False
    while exit is False:
        command = input("Enter command:").split(" ")
        if command[0] == "list_employees":
            list_all()
        elif command[0] == "monthly_spending":
            print(total_month_expense())
        elif command[0] == "yearly_spending":
            print(total_year_expense())
        elif command[0] == "add_employee":
            add_employee()
        elif command[0] == "delete_employee":
            delete_employee(command[1])
        elif command[0] == "update_employee":
            update_employee(command[1])
        elif command[0] == "exit":
            exit = True
        else:
            print("Error! Invalid command!!!")


if __name__ == "__main__":
    main()
