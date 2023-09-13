### Backtracking 주요 문제
- 겹치지 않게 선분 고르기**
``` java
selectedSegs.add(segments[cnt]);
findMaxSegments(cnt+1);
selectedSegs.remove(selectedSegs.size()-1);
findMaxSegments(cnt+1);
```