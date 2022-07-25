from sys import stdin

result = ""

# N Cards list input and sort
N = int(stdin.readline())
N_Cards = sorted(map(int, stdin.readline().split()))

# M Cards list input
M = int(stdin.readline())
M_Cards = map(int, stdin.readline().split())

# binary search use for
def binary(arr, target, start, end) :
  if start > end :
    return 0
  
  mid = (start + end) // 2
  if target == arr[mid] :
    return count.get(target)
  elif target < arr[mid] :
    return binary(arr, target, start, mid-1)
  else :
    return binary(arr, target, mid+1, end)

count = {}
for card in N_Cards :
  if card in count:
    count[card] += 1
  else :
    count[card] = 1

for target in M_Cards :
  print(binary(N_Cards, target, 0, N-1), end=" ")