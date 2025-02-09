ans = 0
def bt(idx, res, numbers, targets):
    if idx == len(numbers):
        if res == targets:
            global ans
            ans += 1
            return
        else:
            return
    bt(idx+1, res+numbers[idx], numbers, targets)
    bt(idx+1, res-numbers[idx], numbers, targets)


def solution(numbers, target):
    global ans
    if sum(numbers) == target:
        return 0
    bt(0, 0, numbers, target)
    return ans