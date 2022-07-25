from sys import stdin
from collections import deque
N = int(stdin.readline())

deque = deque([])

for _ in range(N) :
  commend = list(map(str, stdin.readline().split()))
  if commend[0] == "push_front" :
    deque.appendleft(int(commend[1]))
  elif commend[0] == "push_back" :
    deque.append(int(commend[1]))
  elif commend[0] == "front" :
    if len(deque) == 0 :
      print(-1)
    else :
      print(deque[0])
  elif commend[0] == "back" :
    if len(deque) == 0 :
      print(-1)
    else :
      print(deque[-1])
  elif commend[0] == "size" :
    print(len(deque))
  elif commend[0] == "empty" :
    if len(deque) == 0 :
      print(1)
    else :
      print(0)
  elif commend[0] == "pop_front" :
    if len(deque) == 0 :
      print(-1)
    else :
      print(deque.popleft())
  elif commend[0] == "pop_back" :
    if len(deque) == 0 :
      print(-1)
    else :
      print(deque.pop())