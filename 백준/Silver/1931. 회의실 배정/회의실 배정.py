c = int(input())

time = []
for _ in range(c):
    s,e = map(int, input().split())
    time.append((s,e))
    

time.sort(key=lambda x: (x[1], x[0]))

# 먼저 끝나는 애를 골라
cnt = 1
end = time[0][1]
for i in range(1, len(time)): # start: time[i][0], end: time[i][1]
    # 시간 겹치는 지 확인 저번 end랑 지금 start랑
    # 안겹치면
    if end <= time[i][0]:
        cnt += 1
        end = time[i][1]
        
print(cnt)