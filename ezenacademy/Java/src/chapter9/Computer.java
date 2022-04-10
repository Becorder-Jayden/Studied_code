package chapter9;

// 추상 메서드가 속한 클래스는 추상 클래스로 선언해야 한다
public abstract class Computer {
	
	// 추상클래스 display()와 typing()은 하위 메서드에 따라 구현이 달라진다. 두 메서드 구현에 대한 책임을 상속받는 클래스에 위임한다는 의미
	public abstract void display(); 
	public abstract void typing(); 
	public void turnOn() {
		System.out.println("전원을 켭니다.");
	}
	public void turnOff() {
		System.out.println("전원을 끕니다.");
	}
}
