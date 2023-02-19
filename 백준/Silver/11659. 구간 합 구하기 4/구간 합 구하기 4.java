import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        // 입력값 받기
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());    // ' '으로 띄어쓰기 된 값을 분리해서 읽기

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int[] S = new int[N + 1];   // S: 누적합 저장 공간
        StringBuilder sb = new StringBuilder();     // sb 결과값 출력 공간

        // S값 입력
        st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= N; i++) {
            S[0] = 0;
            S[i] = S[i - 1] + Integer.parseInt(st.nextToken());
        }

        // i, j 구간의 결과값 기록
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());

            // 구간합의 결과를 sb 객체에 저장, \n을 함께 저장해서 다음 줄에 출력되도록 함
            sb.append(S[end] - S[start - 1]).append("\n");  // start - 1: start 이전까지의 누적 값을 빼야 하기 때문
        }
        System.out.println(sb);
    }
}