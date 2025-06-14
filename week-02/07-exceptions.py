# https://www.hackerrank.com/challenges/exceptions/problem?isFullScreen=true

num = int(input())

for _ in range(num):    
    try:
        a, b = map(int, input().split())
        print(a//b)
    except ZeroDivisionError as e:
        print("Error Code:",e)
    except ValueError as e:
        print("Error Code:",e)