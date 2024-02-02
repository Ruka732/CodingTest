# 계단 오르기

import sys

input = sys.stdin.readline

n = int(input())

stairs = [0] + [int(input()) for _ in range(n)]

dp = [0] * 301

# 3번 전까진 규칙이 고정
if n > 0:
  dp[1] = stairs[1]
if n > 1:
  dp[2] = stairs[1] + stairs[2]
if n > 2:
  dp[3] = max(stairs[1]+ stairs[3], stairs[2] + stairs[3])

for i in range(4, n+1):
  # if dp[i] == dp[i-1] + stairs[i-1]

  # 이후 테이블 만들때 3번 연속 1칸씩 뛰지 않기 위해
  # dp[i-1]의 사용을 피한다 -> 사용 시 한칸씩 계속 뜀
  dp[i] = max(dp[i-3] + stairs[i-1] + stairs[i], dp[i-2] + stairs[i])

# print(dp)
print(dp[n])

# dp[i] = max(dp[i-1], dp[i-2]) + stairs[i] 
# 세 계단 연속 x
