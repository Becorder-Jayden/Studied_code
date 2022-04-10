package chapter11;

public class StringTest1 {

	public static void main(String[] args) {
		String str1 = new String("abc");
		String str2 = new String("abc");
		
		System.out.println(str1 == str2);
		System.out.println(str1.equals(str2));
		
		String str3 = "abc";
		String str4 = "abc";
		
		// 문자열 abc는 상수 풀에 저장되어 있으므로 str3와 str4가 가르키는 주소 값이 같음
		System.out.println(str3 == str4);
		System.out.println(str3.equals(str4));
	}

}
