package chapter12;

import java.util.Comparator;
import java.util.Set;
import java.util.TreeSet;

class Mycompare implements Comparator<String>{
	@Override  // 내림차순 정렬
	public int compare(String s1, String s2) {
		return (s1.compareTo(s2)) * -1;
	}
}

public class ComparatorTest {
	
	public static void main(String[] args) {
		
		// TreeSet 생성자의 매개변수로 정렬 방식을 지정
		Set<String> set = new TreeSet<String>(new Mycompare());
		set.add("aaa");
		set.add("bbb");
		set.add("ccc");
		
		System.out.println(set);
	}

}
