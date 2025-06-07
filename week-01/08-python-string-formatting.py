# https://www.hackerrank.com/challenges/python-string-formatting/problem?isFullScreen=true

def print_formatted(n):
    padding = len(bin(n)) - 2
    for i in range(1, n + 1):
        text = str(i)
        print(text.rjust(padding, ' '), end = ' ')
        
        text = oct(i)[2:]
        print(text.rjust(padding, ' '), end = ' ')
        
        text = hex(i)[2:].upper()
        print(text.rjust(padding, ' '), end = ' ')
        
        text = bin(i)[2:]
        print(text.rjust(padding, ' '))
        
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)