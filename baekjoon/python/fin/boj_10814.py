N = int(input())

user = []
for i in range(N) :
  tmp = []
  age, name = map(str, input().split())
  tmp.append(int(age))
  tmp.append(name)
  tmp.append(i)
  user.append(tmp)

user.sort(key=lambda x : (x[0], x[2]))

for i in range(N) :
  print(user[i][0], user[i][1])