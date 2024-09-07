# https://www.acmicpc.net/problem/13305
# 4시 39분~

city = int(input())
km = list(map(int, input().split()))
price = list(map(int, input().split()))

# km = [2, 3, 1]
# price = [5, 2, 4, 1]
kp = [(k, p) for k,p in zip(km, price)]

# 뒤의 가격이 더 싸지는 도시까지 가는 km는 지금 도시에서 충전
# kp[i][0] => 거리
# kp[i][1] => 가격


# 처음 도시에는 충전 해야 됨
total = kp[0][0] * kp[0][1]
cheap = kp[0][1]
for i in range(1, len(kp)):
    # 더 싸지는 도시까지의 거리 더함
    if cheap > kp[i][1]:
        cheap = kp[i][1]
    total += cheap*kp[i][0]
    
print(total)