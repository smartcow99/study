N = int(input())

sum = 1
if N == 1 :
  print(1)
else :
  for i in range(1,N) :
    sum += i*6
    if N <= sum :
      print(i+1)
      break