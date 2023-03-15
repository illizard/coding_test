from collections import deque

def solution(maps):
    row, col = len(maps), len(maps[0]) # 2d map
    dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)] # 이동 방향 상하좌우
    cur_loc = deque([(0, 0, 1)]) #이동 거리
    visited = set([(0, 0)]) #이미 방문 노드
    
    while cur_loc:
        x, y, d_mv = cur_loc.popleft() 
        if x == row-1 and y == col-1:
            return d_mv #종료 조건
        for dx, dy in dirs: 
            nx, ny = x + dx, y + dy #new 방문 노드
            if 0 <= nx < row and 0 <= ny < col and maps[nx][ny] == 1 and (nx, ny) not in visited: #이동 가능 조건
                visited.add((nx,ny))
                cur_loc.append((nx, ny, d_mv+1)) 
    return -1

if __name__=="__main__":
    maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
    res = solution(maps)    
    print(res)


