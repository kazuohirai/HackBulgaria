from sys import argv


def sumIntsFromFile(intsfile):
    fsum = 0
    file = open(intsfile, "r")
    toAdd = file.read().split(" ")
    print toAdd
    for item in toAdd:
        fsum += int(item)
    file.close()
    return fsum


def main():
    f = argv[1]
    sumIntsFromFile(f)

if __name__ == '__main__':
    main()
