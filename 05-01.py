import collections

numbers = []
points = [ [ 0 for y in range( 1000 ) ] for x in range( 1000 ) ]

count=0
with open('05-01.source', 'r') as f:
    numbers = f.read().splitlines()


# 1,2 -> 1,5
for line in numbers:
    coordinates = line.split(" -> ")
    A = coordinates[0].split(",")
    B = coordinates[1].split(",")
    A[0] = int(A[0])
    A[1] = int(A[1])
    B[0] = int(B[0])
    B[1] = int(B[1])
    
    if A[0] == B[0]:
        if (A[1] > B[1]):
            C = A[1]
            A[1] = B[1]
            B[1] = C

        points[A[0]][A[1]]+=1
        points[B[0]][B[1]]+=1
        for x in range(A[1],B[1]):

            if points[A[0]][x] == None:
                points[A[0]][x] = 1
            else:
                points[A[0]][x] += 1
            print(points[A[0]][x])

        
        #x line equals
    elif A[1] == B[1]:
        #y line equals
        if (A[0] > B[0]):
            C = A[0]
            A[0] = B[0]
            B[0] = C

        points[A[0]][A[1]]+=1
        points[B[0]][B[1]]+=1
        for x in range(A[0],B[0]):
            if points[x][A[1]] == None:
                points[x][A[1]] = 1
            else:
                points[x][A[1]] += 1
            print(points[x][A[1]])
        
    else:
        #skip
        continue

    # print(points)
    
    # count += 1
    # if (count > 50):
    #     break

count = 0
total = 0
# print(points)
for x in points:
    for j in range(0,1000):
        if x[j] != None and int(x[j]) > 1:
            # print(x[j])
            total += 1

# print(points)
# total = 0
# for i in range(0,1000):
#     for j in range(0,1000):
#         print(points[i,j])
#         if points[i,j] != None and int(points[i,j]) > 1:
#             total += 1

print(total)