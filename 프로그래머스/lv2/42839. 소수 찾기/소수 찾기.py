from itertools import combinations, permutations

def sosu(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    p = []
    result = set()
    
    for i in range(1, len(numbers) + 1):
        p.extend(permutations(numbers, i))
        result = {int(''.join(i)) for i in p}
    
    result.discard(0) 
    result.discard(1)
     
    for num in result:
        if sosu(num) == True:
            answer += 1
            
    return answer