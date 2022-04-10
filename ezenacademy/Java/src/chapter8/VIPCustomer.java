package chapter8;

public class VIPCustomer extends Customer {
	private int agentID;
	double saleRatio;

	public VIPCustomer(int customerID, String customerName, int agentID) {
		super(customerID, customerName);
		customerGrade = "VIP";
		bonusRatio = 0.05;
		saleRatio = 0.1;
		this.agentID = agentID;
//		System.out.println("VIPCustomer(int, String, int) 생성자 호출");
	}

	public VIPCustomer() {
		customerGrade = "VIP";  // customerGrade: 상위 클래스에서 선언한 customerGrade가 private 변수이기 때문에 오류 발생
		bonusRatio = 0.05;
		saleRatio = 0.1;
//		System.out.println("VIPCustomer() 생성자 호출 ");
	}

//	p.251 Override/Implement Methods ... 버튼이 보이지 않음 -> override를 수기로 작성했기 때문
//	@Override // 재정의된 메서드
//	public int calcPrice(int price) {
//		bonusPoint += price * bonusRatio;
//		return price - (int) (price * saleRatio);
//	}

	public int calcPrice(int price) {
		bonusPoint += price * bonusRatio;
		return price - (int)(price * saleRatio);
	}

	public String showCustomoerInfo() {
		return super.showCustomerInfo() + "담당 상담원 번호는 " + agentID + "입니다.";
	}
	
//	public String showCustomerInfo() {
//		return customerName + " 님의 등급은 " + customerGrade + "이며, 보너스 포인트는 " + bonusPoint + "입니다.";
//	}

	public int getAgentID() {
		return agentID;
	}
}
