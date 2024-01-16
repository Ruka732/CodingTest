# 색종이 자르기
import sys

input = sys.stdin.readline

def dividing(graph, x, y, n):
  global white_count, blue_count
  a = graph[x][y]
  
  for i in range(x, x+n):
    for j in range(y, y+n):
      if a != graph[i][j]:
        dividing(graph, x, y, n//2)
        dividing(graph, x+(n//2), y, n//2)
        dividing(graph, x, y+(n//2), n//2)
        dividing(graph, x+(n//2), y+(n//2), n//2)
        # 자른 것들이 모두 똑같지 않으면 밑에 리턴이 X
        # 자른 후 모든 색이 같을 때 밑의 if 문으로 넘어가게 됨
        return # 마지막을 다 쪼갠 후에만 count에 더해주기 위해서 함수를 끝내주어야 함
  if a == 0:
    white_count += 1
    result[0].append(white_count)
  else:
    blue_count += 1
    result[1].append(blue_count)
  return result

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

white_count = 0
blue_count = 0
result = [[] for _ in range(2)]

dividing(graph, 0, 0, N)

print(len(result[0]))
print(len(result[1]))

# 1. graph 는 전역변수 선언 없이 안에 잘 들어감. 근데 왜 count 들은 선언해야하지
# 2. if a != graph[i][j]: 에서 return을 왜하는거지
# 3. 리턴은 단순히 함수를 끝내기 위해 사용했는데, 
# 안하면 처음 저장해놓은 숫자와 달라도 
# 반복문이 끝나면 색종이 개수가 카운트 되기 때문에 
# 모두 한숫자로 이루어지지 않으면 4방면으로 나누고 
# 숫자가 카운트 되기전에 return으로 함수를 끝내줘야 한다.