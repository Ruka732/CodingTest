# 흙길 보수하기

import sys

input = sys.stdin.readline

n, l = map(int, input().split())

puddles = [list(map(int ,input().split())) for _ in range(n)]
puddles.sort()

cnt = 0
ptr = -1

for puddle in puddles:
  
  if ptr >= puddle[0]:
    puddle[0] = ptr + 1
  
  diff = puddle[1] - puddle[0]
  if diff % l == 0:
    cnt += diff // l
    ptr = puddle[1] - 1
  
  else:
    cnt += diff // l + 1
    rest = l - (diff % l)
    ptr = (puddle[1] - 1) + rest

print(cnt)