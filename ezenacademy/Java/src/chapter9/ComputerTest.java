package chapter9;

public class ComputerTest {
	public static void main(String[] args) {
//		Computer c1 = new Computer();
		Computer c2 = new DeskTop();
//		Computer c3 = new NoteBook();
		Computer c4 = new MyNoteBook();
		// 추상클래스는 인스턴스로 생성할 수 없음: Computer와 NoteBook에서 오류 발생
	}

}
