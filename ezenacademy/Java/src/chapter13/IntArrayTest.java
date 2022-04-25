package chapter13;

import java.util.Arrays;

public class IntArrayTest {

	public static void main(String[] args) {
		int[] arr = {1,2,3,4,5};
		
		int sumVal = Arrays.stream(arr).sum();
		int count = (int)Arrays.stream(arr).count();
		// count() 메서드의 반환 값이 long이므로 int형으로 변환 필요
		
		System.out.println(sumVal);
		System.out.println(count);
	}

}
