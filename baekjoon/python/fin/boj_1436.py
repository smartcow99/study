N = int(input())

cnt = 0
sixsixsix = 666

while True :
  if '666' in str(sixsixsix) :
    cnt += 1
  if cnt == N :
    print(sixsixsix)
    break
  sixsixsix += 1