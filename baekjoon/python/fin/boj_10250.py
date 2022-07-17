T = int(input())

for i in range(T) :
  H, W, N = map(int, input().split())
  if N % H == 0 :
    tmp_h = H
    tmp_w = N // H
  else :
    tmp_h = N % H
    tmp_w = N // H + 1

  result = tmp_h * 100 + tmp_w
  print(result)
