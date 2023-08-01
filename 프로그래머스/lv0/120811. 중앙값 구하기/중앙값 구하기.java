import java.util.Arrays;

class Solution {
    public int solution(int[] array) {
        int answer = 0;
        int n = array.length;
        
        Arrays.sort(array, 0, n);
        
        answer = array[n/2];
        
        return answer;
    }
}