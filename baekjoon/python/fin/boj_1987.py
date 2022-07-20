N = int(input())
thtn = list(map(int, input().split()))

cnt = 0
for i in thtn :
  tmp = 0
  if i == 1 :
    continue
  else :
    for j in range(1, i+1) :
      if i % j == 0 :
        tmp += 1
    if tmp == 2 :
      cnt += 1

print(cnt)