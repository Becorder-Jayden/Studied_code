import java.util.Scanner;
import java.util.Arrays;

public class Main {
    public static int n;

    // cutArray: 해당 부분을 제외한 새로운 배열 생성
    public static int[] cutArray(int[] arr, int n, int s, int e) {
        int[] temp = new int[n];  // 새로운 배열을 임시로 저장할 temp 배열 
        int idx = 0;  // 조건에 해당할 때만 입력할 수 있도록 idx를 새로 정의
        
        for (int i=0; i<n; i++) {
            if (i<s-1 || i>e-1) {
                temp[idx++] = arr[i];  // 조건에 부합할 때만 idx를 증가시켜 값을 입력
            }
        }
        return temp;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        int[] arr = new int[n];
        for (int i=0; i<n; i++) {
            arr[i] = sc.nextInt();
        }

        // (s1, e1) 구간에 대해 잘라내기
        int s1 = sc.nextInt();
        int e1 = sc.nextInt();
        arr = cutArray(arr, n, s1, e1);  // arr을 잘라 만든 temp를 arr에 복사

        // (s2, e2) 구간에 대해 잘라내기
        int s2 = sc.nextInt();
        int e2 = sc.nextInt();
        arr = cutArray(arr, n, s2, e2);  // arr을 잘라 만든 temp를 arr에 복사

        int cnt = 0;
        for (int i=0; i<n; i++) {
            if (arr[i]>0) {
                cnt++;
            }
        }
        System.out.println(cnt);

        for (int i=0; i<n; i++) {
            if (arr[i]>0) {
                System.out.println(arr[i]);
            }
        }
    }
}