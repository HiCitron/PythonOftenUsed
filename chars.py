# -*- coding: utf-8 -*-

def IsNumber(s):
    for i in range(len(s)):
        k = ord(s[i])
        if not(k >= 48 and k <= 57 ):
            return False
    return True

def IsUpper(s):
    for i in range(len(s)):
        k = ord(s[i])
        if not(k >= 65 and k <= 90 ):
            return False
    return True

def IsLower(s):
    for i in range(len(s)):
        k = ord(s[i])
        if not(k >= 97 and k <= 122 ):
            return False
    return True

def IsLetter(s):
    for i in range(len(s)):
        k = ord(s[i])
        if not(k >= 65 and k <= 90 ) and not(k >= 97 and k <= 122):
            return False
    return True

def IsAlphanum(s):
    for i in range(len(s)):
        k = ord(s[i])
        if not(k >= 65 and k <= 90 ) and not(k >= 97 and k <= 122) and not(k >= 48 and k <= 57 ):
            return False
    return True

def IsSpecial(s):
    for i in range(len(s)):
        k = ord(s[i])
        if not( not(k >= 65 and k <= 90 ) and not(k >= 97 and k <= 122) and not(k >= 48 and k <= 57 ) ):
            return False
    return True

def StringIs(s):
    t = []
    for i in range(len(s)):
        k = ord(s[i])
        if (k >= 48 and k <= 57 ):
            t += [0]
        elif (k >= 65 and k <= 90 ):
            t += [1]
        elif (k >= 97 and k <= 122 ):
            t += [2]
        else:
            t += [3]
    return t
