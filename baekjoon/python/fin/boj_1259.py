while True :
  origin = list(map(int, input()))
  if origin[0] == 0 :
    break
  
  copy = list(reversed(origin))
  
  if origin == copy :
    print("yes")
  else :
    print("no")