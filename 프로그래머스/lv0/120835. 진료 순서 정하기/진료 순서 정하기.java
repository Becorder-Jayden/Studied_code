class Solution {
    public int[] solution(int[] emergency) {
        int n = emergency.length;
        int[] answer = new int[n];
    
        int[] rankArr = new int[n];
        int rank = 1;
        for (int i=0; i<n; i++) {
            rankArr[i] = rank++; 
        }
        
        for (int i=0; i<n; i++) {
            for (int j=0; j<n; j++) {
                if ((emergency[i] < emergency[j]) && (rankArr[i] < rankArr[j])) {
                    int temp = rankArr[i];
                    rankArr[i] = rankArr[j];
                    rankArr[j] = temp;
                }
            }
        }
        
        for (int i=0; i<n; i++) {
            answer[i] = rankArr[i];
        }

        
        return answer;
    }
}