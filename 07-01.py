import collections


def calculateFuelDiff(steps):
    fuel =0
    addition = 0
    for x in range(0,steps):
        fuel = fuel + 1 + addition
        addition += 1

    return fuel


crabs = []

count=0
with open('07.source', 'r') as f:
    crabs = f.read().split(",")

# crabs = [16,1,2,0,4,2,7,1,2,14]

index = 0
for number in crabs:
    crabs[index] = int(number)
    index += 1


totalFuel = []

startGuess = round(sum(crabs) / len(crabs))

while startGuess > 2:
    fuel = 0

    for number in crabs:
        print(number)
        fuel += calculateFuelDiff(abs(number - startGuess))

    totalFuel.append(fuel)
    startGuess -= 1

print("startGuess " + str(startGuess) + " "+ str(totalFuel))

print(min(totalFuel))

