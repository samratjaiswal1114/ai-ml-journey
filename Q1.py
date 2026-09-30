from collections import namedtuple

n = int(input())

for i in range(n):
    ID = int(input())
    MARKS = int(input())
    CLASS = int(input())
    NAME = input()
    average = namedtuple('average', ['MARKS'])
    average.MARKS = MARKS


Average1 = MARKS/n
print(Average1)