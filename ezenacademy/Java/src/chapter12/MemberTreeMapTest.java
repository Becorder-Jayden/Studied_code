package chapter12;

public class MemberTreeMapTest {

	public static void main(String[] args) {
		MemberTreeMap memberHashMap = new MemberTreeMap();
		
		Member memberPark = new Member(1003, "박서원");
		Member memberLee = new Member(1001, "이지원");
		Member memberSon = new Member(1002, "손민국");
		Member memberHong = new Member(1004, "홍길동");
		
		// 회원 아이디 순서와 상관없이 회원 추가
		memberHashMap.addMember(memberHong);
		memberHashMap.addMember(memberSon);
		memberHashMap.addMember(memberLee);
		memberHashMap.addMember(memberPark);
		memberHashMap.showAllMember();
		// TreeMap 구조로 인해 자동 정렬되어 출력
		
		memberHashMap.removeMember(1004);
		memberHashMap.showAllMember();
		
	}
}
