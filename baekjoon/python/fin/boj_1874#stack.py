import sys

N = int(sys.stdin.readline())

stack = []
result = []
count = 0
check = False

for i in range(N) :
  x = int(input())
  
  while count < x :
    count += 1
    stack.append(count)
    result.append('+')
  
  if stack[-1] == x :
    stack.pop()
    result.append('-')
  else :
    check = True


if check :
  print("NO")
else :
  print("\n".join(result))