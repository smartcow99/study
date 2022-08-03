from sys import stdin

T = int(stdin.readline())
for _ in range(T) :
  A, B = map(int, stdin.readline().split())
  print(A+B)