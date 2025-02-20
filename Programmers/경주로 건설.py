from heapq import heappop, heappush
from sys import maxsize

def solution(board):
    n = len(board)
    costs = [[[maxsize] * 4 for _ in range(n)] for _ in range(n)] # (행, 열, 방향)
    
    move_list = [(0,1,0), (1,0,1), (0,-1,2), (-1,0,3)]  # (행 이동, 열 이동, 방향)
    
    hp = []
    
    # 초기화
    if board[0][1] == 0: 
        heappush(hp, (100, 0, 1, 0))
        costs[0][1][0] = 100
    
    if board[1][0] == 0: 
        heappush(hp, (100, 1, 0, 1))
        costs[1][0][1] = 100
    
    
    while hp:
        each_cost, now_r, now_c, now_d = heappop(hp)
        
        for move_r, move_c, move_d in move_list:
            next_r = now_r + move_r
            next_c = now_c + move_c
            
            if 0 <= next_r < n and 0 <= next_c < n and board[next_r][next_c] == 0:
                if now_d == move_d:
                    new_cost = costs[now_r][now_c][now_d] + 100
                else:
                    new_cost = costs[now_r][now_c][now_d] + 600
                
                if new_cost < costs[next_r][next_c][move_d]:
                    costs[next_r][next_c][move_d] = new_cost
                    heappush(hp, (new_cost, next_r, next_c, move_d))
    
    return min(costs[n-1][n-1])