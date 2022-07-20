nums = list(map(int, input().split()))

cho = len(nums) // 2

nums = list(set(nums))

if len(nums) > cho :
  print(cho)
else :
  print(len(nums))