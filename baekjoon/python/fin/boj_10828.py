from sys import stdin

N = int(stdin.readline())

stk = []

for _ in range(N) :
  commend = list(map(str, stdin.readline().split()))
  if commend[0] == "push" :
    stk.append(int(commend[1]))
  elif commend[0] == "top" :
    if len(stk) == 0 :
      print(-1)
    else :
      print(stk[-1])
  elif commend[0] == "size" :
    print(len(stk))
  elif commend[0] == "empty" :
    if len(stk) == 0 :
      print(1)
    else :
      print(0)
  elif commend[0] == "pop" :
    if len(stk) == 0 :
      print(-1)
    else :
      print(stk.pop())