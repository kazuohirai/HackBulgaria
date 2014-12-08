from sqlalchemy.orm import Session
from sqlalchemy import create_engine, update
from create_scores import Score
from create_base import Base
from random import randint
from math import pow


def generate_number(digits):
    return randint(0, len(digits)-1)


def generate_operation(operations):
    return randint(0, len(operations)-1)


def generate_question(numbers, operations):
    number1 = numbers[generate_number(numbers)]
    number2 = numbers[generate_number(numbers)]
    operation = operations[generate_operation(operations)]
    print("What is the answer to {}{}{}?".format(number1, operation, number2))
    return [number1, operation, number2]


def add(a, b):
    return int(a+b)


def subtract(a, b):
    return int(a-b)


def multiply(a, b):
    return int(a*b)


def divide(a, b):
    return float("{:.2f}".format(a/b))


def power(a, b):
    return int(pow(a, b))


def validate_input_type(answer):
    try:
        float(answer)
        return True
    except ValueError:
        return False


def validate_input():
    answer = input("-->")
    while not validate_input_type(answer):
        answer = input("-->")
    return float(answer)


def calculate_answer(generated):
    first = generated[0]
    second = generated[2]

    if generated[1] == "+":
        answer = add(first, second)
    elif generated[1] == "-":
        answer = subtract(first, second)
    elif generated[1] == "*":
        answer = multiply(first, second)
    elif generated[1] == "/":
        answer = divide(first, second)
    elif generated[1] == "^":
        answer = power(first, second)

    return answer


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


def play_game(session, digits, operations):
    wrong_answer = False
    correct_answers = 0
    username = input("Enter username: ")
    while wrong_answer is False:
        stuff = generate_question(digits, operations)
        correct = calculate_answer(stuff)
        answer = validate_input()
        if answer == correct:
            correct_answers += 1
            print("Correct!")
        else:
            print("Incorrect! Game Over.")
            score = calculate_score(correct_answers)
            add_score_to_table(session, username, score)
            break
    return correct_answers


def get_scores(session):
    result = session.query(Score).order_by(Score.highest_score.desc()).order_by(Score.handle).all()
    return result[:10]


def scores(scores):
    for entry in scores:
        print (entry)


def main():
    engine = create_engine("sqlite:///math.db")
    Base.metadata.create_all(engine)
    session = Session(bind=engine)
    session.commit()

    actions = ["+", "-", "*", "/", "^"]
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    quit = False
    while quit is False:
        command = input("Enter command: ")
        if command == "play":
            play_game(session, numbers, actions)
        elif command == "score":
            table = get_scores(session)
            scores(table)
        elif command == "quit":
            quit = True
        else:
            print ("Invalid Command!")


if __name__ == "__main__":
    main()
