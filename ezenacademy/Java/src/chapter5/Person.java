package chapter5;

public class Person {
	String name;
	float height;
	float weight;
	char gender;
	boolean married;
	
	public Person() {}
	
	public Person(String pname) {
		name = pname;
	}
	
	public Person(String pname, float pheight, float pweight) {
		name = pname;
		height = pheight;
		weight = pweight;
	}
}