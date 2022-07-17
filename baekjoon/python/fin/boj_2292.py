N = int(input())

check = True
for i in range(N) :
  stri = str(i)
  sum = i
  for j in range(len(stri)) :
    sum += int(stri[j])
  if N == sum :
    check = False
    print(i)
    break
if check :
  print(0)