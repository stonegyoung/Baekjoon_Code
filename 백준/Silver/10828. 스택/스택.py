# 3시 30분
from sys import stdin
n = int(stdin.readline())

stack = []
st = []
for _ in range(n):
    cmd = stdin.readline().split()

    # push 일 때
    if len(cmd) == 2:
        stack.append(cmd[1])
    else:
        if cmd[0] == 'pop':
            if len(stack) == 0:
                st.append(-1)
            else:
                st.append(stack[-1])
                stack.pop()
        elif cmd[0] == 'size':
            st.append(len(stack))
        elif cmd[0] == 'empty':
            if len(stack) == 0:
                st.append(1)
            else:
                st.append(0)
        else: # top
            if len(stack) == 0:
                st.append(-1)
            else:
                st.append(stack[-1])
for s in st:
    print(s)