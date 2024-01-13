# merge sort

import sys

def merge_sort(arr):
  # 길이 1이면 정렬됐다고 판단
  if len(arr) < 2:
    return arr
  
  # 중간 설정
  mid = len(arr) // 2
  # 중간 위로 다 분해
  top = merge_sort(arr[mid:]) # mid + 1 이 맞지 않나 ? 왜 mid가 맞지 - 멍청했다 슬라이싱 다시 보고 오자
  # 중간 아래로 다 분해
  bot = merge_sort(arr[:mid])
  
  # 병합할 빈 리스트 생성
  merged = []
  
  # 인덱스 비교를 위해 설정
  i = 0
  j = 0
  
  # 병합할땐 작은거 부터 큰거로 이어나감
  while i < len(bot) and j < len(top):
    
    if bot[i] < top[j]:
      merged.append(bot[i])
      i += 1
    else:
      merged.append(top[j])
      j += 1
  
  # 병합 마무리하고 남은 부분 붙이기
  merged += bot[i:]
  merged += top[j:]
  return merged

input = sys.stdin.readline

n = int(input())
arr = []

for i in range(n):
  num = int(input())
  arr.append(num)

for i in merge_sort(arr):
  print(i)

print(merge_sort(arr))

# 음수 나와서 안됨 ? 그런듯