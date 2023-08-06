class Solution {
    public int solution(String ineq, String eq, int n, int m) {
        int answer = 0;
        boolean tf = false;
        if (ineq.equals(">") && eq.equals("=")) {
            if (n >= m) {
                tf = true;
            } 
        } else if (ineq.equals("<") && eq.equals("=")) {
            if (n <= m) {
                tf = true;
            } 
        } else if (ineq.equals(">") && eq.equals("!")) {
            if (n > m) {
                tf = true;
            }
        } else if (ineq.equals("<") && eq.equals("!") ){
            if (n < m) {
                tf = true;
            }
        }
                   
        if (tf) answer = 1;
        else answer = 0;
                   
        return answer;
    }
}