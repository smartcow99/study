import sys

def check(fivot):
    cnt = 0
    for i in trees:
        if i >= fivot:
            cnt += i - fivot
    return cnt >= M

N, M = map(int, input().split())
trees = list(map(int, sys.stdin.readline().split()))

start = 0
end = max(trees)

while start <= end:
    mid = (start+end)//2
    if check(mid):
        start = mid + 1
    else:
        end = mid - 1

print(end)

'''
from sys import stdin

N, M = map(int, stdin.readline().split())
trees = list(map(int, stdin.readline().split()))


start, end= 0,  max(trees)

while start <= end :
  mid = (start + end) // 2
  tree = 0
  for i in trees :
    if i > mid :
      tree += (i - mid)

  if tree >= M :
    start = mid + 1
  else :
    end = mid - 1
    
print(end)
'''