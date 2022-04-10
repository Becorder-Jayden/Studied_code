package chapter7;

public class EnhancedForLoop {

	public static void main(String[] args) {
		String[] strArray = {"Java", "Android", "C", "JavaScript", "Python"};
		
		// 변수에 배열의 각 요소가 대입, 초기화와 종료 조건이 없기 때문에 모든 배열의 시작부터 끝 요소까지 실행
		for(String lang : strArray) {
			System.out.println(lang);
		}
	}
}
