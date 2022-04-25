package chapter12;


public class MemberTreeSetTest {
	public static void main(String[] args) {
		MemberTreeSet memberTreeSet = new MemberTreeSet();
		
		Member memberPark = new Member(1003, "박서원");
		Member memberLee = new Member(1001, "이지원");
		Member memberSon = new Member(1002, "손민국");
		
		memberTreeSet.addMember(memberLee);
		memberTreeSet.addMember(memberSon);
		memberTreeSet.addMember(memberPark);
		memberTreeSet.showAllMember();
		
		Member memberHong = new Member(1003, "홍길동");
		memberTreeSet.addMember(memberHong);
		memberTreeSet.showAllMember();
	}

}

// 실행 시 오류 발생
// Exception in thread "main" java.lang.ClassCastException: class chapter12.Member cannot be cast to class java.lang.Comparable (chapter12.Member is in unnamed module of loader 'app'; java.lang.Comparable is in module java.base of loader 'bootstrap')
// Member 클래스가 Comparable 인터페이스를 구현하지 않았다는 의미

// 막혀서 다음 단계 못감 ㅜ