N = int(input())

star = [' ' for _ in range(N)]

for i in reversed(range(N)) :
  star[i] = '*'
  print(''.join(star))