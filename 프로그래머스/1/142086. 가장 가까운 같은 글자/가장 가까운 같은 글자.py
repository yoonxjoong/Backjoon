def solution(s):
    answer = []
    alp_index = {}
    for idx, alp in enumerate(s):
        if alp not in alp_index:
            answer.append(-1)
        else:
            answer.append(idx - alp_index[alp])
            
        alp_index[alp] = idx
    return answer