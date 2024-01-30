# 01타일
import sys

input = sys.stdin.readline

n = int(input())

dp = [0] * (1000001)

for i in range(4):
  dp[i] = i

for i in range(4, n+1):
  dp[i] = (dp[i-2] + dp[i-1])%15746

print(dp[n])