package chapter13;

interface PrintString{
	void showString(String str);
}

public class TestLambda {
	public static void main(String[] args) {
		PrintString lambdaStr = s -> System.out.println(s);
		lambdaStr.showString("hello lambda_1");
		
		// 메서드의 매개변수로 람다식을 대입한 변수 전달
		showMyString(lambdaStr);

		PrintString reStr = returnString();
		reStr.showString("hello ");
	}
	
	// 매개변수를 인터페이스 형으로 받음
	public static void showMyString(PrintString p) {
		p.showString("hello labmda_2");
	}

	public static PrintString returnString() {
		return s -> System.out.println(s + "world");
	}
	
}
