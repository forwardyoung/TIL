package ch03;

public class FunctionTest {

	public static int addNum(int num1, int num2) { // 두 개의 매개변수를 받아 반환하는 함수
		
		int result;
		result = num1 + num2;
		return result;
	}

	public static void sayHello(String greeting) { // 반환값이 없는 함수
		
		System.out.println(greeting);
	}
	
	public static int calcSum()// 반환만 하고 매개변수가 없는 함수
	{
		
		int sum = 0;
		int i;
		
		for(i = 0; i<=100; i++) {
			
			sum += i;
		}
		return sum;
	}
	
	public static void main(String[] args) {
		
		int n1 = 10;
		int n2 = 20;
		
		int total = addNum(n1, n2);
		System.out.println(total);
		
		sayHello("안녕하세요");
		
		total = calcSum();
		System.out.println(total);
	}

}
