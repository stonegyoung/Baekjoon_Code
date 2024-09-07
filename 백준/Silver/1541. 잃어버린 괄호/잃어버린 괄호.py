# https://www.acmicpc.net/problem/1541
# 3시 53분~
# - 앞에 괄호
# 예외: - 40 - 50 뒤에 +일 때만

original = input()

# 기호
pm = []
for o in original:
    if o=='+' or o=='-':
        pm.append(o) 
        
# 숫자
st = original.replace('+', ' ')
st = st.replace('-', ' ')
num = list(map(int, st.split()))

for i in range(len(pm)):
    if pm[i] == '-':
        n = 1
        while i+n<len(pm):
            if pm[i+n] == '-':
                break
            pm[i+n] = '-'
            n+=1

total = num[0]
for i in range(len(pm)):
    if pm[i] == '+':
        total += num[i+1]
    else:
        total -= num[i+1]
        
print(total)

