package chapter11;

public class StringEquals {
	public static void main(String[] args) {
		String str1 = new String("abc");
		String str2 = new String("abc");
		
		// 두 인스턴스 주소 값이 같은지 비교하여 출력
		System.out.println(str1 == str2);
		
		// 두 인스턴스 문자열 값이 같은지 비교하여 출력
		System.out.println(str1.equals(str2));
		
		Integer i1 = new Integer(100);		
		Integer i2 = new Integer(100);
		
		// 두 인스턴스 주소 값이 같은지 비교하여 출력
		System.out.println(i1 == i2);

		// 두 인스턴스 정수 값이 같은지 비교하여 출력
		System.out.println(i1.equals(i2));
	}
}
