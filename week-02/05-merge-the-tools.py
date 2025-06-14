# https://www.hackerrank.com/challenges/merge-the-tools/problem?isFullScreen=true

def merge_the_tools(string, k):
    res = []
    
    for i in range(0, len(string), k):
        s = ""
        seen = set()
        for j in range(i, i + k):
            if string[j] in seen:
                continue
            s += string[j]
            seen.add(string[j])
        
        res.append(s)
    
    for x in res:
        print(x)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)