import sys
input = sys.stdin.readline

res = 0
for _ in range(3):
    a = input().rstrip()
    
    if a.isdigit():
        res = int(a)
    else:
        res +=1

res += 1
if res % 5 == 0 and res % 3 == 0:
    print('FizzBuzz')
elif res % 5 == 0:
    print('Buzz')
elif res % 3 == 0:
    print('Fizz')
else:
    print(res)