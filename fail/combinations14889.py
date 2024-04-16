import sys
from math import inf
from itertools import combinations
input = sys.stdin.readline

def get_synergy_diff(synergy_matrix, left, right):
	left_synergy, right_synergy = 0, 0

	for l_mem_1 in left:
		for l_mem_2 in left:
			left_synergy += synergy_matrix[l_mem_1][l_mem_2]

	for r_mem_1 in right:
		for r_mem_2 in right:
			right_synergy += synergy_matrix[r_mem_1][r_mem_2]

	return abs(left_synergy - right_synergy)

size = int(input().strip())
synergy_matrix = [list(map(int, input().strip().split(' '))) for _ in range(size)]

diff = inf
arr_idx = [i for i in range(size)]
l = tuple(combinations(arr_idx, size//2))

for elem_l in l:
	compl = [False for _ in range(size)]
	for idx in elem_l:
		compl[idx] = True
	elem_r = tuple(filter(lambda idx : not compl[idx], range(size)))
	diff = min(diff, get_synergy_diff(synergy_matrix, elem_l, elem_r))

print(diff)