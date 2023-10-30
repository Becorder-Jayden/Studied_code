
class Solution {
    
    // lcm: 최소공배수
    public static int lcm(int a, int b) {
        return (a*b) / gcd(a, b);
    }
    
    // gcd: 최대공약수
    public static int gcd(int a, int b) {
        if (b == 0) {
            return a;
        }
        return gcd(b, a%b);
    }
    
    public int solution(int[] arr) {
        int answer = arr[0];
        
        for (int i=1; i<arr.length; i++) {
            arr[i] = lcm(answer, arr[i]);
            answer = arr[i];
        }
        
        return answer;
    }
}