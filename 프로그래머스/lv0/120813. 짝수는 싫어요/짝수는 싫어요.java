class Solution {
    public int[] solution(int n) {
        int size;
        if (n%2==1) {
            size = n/2+1;
        } else {
            size = n/2;
        }
        int[] answer = new int[size];
        
        int idx = -1;
        for (int i=0; i<=n; i++) {
            if (i%2 == 1) {
                answer[++idx] = i;
                System.out.print(answer[idx]+" ");
            }
        }
        
        
        
        return answer;
    }
}