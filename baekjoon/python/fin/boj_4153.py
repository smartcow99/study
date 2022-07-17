while True :
  a, b, c = map(int, input().split())
  if a == 0 and b == 0 and c == 0 :
    break
  else :
    tri = [a, b, c]
    tri.sort()
    if(tri[0] ** 2 + tri[1] ** 2 == tri[2] ** 2) :
      print("right")
    else :
      print("wrong")