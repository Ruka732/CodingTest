# 점프 점프
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
jump = list(map(int, input().split()))
inf = 1e10
dp = [inf for _ in range(1001)]
dp[0] = 0

for idx in range(n):
  for distance in range(1, jump[idx] + 1):
    if idx + distance < n:
      dp[idx + distance] = min(dp[idx] + 1, dp[idx + distance])

if dp[n-1] == inf:
  print(-1)
else:
  print(dp[n-1])