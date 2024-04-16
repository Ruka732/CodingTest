# 골드바흐의 파티션

import sys

input = sys.stdin.readline

prime = []
check = [0] * 1000001
check[0] = 1
check[1] = 1

for i in range(2, 1000001):
  if check[i] == 0:
    prime.append(i)
    for j in range(2*i, 1000001, i):
      check[j] = 1

n = int(input())

for _ in range(n):
  cnt = 0
  num = int(input())
  for i in prime:
    if i >= num:
      break
    if not check[num - i] and i <= num-i:
      cnt += 1
  print(cnt)