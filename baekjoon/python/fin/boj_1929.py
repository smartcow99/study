from sys import stdin

M, N = map(int, stdin.readline().split())

def prime(n) :
  check = [True] * (n+1)
  
  m = int(n ** 0.5)
  for i in range(2, m+1) :
    if check[i] == True :
      for j in range(i+i, n+1, i) :
        check[j] =False
  
  return [i for i in range(2, n+1) if check[i] == True]

result = prime(N)
for i in result :
  if i < M :
    continue
  else :
    print(i)
