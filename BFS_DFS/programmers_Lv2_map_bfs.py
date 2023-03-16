from collections import deque

def solution(maps):
    row, col = len(maps), len(maps[0]) # 2d map
    dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)] # 이동 방향 상하좌우
    cur_loc = deque([(0, 0, 1)]) #이동 거리
    visited = set([(0, 0)]) #이미 방문 노드
    
    while cur_loc:
        y, x, d_mv = cur_loc.popleft() 
        if y == row-1 and x == col-1:
            return d_mv #종료 조건
        for dy, dx in dirs: 
            ny, nx = y + dy, x + dx #new 방문 노드
            if 0 <= ny < row and 0 <= nx < col and maps[ny][nx] == 1 and (ny, nx) not in visited: #이동 가능 조건
                visited.add((ny,nx))
                cur_loc.append((ny, nx, d_mv+1)) 
    return -1

if __name__=="__main__":
    maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
    res = solution(maps)    
    print(res)


