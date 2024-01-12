# 골드바흐의 추측

import sys

input = sys.stdin.readline

n = int(input())

for i in range(n):
  a = int(input())
  arr = []
  
  for p in range(2, a):
    for q in range(2, p+1):
      if p % q == 0:
        if p == q:
          arr.append(p)
        break
  
  for i in arr:
    for j in arr:
      if i + j == a:
        print(i, j)