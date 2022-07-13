N = int(input())

n_list = [input() for _ in range(N)]

for i in range(N) :
  for j in range(len(n_list[i])) :
    print(ord(n_list[i][j]))

K = int(input())
