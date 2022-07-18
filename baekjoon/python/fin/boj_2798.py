from itertools import combinations

N, M = map(int, input().split())

cards = list(map(int, input().split()))

result = 0

for i in combinations(cards, 3) :
  tmp = sum(i)
  if result < tmp <= M :
    result = tmp

print(result)