#### 풀기 전 생각해보기😮

- 시작점에서 출발하는게 편할까? 도착점에서 출발하는게 편할까?
- 특정 조건을 만족할 때까지 전진시키는 방법

---

#### 풀이🛫

```python
T = 10

for t in range(T):
    case = int(input())
    arr = [list(map(int, input().split())) for i in range(100)]
    # 도착지점의 인덱스 찾기
    col, row = 0, 0
    for end in range(100):
        if arr[99][end] == 2:
            col = 99
            row = end
            break

    # 출발점에 도착할 때까지 진행
    while col != 0:     # col == 0: 시작점
        # 왼쪽에 길이 있을 때
        if row-1 >= 0 and arr[col][row-1] == 1:
            while row-1 >= 0 and arr[col][row-1] == 1:   # 왼쪽에 길이 없을 때까지 전진
                row -= 1

        # 오른쪽에 길이 있을 때
        elif row+1 < 100 and arr[col][row+1] == 1:
            while row+1 < 100 and arr[col][row+1] == 1:   # 오른쪽에 길이 없을 때까지 전진
                row += 1

        # 위 조건에 해당하지 않을 때 위로 이동
        col -= 1

    print(f"#{t+1}", row))
```

#### 핵심 정리🎁

- 경로와 경로가 아닌 곳을 표시하는 것이 0과 1로 구분되어 있다. 특별히 도착점의 경우 2로 표기가 따로 되어 있기 때문에 도착점을 어렵지 않게 찾을 수 있다.
- 출발지점에서 도착지점으로 연결된 경로를 찾으려면 모든 시작점에 대해서 탐색해야 하지만, 도착지점에서 반대로 시작지점을 찾을 경우 하나의 경우만 탐색하면 되기 때문에 풀이가 훨씬 쉬워질 수 있다.

#### 링크💎

[

SW Expert Academy

SW 프로그래밍 역량 강화에 도움이 되는 다양한 학습 컨텐츠를 확인하세요!

swexpertacademy.com

](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14ABYKADACFAYh)

#### 

#### 후기 😎

- while문이 사용되는 조건을 설정할 때 자주 오류를 범하는 편이다.
- while문 이후의 나오는 조건 <u>동안</u> while문 이하의 코드가 진행된다는 것을 주의하자.
- 풀릴 듯 안풀릴 듯 풀어내서 다행
