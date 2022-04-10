package chapter6;

// 학번 확인하기

public class StudentTest2 {
	public static void main(String[] args) {
		Student1 studentLee = new Student1();
		studentLee.setStudentName("이지원");
		System.out.println(studentLee.serialNum);
//		노란색 줄은 오류가 아니라 이 변수가 static 변수이므로 인스턴트 참조 변수가 아닌 클래스 이름으로 직접 참조하라는 뜻
		System.out.println(studentLee.studentName + " 학번:" + studentLee.studentID);
		
		Student1 studentSon = new Student1();
		studentSon.setStudentName("손수경");
		System.out.println(studentSon.serialNum);
		System.out.println(studentSon.studentName + " 학번:" + studentSon.studentID);
	}
}
