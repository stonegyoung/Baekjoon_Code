# 3시 50분

n = int(input())

res = 666
cnt = 0
while True:
    
    if '666' in str(res):
        cnt +=1
        if cnt == n:
            print(res)
            break
        res += 1
        
    else:
        res += 1