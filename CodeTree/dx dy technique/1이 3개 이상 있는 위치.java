import java.util.Scanner;

public class Main {
    public static final int MAX_N = 100;  // N의 최대 범위
    public static final int DIR_NUM = 4;  // 탐색 방향 4

    // 사용할 변수 정의
    public static int n;  // 변수 n을 정의
    public static int[][] arr = new int[MAX_N][MAX_N];  // arr을 정의

    // 방향정의: 북동남서
    public static int[] dx = new int[]{0, 1, 0, -1};
    public static int[] dy = new int[]{1, 0, -1, 0};

    // 범위 체크 함수 inRange
    public static boolean inRange(int x, int y) {
        return (0 <= x && x < n && 0 <= y && y < n);
    }

    public static int adjacentCnt(int x, int y) {
        int cnt = 0;  // 숫자 세기
        
        // 4방향 탐색 진행
        for (int i=0; i < DIR_NUM; i++) {
            int nx = x + dx[i], ny = y + dy[i];  // 각 방향에 해당하는 nx, ny 정의
            
            // 범위 내 & 1일 경우 cnt + 1
            if (inRange(nx, ny) && arr[nx][ny] == 1) {  
                cnt++;
            }
        }
        
        return cnt;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        n = sc.nextInt();

        // 각 위치의 값 입력
        for (int i=0; i<n; i++) {
            for (int j=0; j<n; j++) {
                arr[i][j] = sc.nextInt();
            }
        }

        // 각 칸에 대해 탐색
        int ans = 0;
        for (int i=0; i<n; i++) {
            for (int j=0; j<n; j++) {
                if (adjacentCnt(i, j) >= 3) {
                    ans++; 
                }
            }
        }
        System.out.println(ans);
    }
}
