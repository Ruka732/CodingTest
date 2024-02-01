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

# 안녕하세요 주민님
# 3주차 시험 치르시느라 고생하셨습니다.

# 저는 2579번(1번)과 1379번(3번) 문제를 시도했지만 모두 끝까지 풀어내진 못했습니다. 풀이 과정은 주석으로 적어 놨습니다.
# 그래서 코드 리뷰하실 때 제 코드에 대해서 리뷰를 해주시는 것도 좋겠지만,
# 주민님의 1,3번 문제 접근 방법(1번 문제의 경우 점화식을 세우겠다는 생각의 과정과 같은)이나, 저의 문제 접근 방법의 문제점을 중점적으로 다뤄주시면 제게 도움이 될 것 같습니다.

# 리뷰 잘 부탁드립니다. 감사합니다.