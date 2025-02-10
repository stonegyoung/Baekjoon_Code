# 11:11
def solution(video_len, pos, op_start, op_end, commands):
    ss, mm = map(int, video_len.split(":"))
    vl = ss*60 + mm
    
    ss, mm = map(int, pos.split(":"))
    now = ss*60 + mm
    
    ss, mm = map(int, op_start.split(":"))
    op_st = ss*60 + mm
    
    ss, mm = map(int, op_end.split(":"))
    op_en = ss*60 + mm
    if op_st <= now <= op_en:
        now = op_en
    for cmd in commands:
        if cmd == 'next':
            if now + 10 > vl:
                now = vl
            else:
                now += 10
            if op_st <= now <= op_en:
                now = op_en
        elif cmd == 'prev':
            if now - 10 < 0:
                now = 0
            else:
                now -= 10
            if op_st <= now <= op_en:
                    now = op_en
    
    answer = f'{now // 60:02}:{now % 60:02}'
    return answer