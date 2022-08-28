def solution(sizes):
    
    
    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            sizes[i].reverse()
    answer = max(r[0] for r in sizes) * max(r[1] for r in sizes)
    return answer