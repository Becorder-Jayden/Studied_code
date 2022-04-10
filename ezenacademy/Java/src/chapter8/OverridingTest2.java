package chapter8;

public class OverridingTest2 {

//	묵시적 클래스 형 변환과 메서드 재정의
	public static void main(String[] args) {
		Customer vc = new VIPCustomer(10030, "나몰라", 2000);  // 하위클래스 newCustomer에 생성된 값을 상위 클래스 Customer 형태로 변수 저장
		vc.bonusPoint = 1000;	
		System.out.println(vc.getCustomerName() + " 님이 지불해야 하는 금액은 " + vc.calcPrice(10000)+ "원 입니다.");
		// 하위 클래스 VIPCustomer의 calcPrice() 메서드가 호출됨 : 가상메서드
	}
	

}
