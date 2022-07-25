'''
블록 제거 2초
블록 놓기 1초
'''
from sys import stdin

N, M, B = map(int, stdin.readline().split())

land = []
for i in range(N) :
  land.append(list(map(int, stdin.readline().split())))

high = max(land)
low = min(land)

print(high, low)