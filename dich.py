# -*- coding: utf-8 -*-

def dich( l, t ):
    a = 0
    b = len(l) - 1
    while b - a > 1:
        m = int((a+b)/2)
        if l[m] >= t:
            b = m
        else:
            a = m
    if t > l[a] and t < l[b]:
        return [False, b]
    else:
        if l[a] == t:
            return [True, a]
        elif l[b] == t:
            return [True, b]
        elif l[a] > t:
            return [False, a]
        elif l[b] < t:
            return [False, b+1]
