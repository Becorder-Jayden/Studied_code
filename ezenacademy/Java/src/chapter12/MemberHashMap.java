package chapter12;

import java.util.HashMap;
import java.util.Iterator;

public class MemberHashMap {
	private HashMap<Integer, Member> hashMap;
	
	public MemberHashMap() {
		hashMap = new HashMap<Integer, Member>();
	}
	
	public void addMember(Member member) {
		hashMap.put(member.getMemberId(), member);  // key-value 쌍 추가
	}
	
	public boolean removeMember(int memberId) {
		// HashMap에 매개변수로 받은 키 값인 회원 아이디가 있다면 HashMap에서 회원을 삭제
		if(hashMap.containsKey(memberId)) {  
			hashMap.remove(memberId);
			return true;
		}
		System.out.println(memberId + "가 존재하지 않습니다.");
		return false;
	}
	
	public void showAllMember() {
		Iterator<Integer> ir = hashMap.keySet().iterator();
		while (ir.hasNext()) {  // 다음 key가 있으면
			int key = ir.next();  // key 값을 가져와서
			Member member = hashMap.get(key);
			System.out.println(member);
		}
		System.out.println();
	}
	
	
}
