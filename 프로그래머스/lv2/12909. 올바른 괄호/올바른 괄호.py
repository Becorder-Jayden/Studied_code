def solution(s):
    ans = False
    lst = []
    for i in s:
        if i == '(':
            lst.append(i)
        else:
            if lst:
                if lst[-1] == '(':
                    lst.pop()
            else:
                lst.append(i)
    if lst == []:
        ans = True
    return ans