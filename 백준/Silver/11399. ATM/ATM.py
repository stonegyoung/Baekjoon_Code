n = int(input())
t_list = list(map(int, input().split()))

sum_time, wait = 0, 0
# 제일 적게 나오는 사람
for t in sorted(t_list):
    # 합
    sum_time += wait + t 
    # 뒷 사람이 기다려야 하는
    wait += t
    
print(sum_time)