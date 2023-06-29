import java.util.Scanner;

public class Main {
    public static final int MAX_LEN = 1000;

    public static String str1, str2;
    
    // dp[i][j]: 첫 번째 문자열의 i번째 문자열까지 고려, 두 번째 문자열의 j번째 문자까지 고려
    public static int[][] dp = new int[MAX_LEN+1][MAX_LEN+1]; 

    public static int str1Len, str2Len;
    
    // 점화식을 적용을 위한 기본 세팅
    public static void init() {
        
        // dp[1][1]: (첫 번째 문자열의 첫 번째 문자, 두 번째 문자열의 첫 번째 문자)가 같은지 여부 저장
        dp[1][1] = str1.charAt(1) == str2.charAt(1) ? 1 : 0;

        // 두 번째 문자열의 1번 인덱스 문자를 사용했을 때, 가능한 부분 수열의 최대 길이를 채워넣기
        for (int i=2; i<=str1Len; i++){
            if(str1.charAt(i) == str2.charAt(1)) {
                dp[i][1] = 1;
            }
            else {
                dp[i][1] = dp[i-1][1];
            }
        }

        // 첫번째 문자열의 1번 인덱스 문자를 사용했을 때, 가능한 부분 수열의 최대 길이 채워넣기
        for (int i=2; i<=str2Len; i++) {
            if (str1.charAt(1) == str2.charAt(i)) {
                dp[1][i] = 1;
            }
            else {  
                dp[1][i] = dp[1][i-1];
            }
        }

    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        str1 = sc.next();
        str2 = sc.next();

        str1Len = str1.length();
        str2Len = str2.length();

        // string의 index가 0부터 시작
        // 1부터 시작할 수 있도록 앞에 무의미한 '#'를 추가
        str1 = "#" + str1;
        str2 = "#" + str2;

        // 두 문자열의 1번 인덱스를 기준으로 판단했을 때
        init();

        // 첫 번째 문자열의 i번째 문자열까지 고려,
        // 두 번째 문자열의 j번째 문자열까지 고려했을 때
        // 가능한 부분수열의 최대 길이 구하기         
        for (int i=2; i<=str1Len; i++) {
            for (int j=2; j<=str2Len; j++) {
                
                // Case 1: i번째 문자와 j번째 문자가 일치할 경우
                //  첫 번째 문자열에서 i-1번째 문자까지 고려,
                //  두 번째 문자열에서 i-1번째 문자까지 고려했을 때
                //  가능한 공통 부분 수열 뒤에 문자 하나를 새롭게 추가 가능
                //  dp[i-1][j-1]+1 적용
                if (str1.charAt(i) == str2.charAt(j)) {
                    dp[i][j] = dp[i-1][j-1] + 1;
                }

                // Case 2: i번째 문자와 j번째 문자를 고려하지 않는 경우 중 더 큰 값 선택
                else {
                    dp[i][j] = Math.max(dp[i-1][j], dp[i][j-1]);
                }
            }
        }

        System.out.println(dp[str1Len][str2Len]);
    }
}