package chapter8;

// Q. 클래스 오류가 왜 나는지 알 수 없음. 코드를 실행하지 못함.

import java.util.ArrayList;

// 상위 클래스 Animal
class Animal {
	public void move() {
		System.out.println("동물이 움직입니다.");
	}
}

// Animal을 상속받은 Human 클래스
class Human extends Animal{
	public void move() {
		System.out.println("사람이 두 발로 걷습니다.");
	}
	public void readBook() {
		System.out.println("사람이 책을 읽습니다.");
	}
}

// Animal을 상속받은 Tiger 클래스
class Tiger extends Animal{
	public void move() {
		System.out.println("호랑이가 네 발로 뜁니다.");
	}
	public void hunting() {
		System.out.println("호랑이가 사냥을 합니다.");
	}
}

// Animal을 상속받은 Eagle 클래스
class Eagle extends Animal{
	public void move() { 
		System.out.println("독수리가 하늘을 납니다.");
	}
	public void flying() {
		System.out.println("독수리가 날개를 쭉 펴고 날아갑니다.");
	}
}

public class AnimalTest {
	ArrayList<Animal> aniList = new ArrayList<Animal>();  // 배열의 자료형은 Animal로 지정
	
	public static void main(String args[]) {
		AnimalTest aTest = new AnimalTest();
		aTest.addAnimal();
		System.out.println("원래 형으로 다운 캐스팅");
		aTest.testCasting();
	}
	
	public void addAnimal() {
		// ArrayList에 추가되면서 Animal형으로 형 반환
		aniList.add(new Human());
		aniList.add(new Tiger());
		aniList.add(new Eagle());
		
		// 배열 요소를 Animal형으로 꺼내서 move()를 호출하면 재정의된 함수가 호출됨
		for(Animal ani : aniList) {
			ani.move();
		}
	}
	
	public void testCasting() {
		for(int i = 0; i < aniList.size(); i++) {
			Animal ani = aniList.get(i);
			if(ani instanceof Human) {
				Human h = (Human)ani;
				h.readBook();
			}
			else if(ani instanceof Tiger) {
				Tiger t = (Tiger)ani;
				t.hunting();
			}
			else if(ani instanceof Eagle) {
				Eagle e = (Eagle)ani;
				e.flying();
			}
			else {
				System.out.println("지원되지 않는 형입니다.");
			}
		}
	}
}
