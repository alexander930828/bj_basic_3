# 1
a = int(input())

for i in range(1, 10):
    print(a, '*', i, '=', a * i)


# 2
a = int(input())

for i in range(a):
    b, c = map(int, input().split())
    print(b + c)


#3
a = int(input())

sum = 0

for i in range(a+1):
    sum = sum + i

print(sum)


#4
from sys import stdin

a = int(stdin.readline())

for i in range(a):
    b, c = map(int, stdin.readline().split())
    print(b + c)


#5
from sys import stdin

a = int(stdin.readline())

while a > 0:
    a = a - 1
    print(a+1)

#6
from sys import stdin

a = int(stdin.readline())

for i in range(a, 0, -1):
    print(i)


#7
from sys import stdin

a = int(stdin.readline())

for i in range(1, a+1):
    b, c = map(int, stdin.readline().split())
    sum = b + c
    print('Case #'+str(i)+":",sum)

#7-1
from sys import stdin

a = int(stdin.readline())

for i in range(1, a+1):
    b, c = map(int, stdin.readline().split())
    sum = b+c
    print("Case #%s: %s"%(i, sum))


#8
from sys import stdin

a = int(stdin.readline())

for i in range(1, a+1):
    b, c = map(int, stdin.readline().split())
    sum = b + c
    print('Case #%s: %s + %s = %s'%(i, b, c, sum))


#9
from sys import stdin

a = int(stdin.readline())

for i in range(1, a+1):
    print('*' * i)


#10
from sys import stdin

a = int(stdin.readline())

for i in range(1, a+1):
    print(' ' * (a-i) + '*' * i)


#11
from sys import stdin

a, b = map(int, stdin.readline().split())

c = list(map(int, stdin.readline().split()))

for i in range(a):
    if c[i] < b:
        print(c[i], end=" ")
