# cat.py
from sys import argv


def cat(f):

    file = open(f, "r")
    toprint = file.read()
    file.close()
    return toprint


def main():
    file_to_read = argv[1]
    cat(file_to_read)

if __name__ == '__main__':
    main()
