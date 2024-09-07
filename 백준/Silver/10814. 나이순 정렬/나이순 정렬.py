# 3시 9분
# 나이 -> 가입
n = int(input())

data = []
for i in range(n):
    age, name = input().split()
    data.append((int(age), i, name))
    
data.sort(key=lambda x: (x[0],x[1]))
for age, _, name in data:
    print(age, name)