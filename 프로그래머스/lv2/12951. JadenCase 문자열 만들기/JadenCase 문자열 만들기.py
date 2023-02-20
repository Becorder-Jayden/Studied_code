def solution(s):
    s = s.lower()
    ans = ''
    
    for i in range(len(s)):
        if i == 0:
            ans += s[i].upper()
        elif s[i-1] == ' ':
            ans += s[i].upper()
        else:
            ans += s[i]
    return ans