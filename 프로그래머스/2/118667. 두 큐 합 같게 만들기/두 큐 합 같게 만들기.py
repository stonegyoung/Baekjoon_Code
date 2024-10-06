from collections import deque
# 7시 47분

def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    answer = 0
    
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    
    if (sum1 + sum2) % 2 != 0:
        return -1 
    result = (sum1+ sum2) / 2
    if max(queue1) > result or max(queue2) > result:
        return -1
    
    for _ in range(len(queue1)*4):
        if sum1 > sum2:
            while sum1 > sum2:
                v = queue1.popleft()
                queue2.append(v)
                sum1 -= v
                sum2 += v
                answer += 1
        else:
            while sum1 < sum2:
                v = queue2.popleft()
                queue1.append(v)
                sum2 -= v
                sum1 += v
                answer += 1
        if sum1 == result:
            return answer
    return -1
