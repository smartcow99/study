while True :
  check = True
  str = input()
  if str == '.' :
    break
  stack = []
  for i in str :
    if i == '(' or i == '[' :
      stack.append(i)
    elif i == ')' or i == ']' :
      if len(stack) == 0 :
        check = False
        break
      else :
        if i == ')' :
          if stack[-1] != '(' :
            check = False
            break
          else :
            stack.pop()
        if i == ']' :
          if stack[-1] != '[' :
            check = False
            break
          else :
            stack.pop()
    else :
      continue
  stack.clear()
  if check :
    print("yes")
  else :
    print("no")