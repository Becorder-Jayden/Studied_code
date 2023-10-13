## Backtracking 주요 문제

- 겹치지 않게 선분 고르기\*\*

```java
	selectedSegs.add(segments[cnt]);
	findMaxSegments(cnt+1);
	selectedSegs.remove(selectedSegs.size()-1);
	findMaxSegments(cnt+1);
```

- 사다리 타기\*\* : 결과를 배열에 담고 교체로 진행 → 가능한 모든 경우에 대응해 진행하는 것보다 효과적

## K개중 하나를 N번 선택하기

#### Simple

- 방향에 맞춰 최대로 움직이기\*\*
- 2명의 도둑\*

#### Condition

- 가능한 수열 중 최솟값 구하기\*\* : 두 부분의 연속 여부 확인

## 순열 만들기

- 외판원 순회\*\*
