package chapter13;

class OutClass {
	private int num = 10;
	private static int sNum = 20;

	static class InStaticClass{
		int inNum = 100;
		static int sInNum = 200;
		
		// 정적 내부 클래스의 일반 메서드
		void inTest() {
			// num += 10;  // 외부 클래스의 인스턴스 변수는 사용할 수 없음
			System.out.println("OutClass num = " + inNum + "(외부 클래스의 인스턴스 변수)");
			System.out.println("OutClass sNum = " + sInNum + "(외부 클래스의 정적 변수");
			System.out.println("OutClass sNum = " + sNum + "(외부 클래스의 정적 변수 사용)");
		}
		
		// 정적 내부 클래스의 정적 메서드
		static void sTest() {
			// num += 10;
			// inNum += 10;
			System.out.println("OutClass sNum = " + sNum + "(외부 클래스의 정적 변수 사용)");
			System.out.println("InStaticClass sInNum = " + sInNum + "");
		}
	}
}

public class InnerTest {
	public static void main(String[] args) {
//		OutClass outClass = new OutClass();
//		System.out.println("외부 클래스 이용하여 내부 클래스 기능 호출");

		// 외부 클래스를 생성하지 않고 바로 정적 내부 클래스 생성 가능
		OutClass.InStaticClass sInClass = new OutClass.InStaticClass();
		System.out.println("정적 내부 클래스 일반 메서드 호출");
		sInClass.inTest();
		
		System.out.println();
		System.out.println("정적 내부 클래스의 정적 메서드 호출");
		OutClass.InStaticClass.sTest();
	}
}
