import java.util.*;

// 동일한 부모 노드에 속해있음을 확인할 때까지, 2개씩 짝을 짓고, 횟수를 증가하며 기록

class Solution {
    public int solution(int n, int a, int b) {
        int answer = 0;

        while (a != b) {
            a = a/2 + a%2;
            b = b/2 + b%2;
            answer ++;
        }
        
        return answer;
    }
}