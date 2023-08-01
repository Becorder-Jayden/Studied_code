class Solution {
    public int solution(int slice, int n) {
        int answer = 0;
        
        int cnt = 1;
        while(cnt*slice/n < 1) {
            cnt ++;
        }
        answer = cnt; 
        
        return answer;
    }
}