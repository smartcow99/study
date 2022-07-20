left, right = map(int, input().split())

check = 0
result = 0

for i in range(left, right+1) :
  for j in range(1, i+1) :
    if i % j == 0 :
      check += 1
  if check % 2 == 0 :
    result += i
    check = 0
  else :
    result -= i
    check = 0

print(result)
