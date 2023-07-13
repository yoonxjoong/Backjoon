def solution(name, yearning, photo):
    answer = []
    tmp = {}
    for index, i in enumerate(name):
        tmp[i] = yearning[index]
    for i in photo:
        sum = 0
        for j in i:
            if tmp.get(j) != None:
                sum += tmp.get(j)
        answer.append(sum)
        
    return answer