class Solution {
    public int solution(int n, int k) {
        int answer = 0;
        int serviceDrink = n/10;
        answer += n * 12000 + (k-serviceDrink) * 2000;
        return answer;
    }
}