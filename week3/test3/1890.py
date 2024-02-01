# 점프

import sys

input = sys.stdin.readline

n = int(input())
moving = [list(map(int, input().split())) for _ in range(n)]

# dp = [[0]*(101) for _ in range(101)]
dp = [[0]*(n+1) for _ in range(n+1)]

dp[1][1] = 1  # 시작점 고정
for i in range(1, n+1):
  for j in range(1, n+1):
    if dp[i][j] != 0 and moving[i-1][j-1]: # 지나갈 경로들에 대해서만 시도
      if i + moving[i-1][j-1] <= n: # 영역 벗어나지 않으면
        dp[i+ moving[i-1][j-1]][j] += dp[i][j] # 들를때마다 += 1 우향 이동
      if j + moving[i-1][j-1] <= n:
        dp[i][j+ moving[i-1][j-1]] += dp[i][j] # 하향 이동
    
    # print(moving[i-1][j-1])
    # print(dp)

# print(moving)
# print(dp)
print(dp[n][n])

# Q : 왜 마지막에 두번 더 찍지 ?

# 분기 - 점 도착 시 값 만큼 오른쪽 or 아래
# 그래프 밖으로 나가면 안된다.
# 2-D dp table, 분기마다 도착점에 += 1
# dp[n-1][n] + dp[n][n-1] (1일때) - > 안된다 그냥 계속 돌려서 경로합을 dp[n][n]에 출력하자