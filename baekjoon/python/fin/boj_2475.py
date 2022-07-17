N = list(map(int, input().split()))

for i in range(len(N)) :
  N[i] = N[i] * N[i]

print(sum(N)%10)