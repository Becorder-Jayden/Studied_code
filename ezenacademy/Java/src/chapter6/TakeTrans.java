package chapter6;

public class TakeTrans {
	public static void main(String[] args) {
//		Student.java 파일에서 public Student 값을 변경(초기화) 시켰기 때문에 오류 발생
		Student studentJames = new Student("James", 5000);
		Student studentTomas = new Student("Tomas", 10000);
		
		Bus bus100 = new Bus(100);
		studentJames.takeBus(bus100);
		studentJames.showInfo();
		bus100.showInfo();
		
		Subway subwayGreen = new Subway("2호선");
		studentTomas.takeSubway(subwayGreen);
		studentJames.showInfo();
		studentTomas.showInfo();
	}
}
