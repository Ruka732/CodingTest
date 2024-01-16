# N-Queen

# 1 - 같은 행에 있으면 안됨
# 2 - 같은 열에 있으면 안됨
# 3 - 같은 대각선에 있으면 안됨
# 4 - 같은 역대각선에 있으면 안됨


# 3 - 인덱스 차가 같음
# 4 - 인덱스 합이 같음

import sys

sys.setrecursionlimit(10 ** 4)

input = sys.stdin.readline

def n_queen(n):
  
  def backtrack(row, dia, anti_dia, cols):
    
    if row == n:
      return 1
    
    result = 0
    
    for col in range(n):
      
      num_dia = row - col
      num_anti = row + col
      
      if col in cols or num_dia in dia or num_anti in anti_dia:
        continue
      
      cols.add(col)
      dia.add(num_dia)
      anti_dia.add(num_anti)
      
      result += backtrack(row + 1, dia, anti_dia, cols)
      
      cols.remove(col)
      dia.remove(num_dia)
      anti_dia.remove(num_anti)
      
    return result
  return backtrack(0, set(), set(), set())

n = int(input())
print(n_queen(n))

# 부끄럽지만 솔루션 찾아서 씀
# 너무 어려움 혼자 몇 번 더 봐야할 듯