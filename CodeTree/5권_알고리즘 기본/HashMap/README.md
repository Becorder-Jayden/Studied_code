# HashMap

- 해싱을 기반으로 데이터를 관리

- (key, value) 쌍으로 관리

- 시간복잡도 O(1) : TreeMap 보다 속도가 빠르지만 순서에는 관심 x

### 사용법

```java
  import java.util.HashMap;

  public class Main {
    public static void main(String[] args) {
      HashMap<Integer, Integer> m = new HashMap<>();

      m.put(K, V);  // 데이터 입력
      m.remove(K, V);  // 데이터 제거
      m.get(K);  // 데이터 값 반환, cf. 값이 없다면 에러 발생
      m.containsKey(K);  // (값이 있을 때) 데이터 값 반환
      m.getOrDefault(K, D);  // 데이터 값 반환, 값이 없으면 D 반환
    }
  }
```

## HashMap 주요 문제

#### 두수의 합, 세수의 합을 정확하게 이해하는 것이 중요해보임

- 두 수의 합\*\* : O(n) 계산을 O(1) 시간 내에 계산
- 세 수의 합\*\*\* : 두 수의 합 문제에서 한 단계 발전
- 자주 등장한 top k 숫자 : hashmap에 정의된 값을 ArrayList에 담아 재정렬
- 원소의 합이 0 : 시간복잡도 고려, 2개씩 쌍을 지어 해결
