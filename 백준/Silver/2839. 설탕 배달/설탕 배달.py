# 12시 25분
'''나머지가 3의 배수지만 5의 배수는 안될 때까지
3 6 9 12일 때까지 5를 빼
3과 5의 최소공배수 15 전까지'''
n = int(input())


def aa(n):
    cnt = 0
    # 1순위
    if n%5 == 0:
        cnt =  n//5
        return cnt
    # 2순위
    n_35 = n
    while n_35>=3:
        if n_35 == 3 or n_35 == 6 or n_35 == 9 or n_35== 12:
            cnt += n_35 // 3
            return cnt
        n_35 -= 5
        cnt += 1
        
    # 3순위
    if n%3 == 0:
        cnt = n//3
        return cnt
    # 4순위
    cnt = -1
    return cnt

print(aa(n))