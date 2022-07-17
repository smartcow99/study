N = int(input())

for i in range(N) :
  sum = 0
  t_Case = list(map(str, input().split('X')))
  for k in t_Case :
    for j in range(1,len(k)+1) :
      sum += j
  print(sum)