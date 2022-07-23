N, M = map(int, input().split())

origin = []
result = []

for _ in range(N) :
  origin.append(input())

for x in range(N-7) :
  for y in range(M-7) :
    index_x = 0
    index_y = 0
    for i in range(x, x+8) :
      for j in range(y, y+8) :
        if (i+j) % 2 == 0 :
          if origin[i][j] != 'W' : index_x += 1
          if origin[i][j] != 'B' : index_y += 1
        else : 
          if origin[i][j] != 'B' : index_x += 1
          if origin[i][j] != 'W' : index_y += 1
    result.append(index_x)
    result.append(index_y)

print(min(result))