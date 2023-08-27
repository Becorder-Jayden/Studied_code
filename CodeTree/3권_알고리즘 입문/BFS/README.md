### BFS 요약 정리

```java
// 1. bfs 진행에 필요한 모듈 import
import java.util.Queue;
import java.util.LinkedList

// 2. Queue 선언
public static Queue<Pair> q = new LinkedList<>(); 

// 3. bfs 정의
while (!q.isEmpty()) {  // q가 비게 될 때 까지
	
	Pair curr = q.poll();  // q에서 하나의 요소 제거
	..
	..

	for (int i=0; i<DIR_NUM; ++) {
		if (canGo(nx, ny)) {
			q.add(new Pair(nx, ny)); 
			..
		}
	}
}

```

### BFS 주요 문제
- BFS 탐색
- k번 최댓값으로 이동하기***
- 돌 잘 치우기 **
