# 4시 33분
def sm(data):
    last = []
    for d in data:
        if d == '(':
            last.append('(')
        elif d == ')':
            if len(last) == 0:
                return 'no'
            v = last.pop()
            if v == '[':
                return 'no'
        elif d == '[':
            last.append('[')
        elif d == ']':
            # last가 (이면
            if len(last) == 0:
                return 'no'
            v = last.pop()
            if v == '(':
                return 'no'
    if len(last) == 0:        
        return 'yes'
    else:
        return 'no'

while True:
    st = input()
    if st == '.':
        break
    
    # ()[]만 남긴다
    data = ''
    for s in st:
        if s in set(['(', ')', '[', ']']):
            data += s
    
    print(sm(data))
    
    