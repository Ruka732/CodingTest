import sys

input = sys.stdin.readline

n, m = map(int, input().split())
seq = list(map(int, input().split()))

cnt = 0
for i in range(n):
  result = 0 # 부분 수열합 리셋
  result += seq[i] # 초항 선택 0~n-1
  if result == m: # 항 하나도 부분수열일 수 있으니까
    cnt += 1
  for j in range(i+1, n): # 다음 항부터 
    result += seq[j] # 부분 수열합
    if result == m: # 찾으면 Ok
      cnt += 1 # for문 안멈추고 다시 ㄱ

print(cnt)