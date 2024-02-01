# 점프

import sys
from math import sqrt

input = sys.stdin.readline

n, m = map(int, input().split())

cant = [int(input()) for _ in range(m)]

max_spd = int((2*n)**0.5) + 1
dp = [[float('inf')] * (max_spd+1) for _ in range(n+1)]
# 돌번호, 속도

# cant = set(cant)

dp[1][0] = 0

for i in range(2, n+1):
  if i in cant:
    continue
  for j in range(1, max_spd):
    dp[i][j] = min(dp[i-j][j-1], dp[i-j][j], dp[i-j][j+1]) + 1

ans = min(dp[n])

if ans == float('inf'):
  print(-1)
else:
  print(ans)