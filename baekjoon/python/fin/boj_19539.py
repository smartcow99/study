N = int(input())
tree = list(map(int, input().split()))

count = 0

if(sum(tree)%3==0) :
  for i in tree :
    count += i // 2
  
  if count >= (sum(tree) / 3) :
    print("YES")
  else :
    print("NO")

else :
  print("NO")
