import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {

        // 값 입력
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(bf.readLine());
        char[] numbers = bf.readLine().toCharArray();   // 문자열로 값을 저장
        int total = 0;  // 결과값을 저장할 변수

        for (int i = 0; i < N; i++) {
            // numbers라는 배열에서 각 요소를 문자열로 변환, 변환된 문자열을 정수로 변환해서 누적
            total += Integer.parseInt(String.valueOf(numbers[i]));

        }
        System.out.println(total);
    }
}