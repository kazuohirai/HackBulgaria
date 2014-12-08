from sqlalchemy.orm import Session
from sqlalchemy import delete

from create_movie import Movie
from create_projections import Projection
from create_reservations import Reservation

import create_base
import cinema_help


def add_movies(session):
    print ("Adding new movie to the database via the session object...")
    session.add_all([
        Movie(name="The Hunger Games", rating=7.9),
        Movie(name="Wreck-It Ralph", rating=7.8),
        Movie(name="Her", rating=8.3)])


def add_projections(session):
    print ("Adding new projection to the database via the session object...")
    session.add_all([
        Projection(movie_id=1, movie_type="3D", time="19:10", date="2014-04-01"),
        Projection(movie_id=1, movie_type="2D", time="19:00", date="2014-04-01"),
        Projection(movie_id=1, movie_type="4DX", time="21:00", date="2014-04-02"),
        Projection(movie_id=3, movie_type="2D", time="20:20", date="2014-04-05"),
        Projection(movie_id=2, movie_type="3D", time="22:00", date="2014-04-02"),
        Projection(movie_id=2, movie_type="2D", time="19:00", date="2014-04-02")])


def add_reservations(session):
    print ("Adding new reservation to the database via the session object...")
    session.add_all([
        Reservation(username="RadoRado", projection_id=1, row=2, col=1),
        Reservation(username="RadoRado", projection_id=1, row=3, col=5),
        Reservation(username="RadoRado", projection_id=1, row=7, col=8),
        Reservation(username="Ivo", projection_id=3, row=1, col=1),
        Reservation(username="Ivo", projection_id=3, row=1, col=2),
        Reservation(username="Mysterious", projection_id=5, row=2, col=3),
        Reservation(username="Mysterious", projection_id=5, row=2, col=4)])


def print_items_from_query(query_array):
    for item in query_array:
        print(item)


def show_movies(session):
    all_movies = session.query(Movie).order_by(Movie.rating.desc()).all()
    return all_movies


def show_projections(session, id, date):
    if len(date) != 0:
        projections = session.query(Projection).filter(Movie.id == id).\
            filter(Projection.date == date).order_by(Projection.date).all()
    else:
        projections = session.query(Projection).filter(Movie.id == id).\
            filter(Movie.id == Projection.movie_id).all()
    return projections


def make_reservation(session):
    print_items_from_query(show_movies(session))
    movie_id = input("Enter id of movie: ")
    print_items_from_query(show_projections(session, movie_id, ""))
    chosen_movie = input("Please choose projection: ")
    result = session.query(Reservation.row, Reservation.col).\
        filter(Projection.id == Reservation.projection_id).filter(Projection.id == chosen_movie)
    taken_spots = 0
    taken_seats = []
    hall = cinema_help.theater

    for row in result:
        taken_spots += 1
        taken_seats.append((row[0], row[1]))
    print(taken_seats)
    for item in taken_seats:
        hall[item[0]][item[1]] = "X"
    print ("There are {} free spots available.".format(cinema_help.max_free_spots - taken_spots))
    cinema_help.print_matrix(hall)

    username = input("Enter username: ")
    tickets = int(input("Enter number of tickets: "))
    while tickets > cinema_help.max_free_spots - taken_spots:
        tickets = int(input("Not enough free spaces. Enter less number of tickets: "))
    seats = []
    while tickets > 0:
        spot = (input("Choose seat: "))
        spot = spot.split(",")
        spot = [int(s) for s in spot]
        if (spot[0] > cinema_help.max_cinema_rows or spot[1] > cinema_help.max_cinema_cols):
            print("Out of bounds.")
        elif hall[int(spot[0])][int(spot[1])] == "X":
            print ("Seat is taken.")
        else:
            seats.append(spot)
            tickets -= 1
    for item in seats:
        ticket = []
        ticket.append(str(username))
        ticket.append(int(chosen_movie))
        ticket.append(spot[0])
        ticket.append(spot[1])
        res = Reservation(username=str(username), projection_id=int(chosen_movie),
                          row=spot[0], col=spot[1])
        session.add(res)
        session.commit()


def cancel_reservation(session, name):
    res = session.query(Reservation.id, Reservation.username, Movie.name, Projection.date,
                        Projection.time, Reservation.row, Reservation.col).\
        filter(Reservation.username == name,
               Projection.id == Reservation.projection_id,
               Movie.id == Projection.movie_id)
    if len(list(res)) == 0:
        return "No reservations for that name."

    print_items_from_query(res)
    to_delete = int(input("Enter ID of reservation to discard: "))
    deletion = session.query(Reservation).filter(Reservation.id == to_delete).all()
    for res in deletion:
        session.delete(res)
    session.commit()


def main():
    create_base.Base.metadata.create_all(create_base.engine)
    session = Session(bind=create_base.engine)
    # add_movies(session)
    # add_projections(session)
    # add_reservations(session)
    session.commit()

    exit = False
    while exit is False:
        command = input(">>> ").split()
        if command[0] == "show-movies":
            movies = show_movies(session)
            print_items_from_query(movies)
        elif command[0] == "show-projections":
            if len(command) == 3:
                projections = show_projections(session, command[1], command[2])
                print_items_from_query(projections)
            else:
                projections = show_projections(session, command[1], "")
                print_items_from_query(projections)
        elif command[0] == "make-reservation":
            make_reservation(session)
        elif command[0] == "cancel-reservation":
            print(cancel_reservation(session, command[1]))
        elif command[0] == "help":
            print(cinema_help.helper)
        elif command[0] == "exit":
            exit = True
        else:
            print("Invalid command. Enter 'help' for further assistance.")

if __name__ == "__main__":
    main()
