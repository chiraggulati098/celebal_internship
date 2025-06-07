# https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=true

def minion_game(string):
    vowels = {'A','E','I','O','U'}
    
    k_score = 0
    s_score = 0
    n = len(string)

    for i in range(n):
        if string[i] in vowels:
            k_score += n - i
        else:
            s_score += n - i

    if k_score > s_score:
        print("Kevin", k_score)
    elif s_score > k_score:
        print("Stuart", s_score)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)