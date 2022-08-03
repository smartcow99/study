from sys import stdin

n = int(stdin.readline())

tiles = [0,1,2]

def func(j):
  tiles.append(tiles[j-1] + tiles[j-2])

for i in range(3, n+1) :
  func(i)

print(tiles[n]%10007)