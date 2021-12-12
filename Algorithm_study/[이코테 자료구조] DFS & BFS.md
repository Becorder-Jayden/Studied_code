# DFS / BFS

by 나동빈님

링크

https://www.youtube.com/watch?v=7C9RgOcvkvo&list=PLRx0vPvlEmdAghTr5mXQxGpHjWqSz0dgC&index=3



* 탐색 : 많은 양의 데이터 중 원하는 데이터를 찾는 과정
* DFS, BFS는 탐색 알고리즘에 해당
* 코딩 테스트에서 자주 등장하는 유형





## 스택 자료구조



* **선입후출** : 먼저 들어온 데이터가 나중에 나가는 형식

* **입구와 출구가 동일한 형태**

  ex) 박스 쌓기, 플링글스 통 구조

* 삽입과 삭제로 진행, 시간복잡도 : O(1)


```python
stack = []

stack.append(n)
stack.pop(n)
```

* 최상단 원소부터 출력하려면 stack을 역순으로 출력





## 큐 자료구조



* **선입선출** : 먼저 들어온 데이터가 먼저 나가는 형식

* **입구와 출구가 모두 뚫려 있는 터널**과 같은 형태

  ex) 투표 대기 줄, 배식 줄

* 삽입과 삭제로 진행, 시간복잡도 : O(1)

```python
from collections import deque

# 큐 구현을 위해 deque 라이브러리 사용
queue = deque()

queue.append(n) 
queue.popleft(n)
```

​		cf. 파이썬에서 리스트 자료형을 이용해 큐를 구현할 수 있지만, 시간 복잡도가 더 높아서 비효율적으로 계산될 수 있기 때문에 deque을 이용하는 것이 좋다

* 먼저 들어온 순서대로 출력하려면 queue를 역순으로 출력





## 재귀 함수 (Recursive Function)



* **자기 자신을 다시 호출하는 함수**

* DFS를 실질적으로 구현하고자 할 때 자주 사용
* 재귀 함수를 사용할 때는 재귀 함수의 종료 조건을 반드시 명시해야 한다

```python
def recursive_function(i):
    # 종료조건을 명시
    if i == 100:
        return
    print(i, '번째 재귀함수에서', i+1, '번째 재귀함수를 호출합니다.')
    recursive_function(i + 1)
    print(i, '번째 재귀함수를 종료합니다.')
```





### 팩토리얼 구현 예제

* n! = 1 * 2 * 3 * ... * (n-1) * n
* 0!과 1!의 값은 1

```python
# 반복적으로 구현한 n!

def factorial_iterative(n):
    result = 1
    # 1에서 n까지 수를 차례대로 곱하기
    for i in range(1, n+1):
        result *= i
    return result

# 재귀적으로 구현한 n!

def factorial_recursive(n):
    # 종료조건 : n이 1이하일 때 1 반환
    if n <= 1:
        return 1
    # n! = n * (n-1)! 적용
    return n * factorial_recursive(n-1)
```





### 최대공약수 계산 (유클리드 호제법) 예제

* 유클리드 호제법
  * 두 자연수 A, B에 대하여 (A>B) A를 B로 나눈 나머지를 R이라고 하자
  * A와 B의 최대공약수는 B와 R의 최대공약수와 같다
* 재귀함수를 통해 유클리드 호제법 아이디어를 작성할 수 있다

```python
def gcd(a, b):
	if a % b == 0:
    	return b
    else:
    	return gcd(b, a % b)
```



* 재귀함수를 잘 활용하면 복잡한 알고리즘을 간결하게 작성할 수 있다
* 모든 재귀함수는 반복문을 이용해 동일한 기능을 구현할 수 있다
* 재귀 함수가 반복문 보다 유리할 수도, 불리할 수도 있다
* 컴퓨터가 함수를 연속적으로 호출하면 컴퓨터메모리 내부의 스택 프레임에 쌓이게 된다
  * 스택을 사용해야 할 때 구현상 **스택 라이브러리 대신에 재귀 함수를 이용**하는 경우가 많다





## DFS (Depth-First Search)



* DFS는 **깊이 우선 탐색**이라고도 부르며, 그래프의 **깊은 부분을 우선적으로 탐색하는 알고리즘**이다
* DFS는 스택 자료구조(또는 재귀 함수)를 이용한다
  1. 탐색 시작 노드를 스택에 삽입하고 방문 처리를 한다
  2. 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 그 노드를 스택에 넣고 방문처리한다. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다
  3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복한다
* 최대한 깊게 들어가는 방식으로 동작하기 때문에 스택 자료구조 대신 재귀함수를 이용해 구현



* DFS 소스코드 예제

```python
# DFS 메서드 정의
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end = ' ')
    
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# 각 노드가 연결된 정보를 표현 (2차원 리스트)       
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

# 각 노드가 방문된 정보를 표현 (1차원 리스트)
visited = [False] * 9

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)

## 1 2 7 6 8 3 4 5
```





# BFS (Breadth-First Search)



* BFS는 **너비 우선 탐색**이라고도 부르며 , 그래프에서 **가장 가까운 노드부터 우선적으로 탐색**하는 알고리즘
* **큐 자료구조**를 이용
  1. 탐색 시작 노드를 큐에 삽입하고 방문 처리한다
  2. 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리한다
  3. 더 이상 2의 과정을 수행할 수 없을 때 까지 반복한다

* ex) 시작노드인 1로부터 [거리가 1인 노드, 거리가 2인 노드, ...] 와 같은 탐색 순서를 갖는다



* BFS 소스코드 예제

```python
from collections import deque

# BFS 메서드 정의
def bfs(graph, start, visited):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    
    # 현재 노드를 방문 처리
    visited[start] = True
    
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in praph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 각 노드가 연결된 정보를 표현 (2차원 리스트) 
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

# 각 노드가 방문된 정보를 표현 (1차원 리스트)
visited = [False] * 9

# 정의된 DFS 함수 호출
bfs(graph, 1, visited)

## 1 2 3 8 7 4 5 6
```



※ 예시 문제 : [음료수 얼려 먹기, 미로 탈출]

* 연결 요소 찾기(Connected Component) 문제  
* BFS는 간선의 비용이 모두 같을 때 최단거리를 탐색하기 위해 사용할 수 있다 





§ DFS, BFS의 예시 문제는 풀이 이해 후에 정리해보도록 하자

