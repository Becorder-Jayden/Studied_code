package chapter11;

public class ClassTest {

	// throws ClassNotFoundException : forName() 메서드에서 발생하는 예외를 처리함.
	// 이름과 일치하는 클래스가 없는 경우 ClassNotFoundException 발생
	public static void main(String[] args) throws ClassNotFoundException { 
		Person person = new Person();
		
		// Object의 getClass() 메서드 사용하기
		Class pClass1 = person.getClass();
		System.out.println(pClass1.getName());
		
		// 직접 class 파일 대입하기
		Class pClass2 = Person.class;
		System.out.println(pClass2.getName());
		
		// 클래스 이름으로 가져오기
		Class pClass3 = Class.forName("classex.Person");
		System.out.println(pClass3.getName());
	}

}
