import collections

numbers = []

count=0
with open('06-01.source', 'r') as f:
    numbers = f.read().split(",")

numbers = [3,4,3,1,2]

index = 0
for number in numbers:
    numbers[index] = int(number)
    index += 1

# print(numbers)

totalNumber = 0

testNumbers = []
for x in range(1,9):
    testNumbers = [x]
    days = 0
    while days < 80:
        newFish = []
        index = 0

        for line in testNumbers:
            if line == 0 :
                newFish.append(6)
                newFish.append(8)
            else:
                newFish.append(line - 1)
        days += 1
        testNumbers = []
        testNumbers = newFish
        print("day " + str(days) + " "+ str(len(testNumbers)))
    
    totalNumber += (numbers.count(x) * len(testNumbers))
    print("x:" +str(x))
    print(numbers.count(x))
print(totalNumber)


