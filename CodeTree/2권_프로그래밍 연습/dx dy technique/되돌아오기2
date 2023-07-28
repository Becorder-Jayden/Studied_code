import java.util.Scanner; 

public class Main {
    public static int DIR_NUM = 4; 
    
    // U, R, D, L
    public static int[] dx = new int[]{0, 1, 0, -1};
    public static int[] dy = new int[]{-1, 0, 1, 0};

    public static int dir = 0;
    public static int currX = 0;
    public static int currY = 0;
    public static int ans = -1;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String order = sc.next();
        int n = order.length();

        for (int i=0; i<n; i++) {
            char ord = order.charAt(i);
            if (ord == 'L') {
                dir = (dir + 3) % 4;
            } else if (ord == 'R') {
                dir = (dir + 1) % 4;
            } else {
                currX = currX + dx[dir];
                currY = currY + dy[dir];
                if (currX == 0 && currY == 0) {
                    ans = i + 1;
                    break;
                }
            }
        }
        System.out.println(ans);
    }
}