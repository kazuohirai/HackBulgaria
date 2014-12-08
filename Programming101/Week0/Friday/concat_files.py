from sys import argv


def concatFiles(IOfiles):
    outputFile = argv[-1]
    output = open(outputFile, "a")

    for i in range(0, len(IOfiles) - 1):
        inputFile = IOfiles[i]
        Input = open(inputFile, "r+")
        toWrite = Input.read().split("\n")
        output.write("\n".join(toWrite))
        output.write("\n")
        Input.close()
    output.close


def main():
    files = []
    for i in range(1, len(argv)):
        files.append(argv[i])
    concatFiles(files)

if __name__ == '__main__':
    main()
