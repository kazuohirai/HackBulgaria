import sqlite3
import helper


database = sqlite3.connect("cinema.db")
database.row_factory = sqlite3.Row
cursor = database.cursor()


def show_movies():
    result = cursor.execute("SELECT id, name FROM movies ORDER BY rating")
    for row in result:
        print ("{} - {}".format(row["id"], row["name"]))


def show_movie_projections(movie_id, date):
    if len(date) != 0:
        result = cursor.execute("""SELECT * FROM projections INNER JOIN movies
                                   ON projections.movie_id = movies.id
                                   WHERE movie_id = ? AND pdate = ? ORDER BY ?""",
                                (movie_id, date, date))
        for row in result:
            print ("{}|{} at {}".format(row["id"], row["name"], row["time"]))
    else:
        result = cursor.execute("""SELECT * FROM projections INNER JOIN movies
                                   ON projections.movie_id = movies.id
                                   WHERE movie_id = ?""", (movie_id,))
        for row in result:
            print ("{}|{} on {} at {}".format(row["id"], row["name"], row["pdate"], row["time"]))


def print_matrix(matrix):
    first_row = " "
    for col in range(0, len(matrix)):
        first_row += " " + str(col)
    print (first_row)
    next_line = ""
    row_count = 0
    for row in matrix:
        next_line += str(row_count) + " "
        row_count += 1
        for col in row:
            next_line += col + " "
        print (next_line)
        next_line = ""


def make_reservation():
    show_movies()
    movie_id = input("Enter id of movie: ")
    show_movie_projections(movie_id, "")
    chosen_movie = input("Please choose projection: ")
    result = cursor.execute("""SELECT row, col
        FROM projections INNER JOIN reservations
        ON projections.id = reservations.projection_id
        WHERE projections.id = ?""", (chosen_movie,))
    taken_spots = 0
    taken_seats = []
    hall = helper.theater

    for row in result:
        taken_spots += 1
        taken_seats.append((row["row"], row["col"]))
    print(taken_seats)
    for item in taken_seats:
        hall[item[0]][item[1]] = "X"
    print ("There are {} free spots available.".format(helper.max_free_spots - taken_spots))
    print_matrix(hall)
    username = input("Enter username: ")
    tickets = int(input("Enter number of tickets: "))
    while tickets > helper.max_free_spots - taken_spots:
        tickets = int(input("Not enough free spaces. Enter less number of tickets: "))
    seats = []
    while tickets > 0:
        spot = (input("Choose seat: "))
        spot = spot.split(",")
        spot = [int(s) for s in spot]
        if (spot[0] > helper.max_cinema_rows or spot[1] > helper.max_cinema_cols):
            print("Out of bounds.")
        elif hall[int(spot[0])][int(spot[1])] == "X":
            print ("Seat is taken.")
        else:
            seats.append(spot)
            tickets -= 1
    tickets = []
    for item in seats:
        ticket = []
        ticket.append(str(username))
        ticket.append(int(chosen_movie))
        ticket.append(item[0])
        ticket.append(item[1])
        tickets.append(ticket)

    cursor.executemany("""INSERT INTO reservations(name, projection_id, row, col)
        VALUES (?,?,?,?)""", tickets)
    database.commit()


def cancel_reservation(name):
    result = cursor.execute("""SELECT reservations.id as id,
        movies.name as mname, projections.time as time, projections.pdate as pdate,
        reservations.row as row, reservations.col as col FROM reservations
        INNER JOIN projections ON reservations.projection_id = projections.id
        INNER JOIN movies ON projections.movie_id = movies.id
        WHERE reservations.name = ?""", (name,))

    for row in result:
        print ("{}|{} - {}, {} ({},{})"
               .format(row["id"], row["mname"], row["pdate"],
                       row["time"], row["row"], row["col"]))
    to_delete = int(input("Enter id of reservation you wish to discard: "))
    cursor.execute("DELETE FROM reservations WHERE id=?", (to_delete,))
    database.commit()


def main():
    exit = False
    while exit is False:
        command = input("--> ").split(" ")
        if command[0] == "show_movies":
            show_movies()
        elif command[0] == "show_movie_projections":
            if len(command) == 3:
                show_movie_projections(command[1], command[2])
            else:
                show_movie_projections(command[1], "")
        elif command[0] == "make_reservation":
            make_reservation()
        elif command[0] == "cancel_reservation":
            cancel_reservation(command[1])
        elif command[0] == "exit":
            exit = True
        elif command[0] == "help":
            print (helper.tech_support)
        else:
            print ("Invalid command. Enter 'help' for further assistance.")

if __name__ == "__main__":
    main()
