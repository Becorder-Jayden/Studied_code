package chapter9;

public class Constant {
	int num = 10;
	final int NUM = 100;
	
	public static void Main(String[] args) {
		Constant cons = new Constant();
		cons.num = 50;
		cons.NUM2 = 200;
		// 변수 이름은 대소문자를 구분하기 떄문에 두 변수는 다른 변수이다.
		
		System.out.println(cons.num);
		System.out.println(cons.NUM);
	}
}
