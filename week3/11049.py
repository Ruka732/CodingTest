# 행렬 곱셈 순서

import sys

input = sys.stdin.readline

n = int(input())

matrices = []
for _ in range(n):
  matrices.append(list(map(int,input().split())))

# matrices[i][0] = ri, matrices[i][1] = ci
inf = 1e9
dp = [[0]*(n+1) for _ in range(n+1)]

for j in range(1, n+1): # 선택한 행렬과의 차이
  for i in range(1, n+1): # 행렬 선택
    if i + j == n+1: # 범위 넘어갈 시
      break
    
    dp[i][i+j] = inf 
    
    for k in range(i, i+j): # 두 행렬 사이의 중간점들에 찍어주기
      dp[i][i+j] = min(dp[i][i+j], dp[i][k] + dp[k+1][i+j] + matrices[i-1][0]*matrices[k-1][1]*matrices[i+j-1][1])

print(dp[1][n])