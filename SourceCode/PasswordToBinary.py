# password를 2진수로 변환

# 딕셔너리 이용
password = '416A676F725974684D2050726F626C656D20536F6C76696E6'

dic = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100',
       '5': '0101', '6': '0110', '7': '0111', '8': '1000', '9': '1001',
       'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}

binary = ''
for i in password:
    binary += dic[i]

print(binary)


# 도겸이형 방식: dictionary를 만드는 방법을 간소화
arr = '416A676F725974684D2050726F626C656D20536F6C76696E6'
hax = '0123456789ABCDEF'
hax_dic = {}
for i in range(16):
    hax_dic[hax[i]] = bin(i)
wor = ''
for j in arr:
    ans = hax_dic[j][2:]
    wor += f'{ans:0>4}'
s = ''
res = ''
for k in wor:
    s += k
    if len(s) == 7:
        res += s + ''
        s = ''
print(res)