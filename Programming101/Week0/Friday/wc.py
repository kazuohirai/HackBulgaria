from sys import argv


def count(inputs):
    command = inputs[0]
    f = inputs[1]
    count = 0
    textfile = open(f, "r")

    if command == "chars":
        for char in textfile.read():
            count += 1
        textfile.close()
        return count

    if command == "words":
        for word in textfile.read().split():
            count += 1
        textfile.close()
        return count

    if command == "lines":
        for line in textfile.read().split("\n"):
            count += 1
        textfile.close()
        return count


def main():
    inputs = []
    for i in range(1, len(argv)):
        inputs.append(argv[i])

    print count(inputs)

if __name__ == '__main__':
    main()
