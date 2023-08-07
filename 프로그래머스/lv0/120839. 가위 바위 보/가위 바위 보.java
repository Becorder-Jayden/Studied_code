class Solution {
    public String solution(String rsp) {
        String answer = "";
        int n = rsp.length();
        for (int i=0; i<n; i++) {
            if (rsp.charAt(i) == '2') {
                answer += ""+0;
            } else if (rsp.charAt(i) == '0') {
                answer += ""+5;
            } else {
                answer += ""+2;
            }
        }
        return answer;
    }
}