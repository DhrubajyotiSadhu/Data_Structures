
def find_longest_spanning():

    arr1 = [0, 1, 0, 1, 1, 1, 1]
    arr2 = [1, 1, 1, 1, 1, 0, 1]

    i = 0
    j = 0
    maxLen = 0
    len = 0
    for i in range(0, arr1.__len__()):
        sum1 = 0
        sum2 = 0

        for j in range(i, arr2.__len__()):
            sum1 = arr1[j]
            sum2 = arr2[j]

        if sum1 == sum2:
            len = j - i

            if len > maxLen:
                maxLen = len

    return maxLen

print find_longest_spanning()