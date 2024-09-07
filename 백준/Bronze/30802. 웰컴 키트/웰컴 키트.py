# https://www.acmicpc.net/problem/30802
# 1시 20분

n = int(input())
# s m l xl xxl xxxl
t_size= map(int, input().split())

t, p = map(int, input().split())

# 티는 사이즈마다
t_need = 0
for tshirt in t_size:
    if tshirt%t != 0:
        t_need += tshirt//t +1
    else:
        t_need += tshirt//t 
        
print(t_need)
# 펜은 사람 수만큼
print(n//p, n%p) # 묶음, 한 개