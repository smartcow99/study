N = int(input())
people = list(map(int, input().split()))

people.sort()

result = 0

for i in range(N) :
  sum = 0
  for j in range(i+1) :
    sum += people[j]
  result += sum

print(result)