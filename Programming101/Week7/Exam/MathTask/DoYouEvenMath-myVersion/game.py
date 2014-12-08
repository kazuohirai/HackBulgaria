from random import randint

from sqlalchemy.orm import Session
from sqlalchemy import create_engine, update

from create_questions import Question
from create_scores import Score
from create_base import Base

MAX_CORRECT_ANSWERS = 15


def add_questions(session):
    print("Adding questions to the database.....")
    session.add_all([
        Question(question="Which is the Ludolphian number?", correct_answer="Pi"),
        Question(question="Which is the Napier's constant?", correct_answer="e"),
        Question(question="Which is the imaginary unit?", correct_answer="i"),
        Question(question="Which is the Khinchin's constant?", correct_answer="K"),
        Question(question="Which is the Landau's constant?", correct_answer="L"),
        Question(question="Which is the Gauss-Kuzmin-Wirsing constant?", correct_answer="Lambda"),
        Question(question="Which is the Fransen-Robinson constant?", correct_answer="F"),
        Question(question="Which is the Pythagoras' constant?", correct_answer="Square root of 2"),
        Question(question="Which is the Theodorus' constant?", correct_answer="Square root of 3"),
        Question(question="Which greek letter marks the Golden Ratio?", correct_answer="Phi"),
        Question(question="Which is the plastic number?", correct_answer="Rho"),
        Question(question="Which is the Ramanujan-Soldner constant?", correct_answer="Mu"),
        Question(question="Which is the Reciprocal Fibonacci constant?", correct_answer="Psi"),
        Question(question="Which is shorter for 10 to the power of 100?", correct_answer="googol"),
        Question(question="Which is the Euler-Mascheroni constant?", correct_answer="Gamma")])


def get_questions(session):
    result = session.query(Question.question).all()
    working = []
    for question in result:
        working.append(question[0])
    return working


def get_correct_answer(session, asked):
    result = session.query(Question.correct_answer).filter(Question.question == asked).one()
    return result[0]


def calculate_score(correct_answers):
    return correct_answers * correct_answers


def add_score_to_table(session, username, score):
    result = session.query(Score.handle).all()
    nicknames = []
    for handle in result:
        nicknames.append(handle[0])
    if username not in nicknames:
        session.add(Score(handle=username, highest_score=score))
        session.commit()
    else:
        session.execute(update(Score).where(Score.handle == username).values(highest_score=score))
        session.commit()


def play(session):
    username = input("Enter your username: ")
    unasked_questions = get_questions(session)
    correct_answers = 0

    while len(unasked_questions) > 0:

        rand_question = unasked_questions[randint(0, len(unasked_questions)-1)]
        unasked_questions.remove(rand_question)
        correct = get_correct_answer(session, rand_question)
        answer = input(rand_question+" >")
        if answer == correct:
            correct_answers += 1
            print ("Correct!")
            if correct_answers == MAX_CORRECT_ANSWERS:
                add_score_to_table(session, username, calculate_score(correct_answers))
                print ("Achievement unlocked: 'FULL SCORE!!!'")
                break
        else:
            add_score_to_table(session, username, calculate_score(correct_answers))
            print("Incorrect! Game Over. Too bad, so sad... LOSER!!!")
            break


def scores(session):
    result = session.query(Score).order_by(Score.highest_score.desc()).order_by(Score.handle).all()
    return result[:10]


def main():
    engine = create_engine("sqlite:///math.db")
    Base.metadata.create_all(engine)
    session = Session(bind=engine)
    add_questions(session)
    session.commit()

    exit = False
    while exit is False:
        command = input("Enter command: ").split(" ")
        if command[0] == "play":
            play(session)
        elif command[0] == "scores":
            top10 = scores(session)
            for item in top10:
                print(item)
        elif command == "exit":
            exit = True
        else:
            print ("Invalid command.")


if __name__ == "__main__":
    main()
