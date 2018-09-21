#inp = [1, 2, 0, 0, 0, 3, 6]
#out = [1, 2, 3, 6, 0, 0, 0]

def shifting(l):
    i = 0
    j = len(l) - 1
    while i < j:

        while l[i] != 0:
            i += 1

        while l[j] == 0:
            j -= 1

        temp = l[i]
        l[i] = l[j]
        l[j] = temp

        i += 1
        j -= 1

    return l

print shifting([1, 2, 0, 0, 0, 3, 6])
