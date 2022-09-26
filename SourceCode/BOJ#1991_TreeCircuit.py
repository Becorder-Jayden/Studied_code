def PreOrd(v):
    if v == 0:
        return
    print(P[v], end='')     # 전위순회
    PreOrd(L[v])
    PreOrd(R[v])

def InOrd(v):
    if v == 0:
        return
    InOrd(L[v])
    print(P[v], end='')     # 중위순회
    InOrd(R[v])

def PosOrd(v):
    if v == 0:
        return
    PosOrd(L[v])
    PosOrd(R[v])
    print(P[v], end='')     # 후위순회

N = int(input())
P = [0] * (N+1)
L = [0] * (N+1)
R = [0] * (N+1)

for n in range(N):
    p, l, r = input().split()
    P[ord(p)-64] = p
    if l == '.':
        L[ord(p)-64] = 0
    else:
        L[ord(p)-64] = ord(l)-64
    if r == '.':
        R[ord(p)-64] = 0
    else:
        R[ord(p)-64] = ord(r)-64

PreOrd(1)
print()
InOrd(1)
print()
PosOrd(1)
