package chapter5;

public class StudentTest {

	public static void main(String[] args) {
		Student studentLee = new Student();
//		studentLee.studentName = "이상원";
				
//		setStudentName() 메서드를 활용해 private 변수에 접근이 가능		
		studentLee.setStudentName("이상원");
		
		System.out.println(studentLee.getStudentName());
	}

}
