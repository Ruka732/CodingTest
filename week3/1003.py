# 피보나치 함수

import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
  zero_dp = [0] * 41
  one_dp = [0] * 41
  
  zero_dp[0] = 1
  zero_dp[1] = 0
  
  one_dp[0] = 0
  one_dp[1] = 1
  
  n = int(input())
  
  for i in range(2, n+1):
    zero_dp[i] = zero_dp[i-1] + zero_dp[i-2]
    one_dp[i] = one_dp[i-1] + one_dp[i-2]
  
  print(zero_dp[n], end=' ')
  print(one_dp[n])