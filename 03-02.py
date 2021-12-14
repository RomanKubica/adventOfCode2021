import collections

numbers1 = []
numbers2 = []
with open('03-01.source') as f:
    numbers1 = f.read().splitlines()

with open('03-01.source') as f:
    numbers2 = f.read().splitlines()    

# print(numbers2)
oxygenOne = []
oxygenTwo = []
coOne = []
coTwo = []

totals = 0
count = 0
safeCount = 0
index = 0
while len(numbers1) != 1:
    safeCount += 1
    # print("index:" + str(index))
    for line in numbers1:
        # print("line:" + str(line) + " - index number: " + str(line[index]))
        if (line[index] == "1"):
            oxygenOne.append(line)
            totals += 1
        else:
            oxygenTwo.append(line)

    # print("groupOne" + str(groupOne))
    # print(groupTwo)
    if len(oxygenOne) >= len(oxygenTwo):
        numbers1 = oxygenOne
    else:
        numbers1 = oxygenTwo

    oxygenOne = []
    oxygenTwo = []
    totals = 0
    index +=1
    # print(index)
    if (index > len(line)-1):
        break

print(numbers1[0])
oxygen =int(numbers1[0],2)

index=0
while len(numbers2) != 1:
    safeCount += 1
    # print("index:" + str(index))
    for line in numbers2:
        # print("line:" + str(line) + " - index number: " + str(line[index]))
        if (line[index] == "1"):
            coOne.append(line)
            totals += 1
        else:
            coTwo.append(line)

    if len(coOne) >= len(coTwo):
        numbers2 = coTwo
    else:
        numbers2 = coOne
    
    # print(numbers2)
    coOne = []
    coTwo = []
    totals = 0
    index +=1
    # print(index)
    if (index > len(line)-1):
        break

print(numbers2[0])
co2=int(numbers2[0],2)
print(co2*oxygen) 
# print(int(numbers1[0],2))
# gamma = ""
# epsilon = "" 


# print("gamma: " + str(gamma))
# print("epsilon: " + str(epsilon))

# print(int(gamma,2))
# print(int(epsilon,2))
# print(int(gamma,2)*int(epsilon,2))
