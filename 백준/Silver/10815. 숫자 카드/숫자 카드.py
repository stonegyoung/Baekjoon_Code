# 4시 45분
import sys
input = sys.stdin.readline

m = int(input())
cards = list(map(int, input().split()))

n = int(input())
have = list(map(int, input().split()))

cards = set(cards)
for c in have:
    if c in cards:
        print('1', end = ' ')
    else:
        print('0', end = ' ')