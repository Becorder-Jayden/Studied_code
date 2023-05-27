import java.util.Scanner;

public class Main {
    public static int MAX_NUM = 100;  // 최대 범위 지정 
    public static int DIR_NUM = 4;  // 탐색 방향: 4

    public static int n, m;
    public static int[][] arr = new int[MAX_NUM][MAX_NUM];  // arr 크기 설정

    // dx, dy 정의: R, D, L, U  *dx가 dcol, dy가 drow에 해당
    public static int[] dx = new int[]{0, 1, 0, -1};
    public static int[] dy = new int[]{1, 0, -1, 0};

    public static int currX = 0, currY = 0;  // 현재위치: 시작 위치 (0, 0)
    public static int dir = 0;  // 방향(R, D, L, U)

    public static boolean inRange(int x, int y) {
        return 0 <= x && x < n && 0 <= y && y < m;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();

        // 시작 위치에 초기값을 입력
        arr[currX][currY] = 1;
        
        // 시작 값을 제외한 나머지 탐색 진행, 범위에 주의할 것
        for (int i=2; i<=n*m; i++) {
            
            // 현재 dir을 기준으로 다음 위치 값 계산
            int nextX = currX + dx[dir], nextY = currY + dy[dir];

            // 더 이상 나가갈 수 없을 때, 시계방향 회전
            if (!inRange(nextX, nextY) || arr[nextX][nextY] != 0) {
                dir = (dir+1) % 4;
            }

            // 다음 위치로 이동해서 올바른 값을 입력
            currX = currX + dx[dir]; currY = currY + dy[dir];
            arr[currX][currY] = i;
        }

        // 출력
        for (int i=0; i<n; i++) {
            for (int j=0; j<m; j++) {
                System.out.print(arr[i][j] + " ");
            }
            System.out.println();
        }
    }
}