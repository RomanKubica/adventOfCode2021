direction = []
with open('02-01.source') as f:
    direction = f.readlines()

depth = 0
forward = 0
increasedTimes = 0
count = 0
size = len(direction)
for line in direction:
    arr = line.split(' ')
    if (arr[0] == 'forward'):
        forward += int(arr[1].replace("\n", ""))
    elif (arr[0] == 'down'):
        depth += int(arr[1].replace("\n", ""))
    else:
        depth -= int(arr[1].replace("\n", ""))

    # count+=1
    # if (count > 10):
    #     break

print("depth: " + str(depth))
print("forward: " +str(forward))

