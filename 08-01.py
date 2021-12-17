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
    for number in numbers:
        print(number)
        size = len(number)
        if size == 2 or size == 3:
            total += 1
        elif size == 4 or size ==7:
            total += 1



print(total)

# while startGuess > 2:
#     fuel = 0

#     for number in crabs:
#         print(number)
#         fuel += calculateFuelDiff(abs(number - startGuess))

#     totalFuel.append(fuel)
#     startGuess -= 1

