# 검색된 문자열의 첫 인덱스+1 을 찾아준다.
# t : 주어진 문자열
# p : 찾는 문자열
def brute_force(t, p):
  i = 0 # t의 검색 인덱스
  j = 0 # p의 검색 인덱스
  while i < len(t) and j < len(p):
    if t[i] == p[j]:
      i += 1
      j += 1
    
    else: 
      i = i - j + 1
      j = 0
    
    return i - j if j == len(p) else -1