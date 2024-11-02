#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 07:05:19 2024

@author: pavan
"""

def visited(x, y, board, N):
    return 0 <= x < N and 0 <= y < N and board[x][y] == -1

def chess_board(N):
    return [[-1 for i in range(N)] for i in range(N)]

def knights_tour(N, x_start, y_start):
    board = chess_board(N)
    board[x_start][y_start] = 0
    
    knight_moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
    
    if not backtracking(N, board, knight_moves, x_start, y_start, 1):
        return "Solution does not exist"
    else:
        return board
    
def backtracking(N, board, knight_moves, x, y, count):
    if count == N*N:
        return True

    for k in sorted(knight_moves, key=lambda k: next_moves(N, board, x + k[0], y + k[1])):
        x_new = x + k[0]
        y_new = y + k[1]
        
        if visited(x_new, y_new, board, N):
            board[x_new][y_new] = count
            if backtracking(N, board, knight_moves, x_new, y_new, count+1):
                return True
            else:
                board[x_new][y_new] = -1
                
    return False

def next_moves(N, board, x, y):
    count = 0
    knight_moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
    for k in knight_moves:
        x_new = x + k[0]
        y_new = y + k[1]
        if visited(x_new, y_new, board, N):
            count += 1
    return count

N = 8
solution = knights_tour(N, 1, 1)

if isinstance(solution, str):
    print(solution)
else:
    for x in solution:
        print(' '.join(f'{num:2d}' for num in x))
