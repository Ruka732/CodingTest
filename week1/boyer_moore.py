# boyer moore

def bm(txt, pat):
  n = len(txt)
  m = len(pat)
  i = 0
  # 뒤에서 부터 접근을 위해 패턴 길이 -1
  # -1 : 인덱스를 0부터 시작하기 위해    
  j = m - 1
  
  while i <= n - m:
    while j >= 0:
      
      if pat[j] != txt[i+j]:
        move = find(pat, txt[i + m - 1])
        break
      j -= 1
    
    if j == -1:
      
      return True
    else:
      i += move
  
  return False

def find(pat, char):
  for i in range(len(pat)-2, -1, -1):
    if pat[i] == char:
      return len(pat)-i -1
  return len(pat)