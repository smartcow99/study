from sys import stdin

input = stdin.readline

A, B = map(int, input().split())
C = int(input())

h = C // 60
m = C - h*60

A += h
B += m

if B >= 60 :
  B -= 60
  A += 1

if A >= 24 :
  A = A % 24

print(A, B)