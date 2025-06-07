# https://www.hackerrank.com/challenges/compress-the-string/problem?isFullScreen=true

num = input()

prev = None
cnt = None

for x in num:
    if not prev:
        prev = x
        cnt = 1
        continue
    
    if prev == x:
        cnt += 1
    else:
        print(f"({cnt}, {prev})", end = " ")
        prev = x
        cnt = 1

print(f"({cnt}, {prev})")