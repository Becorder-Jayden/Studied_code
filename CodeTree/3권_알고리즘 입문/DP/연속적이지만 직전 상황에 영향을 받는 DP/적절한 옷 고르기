import java.util.Scanner;

public class Main {
    public static final int INT_MIN = Integer.MIN_VALUE;
    public static final int MAX_N = 200;
    public static final int MAX_M = 200; 

    public static int n, m;

    public static int[] s = new int[MAX_N +1]; 
    public static int[] e = new int[MAX_N +1]; 
    public static int[] v = new int[MAX_N +1]; 

    // dp[i][j]: i번째 날까지 입을 옷을 모두 결정하고, 마지막 날에 입은 옷이 j일 경우 얻을 수 있는 최대 만족도
    public static int[][] dp = new int[MAX_M+1][MAX_N+1];
    
    public static void init() {

        // 최댓값을 구하는 문제: 초기에는 모두 INT_MIN을 입력
        for (int d=1; d<=m; d++) {  // d: 날짜
            for (int i=1; i<=n; i++){  // i: 착장 아이템
                dp[d][i] = INT_MIN;
            }
        }

        // 첫째 날에 대한 정보
        for (int i=1; i<=n ;i++) {
            if (s[i] == 1) {
                dp[1][i] = 0;
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();  // 옷의 정보 개수
        m = sc.nextInt();  // 날짜

        for (int i=1; i<=n; i++) {
            s[i] = sc.nextInt();  // 입기 시작한 날짜
            e[i] = sc.nextInt();  // 입을 수 있는 마지막 날짜 
            v[i] = sc.nextInt();  // 옷의 화려함
        }

        init();

        for (int i=2; i<=m; i++) {  // 둘째날 부터 시작, *첫째날은 init()에서 입력
            for (int j=1; j<=n; j++) { 
                for (int k=1; k<=n; k++) {

                    // (i-1날에 k번 옷)을 입고, (i번째 날에 j번 옷)을 입은 경우 
                    //  i: 날짜, j: 이전에 선택한 옷 
                    //  k: 새롭게 선택할 옷 
                    if ( (s[k] <= i-1 && i-1 <= e[k]) && (s[j] <= i && i <= e[j]) ) {  // j, k가 범위안에 존재할 때
                        
                        // 크기 비교
                        //  1. dp[i][j]: i-1, i날에 동일한 옷(j)을 입었을 때
                        //  2. dp[i-1][k]: i-1날과 다르게(j) k옷을 입었을 때  
                        dp[i][j] = Math.max(dp[i][j], dp[i-1][k] + Math.abs(v[j] - v[k]));
                    }
                }
            }
        }

        // 정답 입력
        int ans = 0;
        for (int j=1; j<=n; j++) {
            ans = Math.max(ans, dp[m][j]);
        }

        System.out.println(ans);
    }
}