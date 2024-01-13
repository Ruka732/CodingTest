# quick sort

import sys

sys.setrecursionlimit(10**4)

def quick_sort(arr, start, end):
  # 원소가 1개 일때
  if start >= end:
    return
  
  pivot = start
  left = start + 1
  right = end
  
  while left <= right:
    # pivot 보다 큰 데이터 찾을 때 까지 반복, 왼쪽
    while left <= end and arr[left] <= arr[pivot]:
      left += 1
    # pivot 보다 작은 데이터 찾을 때 까지 반복, 오른쪽
    while right > start and arr[pivot] <= arr[right]:
      right -= 1
    # 엇갈릴 경우 pivot과 작은 값 교체
    if left > right:
      arr[right], arr[pivot] = arr[pivot], arr[right]
    else:
      # 엇갈리지 않은 경우 왼쪽 오른쪽 교환
      arr[right], arr[left] = arr[left], arr[right]
  
  # 분할 완료 후 재귀적으로 퀵정렬 수행
  quick_sort(arr, start, right - 1)
  quick_sort(arr, right + 1, end)

input = sys.stdin.readline

n = int(input().rstrip())
arr = []

for i in range(n):
  num = int(input())
  arr.append(num)

quick_sort(arr, 0, len(arr)-1)

for i in arr:
  print(i)