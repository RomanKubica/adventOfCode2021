import collections

lines = []

count=0
with open('08.sources', 'r') as f:
    lines = f.read().splitlines()

# be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
total = 0

for line in lines:
    parts = line.split(" | ")
    numbers = parts[1].split(" ")
    print(numbers)

    code = findA(line.replace(" | ", " "))

    digits = ""
    for number in numbers:
        size = len(number)
        if size == 2:
            digits += 1
        elif size == 3:
            digits += 7
        elif size == 4:
            digits += 4
        elif size == 7:
            digits += 8
        else:
            digits += decodeDigit(number, code)

def findA(line):
    numbers = line.split(" ")

    one = ""
    seven = ""

    for number in numbers:
        size = len(number)
        if size == 2:
            one = number
        elif size == 3:
            seven = number

    a = removeChars(seven,one)

    return a

def removeChars(string1,removeString):
    for rem in removeString:
        string1.replace(rem,"")

    return string1


print(total)

# while startGuess > 2:
#     fuel = 0

#     for number in crabs:
#         print(number)
#         fuel += calculateFuelDiff(abs(number - startGuess))

#     totalFuel.append(fuel)
#     startGuess -= 1

