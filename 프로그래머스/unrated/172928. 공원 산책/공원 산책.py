def solution(park, routes):
    answer = []
    # 시작 위치
    x, y = 0, 0
    
    for index_i, i in enumerate(park):
        for index_j, j in enumerate(i):
            if j == 'S':
                x, y = index_i, index_j
                break;     
    
     # 이동 방향 정의
    op = {'N':(-1, 0), 'S':(1, 0), 'W':(0, -1), 'E':(0, 1)}
    
    for i in routes:
        tmp = i.split()
        xx, yy = x, y
        status = True
        dx, dy = op.get(tmp[0])
        for j in range(int(tmp[1])):
            nx = xx + dx
            ny = yy + dy
            
             # 공원 안에 있고, 장애물이 아니면 이동 가능(True)
            if 0 <= nx <= len(park)-1 and 0 <= ny <= len(park[0])-1 and park[nx][ny] != 'X':
                status = True
                xx, yy = nx, ny
            else:  # 공원을 벗어낫거나, 장애물이면 이동 불가(False)
                status = False
                break
                
        if status:
            x, y = nx, ny
        
    answer.append(x)
    answer.append(y)
    
    return answer