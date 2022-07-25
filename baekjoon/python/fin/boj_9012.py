import sys


N = int(input())
for _ in range(N) :
  str = input()
  stack = []
  for i in str :
    if i == '(' :
      stack.append(i)
    elif i == ')' and len(stack) != 0 :
      stack.pop()
    else :
      stack.append(N)
      break
  if len(stack) == 0 :
    print("YES")
  else :
    print("NO")
    