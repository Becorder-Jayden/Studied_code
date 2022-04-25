package chapter12;

import java.util.ArrayList;

public class MemberArrayList {
	
	// ArrayList 선언
	private ArrayList<Member> arrayList;
	
	//Member형으로 선언한 ArrayList 생성
	public MemberArrayList() {
		arrayList = new ArrayList<Member>();
	}

	// Member형으로 성넌한 ArrayList 생성
	public void addMember(Member member) {
		arrayList.add(member);
	}
	
	// 해당 아이디를 가진 회원을 ArrayList에서 찾아 제거
	public boolean removeMember(int memberId) {
		for(int i = 0; i < arrayList.size(); i++) {
			// get() 매서드로 회원을 순차적으로 가져옴
			Member member = arrayList.get(i);
			int tempId = member.getMemberId();
			
			// 회원 아이디가 매개변수와 일치하면 해당 회원을 삭제
			if(tempId == memberId) {
				arrayList.remove(i);
				return true;
			}
		}
		// 반복문이 끝날 때까지 해당 아이디를 찾지 못한 경우
		System.out.println(memberId + "가 존재하지 않습니다.");
		return false;
	}
	
	// 전체 회원을 출력하는 메서드 
	public void showAllMember() {
		for(Member member : arrayList) {
			System.out.println(member);
		}
		System.out.println();
	}
}
