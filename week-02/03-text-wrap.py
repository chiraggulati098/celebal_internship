# https://hackerrank.com/challenges/text-wrap/problem?isFullScreen=true

import textwrap

def wrap(string, max_width):
    res = ""
    
    cur = max_width
    for x in string:
        res += x
        cur -= 1
        
        if cur == 0:
            res += "\n"
            cur = max_width
            
    return res

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)