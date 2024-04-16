import sys
from copy import deepcopy
input = sys.stdin.readline

def shift_up(piece):
	if all(row > 0 for row, col in piece):
		for idx in range(len(piece)):
			piece[idx][0] -= 1
	else:
		return [[-1,0]]

	return piece

def shift_right(piece, width):
	if all(col + 1 < width for row, col in piece):
		for idx in range(len(piece)):
			piece[idx][1] += 1
	else:
		return [[0,-1]]

	return piece

def get_piece_max(paper, piece, height, width):
	piece_max = 0

	while piece[0][0] != -1:
		curr_max = 0
		for row, col in piece:
			curr_max += paper[row][col]
			# test[row][col] = 1
		piece_max = max(piece_max, curr_max)
		
		r_piece = deepcopy(piece)
		while r_piece[0][1] != -1:		
			curr_max = 0
			for row, col in r_piece:
				curr_max += paper[row][col]

			piece_max = max(piece_max, curr_max)
			r_piece = shift_right(r_piece, width)

		piece = shift_up(piece, height)

	return piece_max


h, width = map(int, input().strip().split(' '))
paper = [list(map(int, input().strip().split(' '))) for _ in range(h)]

tet_s = [[[h-1,0],[h-1,1],[h-2,0],[h-2,1]]]
tet_i = [[[h-1,0],[h-1,1],[h-1,2],[h-1,3]],
		[[h-1,0],[h-2,0],[h-3,0],[h-4,0]]]
tet_l = [[[h-1,0],[h-1,1],[h-2,0],[h-3,0]],
		[[h-1,0],[h-1,1],[h-2,1],[h-3,1]],
		[[h-1,0],[h-2,0],[h-3,0],[h-3,1]],
		[[h-3,0],[h-3,1],[h-2,1],[h-1,1]],
		[[h-1,0],[h-2,0],[h-1,1],[h-1,2]],
		[[h-1,0],[h-1,1],[h-1,2],[h-2,2]],
		[[h-2,0],[h-2,1],[h-2,2],[h-1,2]],
		[[h-1,0],[h-2,0],[h-2,1],[h-2,2]]]
tet_z = [[[h-2,0],[h-3,0],[h-2,1],[h-1,1]],
		[[h-1,0],[h-2,0],[h-2,1],[h-3,1]],
		[[h-2,0],[h-2,1],[h-1,1],[h-1,2]],
		[[h-1,0],[h-1,1],[h-2,1],[h-2,2]]]
tet_t = [[[h-1,0],[h-2,1],[h-1,1],[h-1,2]],
		[[h-2,0],[h-2,1],[h-1,1],[h-2,2]],
		[[h-1,0],[h-2,0],[h-3,0],[h-2,1]],
		[[h-2,0],[h-3,1],[h-2,1],[h-1,1]]]

tet = []
tet.append(tet_s)
tet.append(tet_i)
tet.append(tet_l)
tet.append(tet_z)
tet.append(tet_t)

global_max = 0

for tet_ in tet:
	for piece in tet_:
		global_max = max(global_max, get_piece_max(paper, piece, h, width))

print(global_max)