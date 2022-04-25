package chapter12;

public class GenericPrinterTest {

	public static void main(String[] args) {
		GenericPrinter<Powder> powderPrinter = new GenericPrinter<Powder>();
		
		powderPrinter.setMaterial(new Powder());  // Powder형으로 GenericPrinter 클래스 생성
		Powder powder = powderPrinter.getMaterial();
		System.out.println(powder);
	
		GenericPrinter<Plastic> plasticPrinter = new GenericPrinter<Plastic>();
		
		plasticPrinter.setMaterial(new Plastic());  // Plastic형으로 GenericPrinter 클래스 생성
		Plastic plastic = plasticPrinter.getMaterial();
		System.out.println(plastic);
	}
}
