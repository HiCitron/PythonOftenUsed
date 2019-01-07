# -*- coding: utf-8 -*-

# Can you add element of l to obtain t

# find solution existence, without rep
# returns true or false
# ex: dynExist( [1,2,3], 5 ) = True
def dynExist(l, t, b=False):
    if b:
        return b
    else:
        i = 0
        while l[i] < t:
            b = dynExist(l[:i] + l[i + 1:], t - l[i], b)
            if i == len(l) - 1:
                break
            else:
                i += 1
        if l[i] == t:
            b = True
        return b


# find the smallest solution, without repetition
# return the solution found, false otherwise
# ex: dynSmallest( [1,2,3,4,5,6], 10 ) = [4, 6]
def dynSmallest(l, t, s=[], sm=False):
    i = 0
    while l[i] < t:
        sm = dynSmallest(l[:i] + l[i + 1:], t - l[i], s + [l[i]], sm)
        if i == len(l) - 1:
            break
        else:
            i += 1
    if l[i] == t:
        if not sm:
            sm = s[:] + [l[i]]
        elif len(s) + 1 < len(sm):
            sm = s[:] + [l[i]]
    return sm


print(dynExist([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 35))
