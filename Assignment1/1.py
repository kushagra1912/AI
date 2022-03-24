import math

x = int(input())
n = int(input())

sum = 0

for i in range(0, n +1):
    sum += (x**n)/math.factorial(n)

print(sum)