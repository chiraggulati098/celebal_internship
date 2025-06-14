# https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem?isFullScreen=true

n = int(input())
s = set(map(int, input().split()))

num = int(input())
for _ in range(num):
    command = input().split()
    
    if command[0] == 'pop':
        s.pop()
    elif command[0] == 'remove':
        s.remove(int(command[1]))
    else:
        s.discard(int(command[1]))

print(sum(s))