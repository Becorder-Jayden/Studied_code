class Solution {
    public int solution(int n) {
        int answer = 0;
        
        int cnt = 1; 
        while ((cnt*6)%n != 0) {
            cnt ++;
        }
        answer = cnt;
        
        return answer;
    }
}