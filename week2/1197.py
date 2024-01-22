# 최소 스패닝 트리

import sys

input = sys.stdin.readline

v, e = map(int, input().split())

vertices = [i for i in range(v+1)]
edges = []
for _ in range(e):
  # a, b : vetices , c : cost
  edges.append(list(map(int, input().split())))

# 비용 순으로 간선 정보를 정렬
edges.sort(key=lambda x: x[2])

def union_find(x):
  # vertex 와 vertices 의 인덱스가 다른 경우 : 이미 union_find 되어 있음
  # 그래프에 연결된 노드를 찾기 위해 재귀 함수 호출
  if x != vertices[x]:
    vertices[x] = union_find(vertices[x])
  
  return vertices[x]

answer = 0

# 각 간선 정보에 대해서
for start, end, cost in edges:
  # 크루스칼 알고리즘
  
  # 사이클 여부를 찾기 위해서
  sRoot = union_find(start)
  eRoot = union_find(end)
  # union_find
  if sRoot > eRoot:
    vertices[sRoot] = eRoot
  else:
    vertices[eRoot] = sRoot
  
  # 간선을 신장 트리에 추가 - 가중치 담기
  answer += cost

print(answer)

# edges = vertices - 1
# cycle 여부 판단에 대해서 잘 모르겠다.