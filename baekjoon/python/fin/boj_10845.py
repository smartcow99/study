from sys import stdin

N = int(stdin.readline())

que = []

for _ in range(N) :
  commend = list(map(str, stdin.readline().split()))
  if commend[0] == "push" :
    que.append(int(commend[1]))
  elif commend[0] == "front" :
    if len(que) == 0 :
      print(-1)
    else :
      print(que[0])
  elif commend[0] == "back" :
    if len(que) == 0 :
      print(-1)
    else :
      print(que[-1])
  elif commend[0] == "size" :
    print(len(que))
  elif commend[0] == "empty" :
    if len(que) == 0 :
      print(1)
    else :
      print(0)
  elif commend[0] == "pop" :
    if len(que) == 0 :
      print(-1)
    else :
      print(que.pop(0))