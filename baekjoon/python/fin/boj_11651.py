N = int(input())
xy = []
for i in range(N) :
  xy.append(list(map(int, input().split())))

xy.sort(key=lambda x : (x[1], x[0]))

for i in range(N) :
  print(xy[i][0], xy[i][1])