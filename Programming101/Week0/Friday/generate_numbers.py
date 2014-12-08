# generate_numbers.py
from sys import argv
from random import randint


def main():
    f = argv[1]
    n = argv[2]
    file = open(f, "w")
    for i in range(0, int(n)):
        toWrite = randint(1, 1000)
        if i == int(n) - 1:
            toWrite = str(toWrite) + ""
        else:
            toWrite = str(toWrite) + " "
        file.write(toWrite)
    file.close()

if __name__ == '__main__':
    main()
