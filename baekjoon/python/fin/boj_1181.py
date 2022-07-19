N = int(input())

dic = []
for _ in range(N) :
  dic.append(input())
dic = list(set(dic))
dic.sort(key=lambda x : (len(x), x))

for i in dic :
  print(i)