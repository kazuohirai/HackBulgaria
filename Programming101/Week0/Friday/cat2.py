# cat2.py
from sys import argv


def cat2(files):
    fileread = ""
    for item in files:
        file = open(item, "r")
        fileread += file.read()
        file.close()
    return fileread


def main():
    files = []
    for i in range(1, len(argv)):
        files.append(argv[i])

    cat2(files)

if __name__ == '__main__':
    main()
