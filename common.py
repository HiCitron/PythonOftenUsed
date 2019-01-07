# -*- coding: utf-8 -*-

# Returns all element in both l1 and l2, with/without duplicates
def Common( l1, l2, rep = True ):
    if len(l2) > len(l1):
        l1, l2 = l2, l1
    com = []
    for i in range(len(l2)):
        if l2[i] in l1:
            com.append( l2[i] )
    if rep == False:
        com = list(set(com))
    return com

def LargestSublist( l1, l2 ):

    if len(l2) > len(l1):
        l1, l2 = l2, l1
    maxi = 0
    res = False
    for i in range(len(w2)):
        s = ""
        k = i
        while s in w1 and k != len(w2):
            s += w2[k]
            k += 1
        if len(s)-1 > maxi:
            maxi = len(s)-1
            res = s[:-1]
        if i > len(w2) - maxi:
            break
    return res


def LargestSubstring( w1, w2 ):
    if len(w2) > len(w1):
        w1, w2 = w2, w1
    maxi = 0
    res = False
    for i in range(len(w2)):
        s = ""
        k = i
        while s in w1 and k != len(w2):
            s += w2[k]
            k += 1
        if len(s)-1 > maxi:
            maxi = len(s)-1
            res = s[:-1]
        if i > len(w2) - maxi:
            break
    return res
