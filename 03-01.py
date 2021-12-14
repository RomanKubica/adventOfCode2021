import collections

numbers = []
with open('03-01.source') as f:
    numbers = f.readlines()

totals = {}
sizeHalf = len(numbers) / 2
count = 0
for line in numbers:
    print(line)
    for index, number in enumerate(line):
        if (index < 10):
            index = "0"+str(index)
        if (number == "1"):
            if "index"+str(index) in totals.keys():
                totals["index"+str(index)] = totals["index"+str(index)] + 1
            else:
                totals["index"+str(index)] = 1

    # count+=1
    # if (count > 10):
    #     break
    print(totals)

gamma = ""
epsilon = "" 

print("total amount:"+str(len(numbers)))
sortedTotals = collections.OrderedDict(sorted(totals.items()))
print(sortedTotals)
for k,v in sortedTotals.items():
    if (v > sizeHalf):
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"

print("gamma: " + str(gamma))
print("epsilon: " + str(epsilon))

print(int(gamma,2))
print(int(epsilon,2))
print(int(gamma,2)*int(epsilon,2))
