import math

inputNum = int(input())
for i in range(inputNum) :
  N, M = map(int, input().split())
  result = math.factorial(M)/(math.factorial(N)*math.factorial(M-N))
  print(int(result))
