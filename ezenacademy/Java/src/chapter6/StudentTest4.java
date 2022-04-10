package chapter6;

// 8행과 13행은 serialNum을 직접 참조하지 않고 getSerialNum() 메서드를 호출하여 참조

public class StudentTest4 {
	public static void main(String[] args) {
		Student2 studentLee = new Student2();
		studentLee.setStudentName("이지원");
		System.out.println(Student2.getSerialNum());
		System.out.println(studentLee.studentName + " 학번:" + studentLee.studentID);

		Student2 studentSon = new Student2();
		studentSon.setStudentName("손수경");
		System.out.println(Student2.getSerialNum());
		System.out.println(studentSon.studentName + " 학번:" + studentSon.studentID);
	}
}
