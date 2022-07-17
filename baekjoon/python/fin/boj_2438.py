N = int(input())
star = ['*']
for i in range(N) :
  star.append(star[i]+'*')
  print(star[i])
