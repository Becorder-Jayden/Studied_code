import java.util.Scanner;

public class Main {
    public static final int INT_MAX = Integer.MAX_VALUE;
    public static final int MAX_N = 100;
    public static final int MAX_M = 10000;
    public static final int MAX_ANS = 10001;

    public static int n, m;

    public static int[] coin = new int[MAX_N + 1];
    public static int[] dp = new int[MAX_M + 1];

    public static void init() {

        // 구해야 하는 값이 최소값이므로 dp에는 최대값을 초기값으로 설정
        for (int i = 1; i <= m; i++) {
            dp[i] = MAX_ANS;
        }   
        
        // 0을 고르는 경우는 존재 하지 않으므로, 0으로 초기값 설정
        dp[0] = 0;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        n = sc.nextInt();
        m = sc.nextInt();
        for(int i = 1; i <= n; i++)
            coin[i] = sc.nextInt();

        init();

        // m = (1, m)의 범위 탐색
        for(int i = 1; i <= m; i++){

            // 모든 동전의 종류(coin[1], coin[n])에 대해 탐색 
            for(int j = 1; j <= n; j++) {
                
                // 탐색중인 m보다 동전의 크기가 작(거나 같)을 때 
                if(i >= coin[j]) {

                    // dp[i]: 기록된 거스름돈의 개수(dp[i])
                    // dp[i-coin[j]]: 동전의 종류에 따라 확인 가능한 이전 값
                    // ex) 동전의 종류가 1, 2, 4이고 현재 m = 5인 지점을 탐색
                    //      1, 2, 4는 5보다 작은 수
                    //      dp[5]의 값은 {dp[5-1]+1, dp[5-2]+1, dp[5-4]+1}에서 비교 
                    //      더 작은 값을 dp[i]의 값으로 선택
                    dp[i] = Math.min(dp[i], dp[i-coin[j]] + 1);  // *이해 중요
                }
            }
        }
        
        // 정답 도출
        int ans = dp[m];
        if (ans == MAX_ANS) {
            ans = -1; 
        }
        System.out.println(ans);
    }
}