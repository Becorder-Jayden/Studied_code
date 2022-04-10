package chapter2;

public class ExplicitConversion {

	public static void main(String[] args) {
		double dNum1 = 1.2;
		float fNum2 = 0.9F;
		
		// 강제로 형을 바꾸려면 바꿀 형을 괄호로 써서 명시
		int iNum3 = (int)dNum1 + (int)fNum2;  // 두 실수가 각각 형 변환되어 더해짐
		int iNum4 = (int)(dNum1 + fNum2);  // 두 실수의 합이 먼저 계산되고 형 변환
		System.out.println(iNum3);
		System.out.println(iNum4);  // 2.1이 int형으로 바뀌어 2 출력
	}

}
