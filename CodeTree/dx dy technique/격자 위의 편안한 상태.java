import java.util.Scanner; 

public class Main {
    public static int DIR_NUM = 4;
    
    public static int N, M;
    public static int[][] arr = new int[100][100];

    // U, R, D, L
    public static int[] dx = new int[]{0, 1, 0, -1};
    public static int[] dy = new int[]{-1, 0, 1, 0};

    // inRange
    public static boolean inRange(int x, int y) {
        return 0<=x && x<N && 0<=y && y<N;
    }


    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        M = sc.nextInt();

        // 색칠 진행
        while (M-- > 0) {
            int r = sc.nextInt();
            int c = sc.nextInt();

            r--; c--;

            arr[r][c] = 1;

            int colored = 0;
            for (int i=0; i<DIR_NUM; i++) {
                int nr = r + dx[i]; 
                int nc = c + dy[i];

                if (inRange(nr, nc) && arr[nr][nc] == 1) {
                    colored ++;
                }
            }

            int cozy = 0;
            if (colored == 3) {  // *정확히 3개여야 하는 조건 
                cozy = 1;
            }
            System.out.println(cozy);
        }
    }
}