# LCS

import sys

input = sys.stdin.readline

arr1 = [''] + list(map(str, input().strip()))
arr2 = [''] + list(map(str, input().strip()))
m, n = len(arr1), len(arr2)
dp = [[0]*(m) for _ in range(n)]

for i in range(1, n): # arr2 에 대해서
  for j in range(1, m): # arr1 에 대해서
    if arr2[i] == arr1[j]: # 끝이 같은 경우
      dp[i][j] = dp[i-1][j-1] + 1
    else: # 그 외의 경우
      dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[n-1][m-1])