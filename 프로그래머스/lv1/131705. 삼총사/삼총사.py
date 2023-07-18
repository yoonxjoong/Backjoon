import itertools

def solution(number):
    answer = 0
    combinations = itertools.combinations(number, 3)
    for combination in combinations:
        if sum(combination) == 0:
            answer += 1
    return answer