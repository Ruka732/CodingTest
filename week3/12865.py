# 평범한 배낭

import sys

input = sys.stdin.readline

n, k = map(int, input().split())

w = []
v = []

for _ in range(n):
  weight, value = map(int, input().split())
  w.append(weight)
  v.append(value)

dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

for i in range(1, n+1): # 물건들에 대해서
  for j in range(1, k+1): # 무게만큼
    if w[i-1] <= j:
      # dp[i][j] += v[i]
      dp[i][j] = max(dp[i-1][j-w[i-1]] + v[i-1], dp[i-1][j])
    else:
      dp[i][j] = dp[i-1][j]

print(dp[n][k])