# 테트로미노

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

matrix = [[list(map(int, input().split()))] for _ in range(n)]

def move_right(size, current_x, current_y, matrix):
  if current_y + 1 < size:
    matrix[current_x][current_y+1]