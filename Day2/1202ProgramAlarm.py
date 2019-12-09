import csv
import operator

try:
    fp = open('input.txt')
    reader = csv.reader(fp)
    inputList = reduce(operator.concat, list(reader))

    for i in range(len(inputList)):
        if i % 4 == 0:
            if inputList[i] == '99':
                print(inputList)
                exit(1)
        elif inputList[i] == '1':
            inputList[int(inputList[i + 3])] = int(inputList[int(inputList[i + 1])]) + int(inputList[int(inputList[i + 2])])
        elif inputList[i] == '2':
            inputList[int(inputList[i + 3])] = int(inputList[int(inputList[i + 1])]) * int(inputList[int(inputList[i + 2])])

finally:
    fp.close()
