# Problem 1
# Re arrange the array such that arr[i] = i else -1

def array_arrange():
    arr = [-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]
    for i in range(0, len(arr)):
            if arr[i] != -1:
                temp = arr[i]
                temp1 = arr[temp]
                if temp1 != -1:
                    arr[temp] = temp
                    arr[temp1] = temp1
                else:
                    arr[temp] = temp
                    arr[i] = -1

    print arr

array_arrange()

# Output
# [-1, 1, 2, 3, 4, -1, 6, -1, -1, 9]