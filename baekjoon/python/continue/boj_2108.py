from sys import stdin
import numpy

N = int(stdin.readline())

num = []
for _ in range(N) :
  num.append(int(stdin.readline()))
num.sort()
print(numpy.mean())
print(num[N//2])

