N = int(input())

result = int(N/5)
N = N%5

if(N == 4) :
  result -= 1
  N += 5
elif(N == 1) :
  result -= 1
  N += 5
elif(N%5 == 2) :
  result -= 2
  N += 10
if(result == -1) :
  print(-1)
else :
  print(result + int(N/3))