depth = []
with open('01-01.source') as f:
    depth = f.readlines()

increasedTimes = 0
count = 0
size = len(depth)
for number in depth:
    if (count > 0 and count < size - 2):
        a = int(depth[count-1]) + int(number) + int(depth[count+1])
        b = int(number) + int(depth[count+1]) + int(depth[count+2])
        print(a)
        print(b)
        if (a < b):
            increasedTimes +=1

    count += 1

print(increasedTimes)