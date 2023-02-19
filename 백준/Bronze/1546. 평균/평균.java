import java.io.IOException;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {

        // 입력값 받기
        Scanner sc = new Scanner(System.in);    // Scanner : 입력 소스로부터 데이터를 읽어올 때 사용
        int N = sc.nextInt();   // 입력값의 개수
        int[] A = new int[N];   // N개 만큼 저장공간 생성

        // 저장공간에 값 입력
        for (int i = 0; i < N; i++) {
            A[i] = sc.nextInt();
        }

        // 변수 설정
        long sum = 0;
        long max = 0;

        for (int i = 0; i < N; i++) {
            // 저장공간의 값을 돌면서 더 큰값이 나오면 max 값 갱신
            if (A[i] > max) {
                max = A[i];
            }
            
            // 누적 합 입력
            sum = sum + A[i];
        }

        System.out.println(sum * 100.0 / max / N);

    }
}