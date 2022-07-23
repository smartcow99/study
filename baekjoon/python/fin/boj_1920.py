import sys


N = int(sys.stdin.readline())
N_list = list(map(int, sys.stdin.readline().split()))
N_list.sort()

M = int(sys.stdin.readline())
M_list = list(map(int, sys.stdin.readline().split()))

for i in M_list :
  start, end = 0, len(N_list)-1
  check = False
  if N_list[start] == i or N_list[end] == i :
    check = True
  if N_list[start] < i and N_list[end] > i :
    while start - end != -1 :
      if N_list[start] > i or N_list[end] < i :
        break
      mid = (start + end) // 2
      if N_list[mid] == i :
        check = True
        break
      elif N_list[mid] > i :
        end = mid
      else :
        start = mid
  if check :
    print(1)
  else :
    print(0)