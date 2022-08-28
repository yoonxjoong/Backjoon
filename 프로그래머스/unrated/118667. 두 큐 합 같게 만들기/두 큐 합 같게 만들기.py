from collections import deque
def solution(queue3, queue4):
    queue1 = deque(queue3)
    queue2 = deque(queue4)
    s_1 = sum(queue3)
    s_2 = sum(queue4)
    for i in range(len(queue1) * 3):    
        if s_1 == s_2 :
            return i
        if s_1 > s_2:
            q_1 = queue1.popleft()
            queue2.append(q_1)
            s_1 -= q_1
            s_2 += q_1
        else:
            q_2 = queue2.popleft()
            queue1.append(q_2)
            s_2 -= q_2
            s_1 += q_2
    return -1