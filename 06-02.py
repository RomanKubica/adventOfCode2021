import collections

numbers = []

count=0
with open('06-01.source', 'r') as f:
    numbers = f.read().split(",")

# numbers = [3,4,3,1,2]
result = [0] * 9

index = 0
for number in numbers:
    numbers[index] = int(number)
    index += 1

for index, num in enumerate(result):
    result[index] = numbers.count(index)

# print(numbers)

totalNumber = 0

testNumbers = []
days = 0
while days < 256:

    adding = [0] * 9
    for index, number in enumerate(result):
        if index == 0 :
            adding[6] +=  result[index]
            adding[8] += result[index]
            result[index] = 0
        else:
            adding[index-1] +=  result[index]
            result[index] = 0

        index += 1

    days += 1
    for i in range(len(result)):
        result[i] += adding[i]

    print("day " + str(days) + " "+ str(sum(result)))
    
print(sum(result))


