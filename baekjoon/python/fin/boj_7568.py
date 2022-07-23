N = int(input())

people = []
score = [1 for _ in range(N)]

for i in range(N) :
  tmp = list(map(int, input().split()))
  people.append(tmp)

for x in range(N) :
  for y in range(N) :
    if people[x][0] < people[y][0] and people[x][1] < people[y][1] :
      score[x] += 1
  if N - 1 == x :
    print(score[x])
  else :
    print(score[x],end=" ")