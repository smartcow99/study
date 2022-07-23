# 이진탐색 예제

import sys

N, K = map(int, sys.stdin.readline().split())
lensun_list = []

for _ in range(N) :
  lensun_list.append(int(sys.stdin.readline()))

lensun_len = 0
lensun_count = 0
result = 0

start, end = 1, max(lensun_list)
while start <= end :
  mid = (start + end) // 2
  lensun = 0
  
  for i in lensun_list :
    lensun += i // mid
    lensun_len = mid
  
  if lensun >= K :
    start = mid+1
    result = max(result, mid)
  else :
    end = mid - 1
    
print(result)
