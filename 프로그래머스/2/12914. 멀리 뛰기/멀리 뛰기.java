class Solution {
    public long solution(int n) {
        long[] arr = new long[2001];
        arr[0] = 0;
        arr[1] = 1L;
        arr[2] = 2L;
        for (int i=3; i<=n; i++) {
            arr[i] = (arr[i-1]+arr[i-2]) % 1234567;
        }
        
        return arr[n];
    }
}


// class Solution {
//     public long solution(int n) {
//         long[] memo = new long[2001];
//         memo[1] = 1;
//         memo[2] = 2;

//         for (int i = 3; i <= n; i++) {
//             memo[i] = (memo[i - 1] + memo[i - 2]) % 1234567;
//         }

//         return memo[n];
//     }
// }