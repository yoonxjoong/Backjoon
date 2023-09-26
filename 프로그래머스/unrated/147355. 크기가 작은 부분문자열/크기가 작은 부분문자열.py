def solution(t, p):
    answer = 0
    tmp_len = len(p)
    result = [t[i:i+tmp_len] for i in range(len(t) - tmp_len + 1)]
    
    for i in result:
        if i <= p:
            answer += 1
    
    return answer