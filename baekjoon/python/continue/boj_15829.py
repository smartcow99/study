L = int(input())
alp = list(map(str, input()))

alphabet = 'abcdefghijklmnopqrstuvwxyz'

for i in range(L) :
  alp[i] = alphabet.find(alp[i]) + 1

tmp = 0
for i in range(L) :
  tmp += int(alp[i]) * (31**i)

print(tmp%1234567891)