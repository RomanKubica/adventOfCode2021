import collections

numbers = []
bingos = []

count=0
with open('04-01.source', 'r') as f:
    numbers = f.read().splitlines()

selectedNumbers = str(numbers.pop(0)).split(',')
index = 0
for number in selectedNumbers:
    selectedNumbers[index] = int(number)
    index += 1

print(selectedNumbers)

for line in numbers:
    bingoLine = []
    if (line != ""):

        number = int(line[0:2])
        bingoLine.append(number)
        number = int(line[3:5])
        bingoLine.append(number)
        number = int(line[6:8])
        bingoLine.append(number)
        number = int(line[9:11])
        bingoLine.append(number)
        number = int(line[12:14])
        bingoLine.append(number)
        bingos.append(bingoLine)


def startBingo(selectedNumbers, bingos):
    for num in selectedNumbers:
        for i, bingoLine in enumerate(bingos):
            for j, bingoNumber in enumerate(bingoLine):
                print("location: " + str(i) + ":"+str(j) + " number there: " + str(bingoLine[j]))
                if bingoNumber == num:
                    bingoLine[j] = 'x'
                    win = checkForBingo(i,j)
                    if win == True:
                        return sumRemaining(i,j,num)


        print(bingoLine)

        # count += 1
        # if (count > 10):
        #     break

def checkForBingo(row,column):
    # check row
    noRow = True
    noColumn = True
    for item in bingos[row]:
        if item != 'x':
            noRow = False

    if noRow == True:
        return True

    # check column
    rowSelection = row % 5 # 0 1 2 3 4,    5 6 7 8 9,   10 11 12 13 14 - 
    for x in range(0,rowSelection+1):
        if bingos[row-x][column] != 'x':
            noColumn = False

    for x in range(0,5-rowSelection):
        if bingos[row+x-rowSelection][column] != 'x':
            noColumn = False

    return noRow or noColumn


def sumRemaining(row,column, finalNumber):
    print(finalNumber)
    total = 0
    rowSelection = row % 5 # 0 1 2 3 4,    5 6 7 8 9,   10 11 12 13 14 - 

    print(bingos[row])
    if rowSelection > 0:
        for x in range(0,rowSelection+1):
            for item in bingos[row-x]:
                if item != 'x':
                    total += item

    for x in range(0,5-rowSelection):
        for item in bingos[row+x]:
            if item != 'x':
                total += item

    return finalNumber * total



total = startBingo(selectedNumbers, bingos)
print(total)

# gamma = ""
# epsilon = "" 

# print("total amount:"+str(len(numbers)))
# sortedTotals = collections.OrderedDict(sorted(totals.items()))
# print(sortedTotals)
# for k,v in sortedTotals.items():
#     if (v > sizeHalf):
#         gamma += "1"
#         epsilon += "0"
#     else:
#         gamma += "0"
#         epsilon += "1"

# print("gamma: " + str(gamma))
# print("epsilon: " + str(epsilon))

# print(int(gamma,2))
# print(int(epsilon,2))
# print(int(gamma,2)*int(epsilon,2))
