package chapter13;


class Outer2 {
	Runnable getRunnable(int i) {
		int num = 100;
		
		// MyRunnable 클래스 이름을 빼고 클래스를 바로 생성하는 방법
		return new Runnable() {	// 익명 내부 클래스. Runnable 인터페이스 생성
			@Override
			public void run() {
				// 오류 발생
//				num = 200;
//				i = 10;
				System.out.println(i);
				System.out.println(num);
			}
		};
	}
	
	Runnable runner = new Runnable() {
		@Override
		public void run() {
			System.out.println("Runnable이 구현된 익명 클래스 변수");
		}
	};
}

public class AnonymousInnerTest {

	// 인터페이스나 추상 클래스형 변수를 선언하고 클래스를 생성해 대입하는 방법 
	public static void main(String[] args) {  // 익명 내부 클래스를 변수에 대입
		Outer2 out = new Outer2();
		Runnable runnerble = out.getRunnable(10);
		runnerble.run();
		out.runner.run();
	}

}
