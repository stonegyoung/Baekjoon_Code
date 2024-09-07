# https://www.acmicpc.net/problem/1181
# 2시 10분
def same_len(x):
    return ord(x)


n = int(input())

voca = []
for _ in range(n):
    voca.append(input())
    
voca = list(set(voca))
# 길이가 짧은 것부터 단어 순
voca.sort(key=lambda x: tuple([len(x)]+[same_len(x[i]) for i in range(len(x))]))

for v in voca:
    print(v)