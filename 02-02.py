direction = []
with open('02-01.source') as f:
    direction = f.readlines()

depth = 0
forward = 0
aim = 0
increasedTimes = 0
count = 0
size = len(direction)
for line in direction:
    arr = line.split(' ')
    print(line.replace("\n", ""))
    number = int(arr[1].replace("\n", ""))
    if (arr[0] == 'forward'):
        forward += number
        depth += int(number * aim)
    elif (arr[0] == 'down'):
        # depth += number
        aim += number
    else:
        # depth -= number
        aim -= number

    # count+=1
    # if (count > 10):
    #     break

    print("depth: " + str(depth))
    print("forward: " +str(forward))
    print("aim: " +str(aim)+"\n")

print("total:"+ str(depth*forward))
