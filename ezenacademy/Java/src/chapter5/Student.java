package chapter5;

public class Student {
	int studentID;
	private String studentName;
	int grade;
	String address;
	
	
	//	함수 반환형을 비워두어 오류가 발생하는 것을 방지하기 위해 비어있다라는 뜻의 void를 사용
	public void showStudentInfo() {
		System.out.println(studentName + ", " + address);
	}
	
	//	private 변수인 studentName에 접근해 값을 가져오는 public get() 메서드
	public String getStudentName() {
		return studentName;
	}

	// private 변수인 studentName에 접근해 값을 지정하는 public set() 메서드
	public void setStudentName(String studentName) {
		this.studentName = studentName;
	}
	
	public static void main(String[] args) {
		Student studentAhn = new Student();  // Student 클래스 생성
		studentAhn.studentName = "안연수";
		
		System.out.println(studentAhn.studentName);
		System.out.println(studentAhn.getStudentName());
	}
}