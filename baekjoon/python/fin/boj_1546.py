N = int(input())
M = list(map(int, input().split()))
M_max = max(M)

for i in range(N) :
  M[i] = M[i] / M_max * 100

print(sum(M)/len(M))