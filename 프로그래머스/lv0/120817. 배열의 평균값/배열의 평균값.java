class Solution {
    public double solution(int[] numbers) {
        double answer = 0;
        int len = numbers.length;
        
        int totalSum = 0;
        for (int i=0; i<len; i++) {
            totalSum += numbers[i];
        }
        
        answer = (double)totalSum / len;
        
        return answer;
    }
}