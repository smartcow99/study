result = 1
for _ in range(3) :
  result = result * int(input())

for i in range(10) :
  print(list(map(int, str(result))).count(i))
