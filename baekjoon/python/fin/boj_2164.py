import sys

N = int(sys.stdin.readline())

cards = [i for i in range(1, N+1)]

if N == 1 :
  print(N)
else :
  while len(cards) > 1 :
    if len(cards) % 2 == 1 :
      cards.pop(0)
      cards.append(cards.pop(0))
    cards = cards[1::2]
  print(cards[0])