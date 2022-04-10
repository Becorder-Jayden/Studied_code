package chapter9;

public abstract class NoteBook extends Computer{
// 추상 메서드 display와 typing 중 display만 구현했으므로 추상 클래스에 해당
	@Override
	public void display() {
		System.out.println("NoteBook display()");
	}
}
