import sys

input = sys.stdin.readline

def quad(graph, x, y, n):
  global result
  # result += '('
  a = graph[x][y]
  
  for i in range(x, x+n):
    for j in range(y, y+n):
      if graph[i][j] != a:
        result += '('
        quad(graph, x, y, n//2)
        quad(graph, x, y+(n//2), n//2)
        quad(graph, x+(n//2), y, n//2)
        quad(graph, x+(n//2), y+(n//2), n//2)
        result += ')'
        return
  if a == 1:
    result += '1'
  else:
    result += '0'
  return result

N = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(N)]
result = ''

quad(graph, 0, 0, N)

print(result)