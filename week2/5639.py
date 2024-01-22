# 이진 검색 트리

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)

arr = []

# 노드 개수가 미리 주어지지 않아서
while True:
  try:
    x = int(input())
    arr.append(x)
  except:
    break


def postorder(arr):
  if len(arr) == 0:
    return
  
  tempL, tempR = [], [] 
  
  # input이 전위 순회한 결과로 주어짐 - 루트 노드를 주며 왼쪽으로 내려감
  root = arr[0]
  
  for i in range(1, len(arr)):
    # 이진 트리 쪼개기
    if arr[i] > root:
      tempL = arr[1:i]
      tempR = arr[i:]
      break
    
    # 자식이 한쪽에만 있는 경우.
    else:
      tempL = arr[1:]
  
  # 양쪽으로 재귀 수행
  postorder(tempL)
  postorder(tempR)
  # 재귀적으로 수행 후 root 값이 후외 순회한 결과 순으로 출력
  print(root)

postorder(arr)