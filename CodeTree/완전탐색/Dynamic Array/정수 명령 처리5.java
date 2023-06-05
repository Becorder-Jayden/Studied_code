import java.util.Scanner;
import java.util.Arrays;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        
        ArrayList<Integer> arr = new ArrayList<>();

        for (int i=0; i<n; i++) {
            String order = sc.next();

            if (order.equals("push_back")) {
                int A = sc.nextInt();
                arr.add(A);
            } 
            
            // *pop(remove)할 때 마지막 인덱스 = arr.size()-1
            else if (order.equals("pop_back")) {  
                arr.remove(arr.size()-1);  // *
            } 

            else if (order.equals("size")) {
                System.out.println(arr.size());
            }     
            
            // *get할 때의 k번 째 인덱스 = arr.get(k-1);
            else if (order.equals("get")) {  
                int k = sc.nextInt();
                System.out.println(arr.get(k-1));  // *
            }
        }
    }
}
