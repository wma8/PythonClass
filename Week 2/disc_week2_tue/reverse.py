def reverse(l):
    for i in range(len(l) / 2):
        l[i], l[-i-1] = l[-i-1], l[i]