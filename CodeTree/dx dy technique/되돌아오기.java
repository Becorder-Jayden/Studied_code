import java.util.Scanner;

public class Main {
    public static final int DIR_NUM = 4;
    
    public static int n, x, y;
    
    // U, R, D, L
    public static int[] dx = new int[]{0, 1,  0, -1};
    public static int[] dy = new int[]{-1,  0, 1, 0};
    
    // 답을 저장
    public static int ans = -1;
    
    // 걸린 시간
    public static int time;
    
    // dir 방향으로 dist 만큼 이동, 시작지에 도착하면 true
    public static boolean move(int dir, int dist) {
        while(dist-- > 0) {
            x += dx[dir];
            y += dy[dir];
            
            // 이동한 시간을 기록합니다.
            time++;
    
            // 시작지로 다시 돌아오면,
            // 답을 갱신해줍니다.
            if(x == 0 && y == 0) {
                ans = time;
                return true;
            }
        }
        
        return false;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        
        while(n-- > 0) {
            char cDir = sc.next().charAt(0);
            int dist = sc.nextInt();
            
            int dir;
            if(cDir == 'N')
                dir = 0;
            else if(cDir == 'E')
                dir = 1;
            else if(cDir == 'S')
                dir = 2;
            else
                dir = 3;
            
            // 주어진 dir에 따라 dist만큼 이동
            boolean done = move(dir, dist);
            
            // 시작위치에 도착했을 때, 종료
            if(done)
                break;
        }
        
        System.out.print(ans);
    }
}