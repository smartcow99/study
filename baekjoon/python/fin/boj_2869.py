A, B, V = map(int, input().split())

V -= A
result = V // (A-B)
dif = V % (A-B)
if dif > 0 :
  print(result+2)
else :
  print(result+1)