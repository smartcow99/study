import math

w, h = map(int ,input().split())

result = 0
for i in range(1, w) :
  result += math.floor(h * i / w)
print(result*2)