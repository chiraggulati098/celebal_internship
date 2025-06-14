# https://www.hackerrank.com/challenges/alphabet-rangoli/problem?isFullScreen=true

def print_rangoli(size):
    width = (size - 1) * 4 + 1
    stack = []
    
    for i in range(size):
        needed = 1 + (i * 4)
        padding = (width - needed) // 2
        
        num_alphabets = 1 + (i * 2)
        alphas = [0] * (num_alphabets)
        
        mid_alphabet = chr(ord('a') + size - i - 1)
        
        cur = 0
        for i in range(num_alphabets // 2, -1, -1):
            alphas[i] = cur
            cur += 1
        
        cur = 0
        for i in range(num_alphabets // 2, num_alphabets):
            alphas[i] = cur
            cur += 1
        
        for i in range(len(alphas)):
            alphas[i] = chr(ord(mid_alphabet) + alphas[i])
        
        line = ('-' * padding) + ('-'.join(alphas)) + ('-' * padding)
        print(line)
        stack.append(line)
    
    stack.pop()
    while stack:
        print(stack.pop())
    
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)