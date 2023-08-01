class Solution {
    public int[] solution(int numer1, int denom1, int numer2, int denom2) {
        int[] answer = new int[2];
        
        int num1 = numer1 * denom2;
        int num2 = numer2 * denom1; 
        int num = num1+num2; 
        int denom = denom1 * denom2;
        
        for (int i=denom; i>=2; i--) {
            if (num%i == 0 && denom%i==0) {
                num /= i;
                denom /= i;
            }
        }
        answer[0] = num;
        answer[1] = denom;
        
        return answer;
    }
}