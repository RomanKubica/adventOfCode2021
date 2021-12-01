depth = []
with open('01-01.source') as f:
    depth = f.readlines()

increasedTimes = 0
count = 0
for number in depth:
    if (count > 0):
        if (depth[count-1] < number):
            # print(depth[count-1] + " " + number)
            increasedTimes +=1

    count += 1

print(increasedTimes)