from sys import stdin

def count_total(cm, mid):
    total = 0
    for c in cm:
        total += c // mid
    return total

def line_cut(start, end, cm, n):
    while start <= end:
        mid = (start + end) // 2
        total = count_total(cm, mid)

        if total >= n:  # 충분히 많은 랜선을 만들 수 있는 경우
            start = mid + 1
        else:  # 랜선 개수가 부족한 경우
            end = mid - 1

    return end

k, n = map(int, stdin.readline().split())

cm = [int(stdin.readline().rstrip()) for _ in range(k)]

start = 1
end = max(cm)

print(line_cut(start, end, cm, n))