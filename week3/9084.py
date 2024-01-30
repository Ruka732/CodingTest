# 동전

import sys

input = sys.stdin.readline

n = int(input())

for _ in range(n):
  m = int(input())
  arr = list(map(int, input().split()))
  
  won = int(input())
  dp = [0] * (won+1)
  dp[0] = 1
  for j in arr:
    for i in range(1, won + 1):
      if i >= j:
        dp[i] += dp[i-j]
  
  print(dp[won])