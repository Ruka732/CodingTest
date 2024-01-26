# 피보나치 수2

import sys

input = sys.stdin.readline

n = int(input())

dp = [0] * 91

dp[1] = 1
dp[2] = 1
dp[3] = 2

def fibo(x):
  if x <= 3:
    return dp[x]
  
  if dp[x] != 0:
    return dp[x]
  
  dp[x] = fibo(x-2) + fibo(x-1)
  
  return dp[x]

print(fibo(n))