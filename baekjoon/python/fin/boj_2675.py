T = int(input())

for i in range(T) :
  result = []
  S, R = map(str, input().split())
  for j in R :
    result.append(j*int(S))
  print("".join(result))