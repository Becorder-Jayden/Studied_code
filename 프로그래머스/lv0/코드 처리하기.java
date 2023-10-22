class Solution {
    public String solution(String code) {
        /* 
            StringBuilder를 사용하면 문자를 쉽게 다룰 수 있다
            append(): 문자열 추가
            insert(): 문자열 삽입
            delete(): 문자열 삭제
            replace(): 문자열 대체
        */ 
        StringBuilder answer = new StringBuilder();
        int mode = 0;

        for (int i = 0; i < code.length(); i++) {
            char current = code.charAt(i);
            if (current == '1') {
                mode = mode == 0 ? 1 : 0;  // 삼항 연산자를 이용해 깔끔하게 정리 
                continue;
            }

            if (i % 2 == mode) {
                answer.append(current);
            }
        }
        return answer.length() == 0 ? "EMPTY" : answer.toString();
    }
}