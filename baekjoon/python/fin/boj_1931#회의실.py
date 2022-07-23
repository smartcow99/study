N = int(input())

schedule = []
count = 1

for i in range(N) :
  start, end = tuple(map(int, input().split()))
  schedule.append((start, end))

schedule.sort(key=lambda x:(x[1],x[0]))

endTime = schedule[0][1]

for i in range(1,N) :
  if (schedule[i][0] >= endTime) :
    count += 1
    endTime = schedule[i][1]

print(count)
