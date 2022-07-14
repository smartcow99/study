import re
from unittest import result


N, K = map(int, input().split())
A_list = []

for i in range(N):
  A_list.append(int(input()))

A_list.reverse()
result = int(0)

for i in range(N):
  if(A_list[i] <= K) :
    result += int(K / A_list[i])
    K = K - int(K/A_list[i]) * A_list[i]

print(result)