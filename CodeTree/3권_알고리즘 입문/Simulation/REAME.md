## Simulation 주요 문제

### 격자 안에서 완전 탐색
- 트로미노
- 금 채굴하기: 마름모 범위 구하기 -> |i-x| + |j-y| <= k
- 기울어진 직사각형*** 
- 겹쳐지지 않는 두 직사각형**
- 양수 직사각형의 최대 크기* : 기본문제

### 격자 안에서 밀고 당기기
- 1차원 바람***
- 2차원 바람*
- 기울어진 직사각형의 회전***: 기울어진 직사각형 

### 격자 안에서 터지고 떨어지는 경우
떨어질 때 아래서부터 갱신 방향에 주의하기 : 아래서 위 방향
일시적으로 일어난 결과를 반영하기 위해 temp 사용

- 1차원 폭발 게임** : 연속된 폭탄의 개수 파악 & drop, getEndIdx
- 단 한 번의 2048 시도*** : drop & rotate
- 십자 모양의 지속적 폭발 : 기본문제 
- 2차원 폭발 게임 : 마스터 문제, getEndIdxOfExplosion

```java
// 정확하게 이해 필요 
public static void explode() {
	boolean didExplode;
	do {
			didExplode = false; 
			for (int i=0; i<endOfNumbers_1d; i++) {
					if (numbers_1d[i] == WILL_EXPLODE) continue;

					int endIdx = getEndIdxOfExplosion(i, numbers_1d[i]);

					if (endIdx-i+1 >= m) {
							fillZero(i, endIdx);
							didExplode = true;
					}
			}
			moveToTemp();
			copyFromTemp();

	} while (didExplode);
}
```