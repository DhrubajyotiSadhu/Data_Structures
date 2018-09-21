array=[2, 5, 3, 5, 4, 4, 2, 3]
x=3
y=4
index_x=-1
index_y=-1
distanceVariable=-1
for i in range(0,len(array)):
    if array[i]==x and index_x<i:
        index_x=i
    if array[i]==y and index_y < i:
        index_y=i
    if index_y !=-1 and index_x !=-1:
        distanceVariable=abs(index_x - index_y)

print distanceVariable



