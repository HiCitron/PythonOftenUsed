# -*- coding: utf-8 -*-

# binary in string format of an integer
# Binary( 8 ) = '1000'
def Binary(n):
    return bin(n)[2:]

# hex in string format of an integer
# Hexa( 255 ) = 'FF'
def Hexa(n):
    return hex(n)[2:]

# dec of a binary in string format
# Bin2Dec( '1000' ) = 8
def Bin2Dec(n):
    return int(n,2)

# dec of a hex in string format
# Hex2Dec( "FF" ) = 255
def Hex2Dec(n):
    return int(n,16)

# True if binary, False if not
def IsBin(n):
    n = str(n)
    for i in range(len(n)):
        if n[i] != '0' and n[i] != '1':
            return False
    return True

# True if hexa, False if not
def IsHex(n):
    n = str(n)
    for i in range(len(n)):
        k = ord(n[i])
        if not(ord(n[i]) >= 48 and ord(n[i]) <= 57) and not(ord(n[i]) >= 65 and ord(n[i]) <= 70) and not(ord(n[i]) >= 97 and ord(n[i]) <= 102):
            return False
    return True

# True if dec, False if not
def IsDec(n):
    n = str(n)
    for i in range(len(n)):
        k = ord(n[i])
        if ord(n[i]) < 48 or ord(n[i]) > 57:
            return False
    return True

# xor of two integers
def xor(n1, n2):
    return n1^n2
