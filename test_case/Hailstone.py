# coding=utf-8

# 冰雹序列

def hailstone( n ):
    length = 1
    while 1 < n:
        if n % 2:
            n = n * 3 + 1
        else: 
            n = n / 2
        length = length + 1
        print n
    return length

hailstone( 27 )
