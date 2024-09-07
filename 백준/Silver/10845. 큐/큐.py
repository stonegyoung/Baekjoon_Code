# 3시 30분~3시 50분
from sys import stdin
from collections import deque
n = int(stdin.readline())

queue = deque()
st = []
for _ in range(n):
    cmd = stdin.readline().split()

    # push 일 때
    if len(cmd) == 2:
        queue.append(cmd[1])
    else:
        if cmd[0] == 'pop':
            if len(queue) == 0:
                st.append(-1)
            else:
                st.append(queue[0])
                queue.popleft()
        elif cmd[0] == 'size':
            st.append(len(queue))
        elif cmd[0] == 'empty':
            if len(queue) == 0:
                st.append(1)
            else:
                st.append(0)
        elif cmd[0] == 'front':
            if len(queue) == 0:
                st.append(-1)
            else:
                st.append(queue[0])
        elif cmd[0] == 'back':
            if len(queue) == 0:
                st.append(-1)
            else:
                st.append(queue[-1])
        
for s in st:
    print(s)