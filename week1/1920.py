# 수 찾기

import sys

sys.setrecursionlimit(10**9)

input = sys.stdin.readline

def binary_search(temp, pl, pr, arr):
  if pl > pr:
    return 0
  # arr.sort()
  # pl = 0
  # pr = len(arr) - 1
  pc = (pr + pl) // 2
  
  if arr[pc] == temp:
    return 1
  elif arr[pc] > temp:
    return binary_search(temp, pl, pc-1, arr)
  elif arr[pc] < temp:
    return binary_search(temp, pc+1, pr, arr)


n = int(input())
temp = list(map(int, input().split()))
m = int(input())
nums = list(map(int, input().split()))

temp.sort()
for j in nums:
  print(binary_search(j, 0, len(temp)-1, temp))

# fault 1
# 재귀함수 탈출 선언을 안해서 무한 루프
# fault 2
# pl, pr 값을 선언하고 시작해야하는데 안에서 0과 len(arr)-1로 계속 재생성
# fault 3
# 마지막 프린트하는 함수의 인자에 len(nums)-1 을 pr 값으로 넣음