from sys import stdin

input = stdin.readline

N = int(input())
roads = list(map(int, input().split()))
cities = list(map(int, input().split()))

total_cost = 0
min_cost = cities[0]

for i in range(N-1) :
  if cities[i] < min_cost :
    min_cost = cities[i]
  total_cost += min_cost * roads[i]

print(total_cost)


