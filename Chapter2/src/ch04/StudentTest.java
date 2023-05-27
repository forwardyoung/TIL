package ch04;

public class StudentTest {

	public static void main(String[] args) {

		Student studentCha = new Student(); // studentCha는 참조변수 역할을 하며, 인스턴스이다.
		
		studentCha.studentID = 12345;
		studentCha.setStudentName("Cha");
		studentCha.address = "서울 강남구";
		
		studentCha.showStudentInfo();
		
		Student studentKim = new Student();
		studentKim.studentID = 54321;
		studentKim.studentName = "Kim";
		studentKim.address = "경기도 성남시";
		
		studentKim.showStudentInfo();
		System.out.println(studentKim);
		System.out.println(studentCha);
	}

}
