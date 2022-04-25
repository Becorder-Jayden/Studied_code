package chapter15;

import java.io.FileInputStream;
import java.io.IOException;

// 출력 결과가 의도와 조금 다른듯?
public class FileInputStreamTest3 {
	public static void main(String[] args) {
		try(FileInputStream fis = new FileInputStream("input2.txt")) {
			byte[] bs = new byte[10];
			int i;
			while ((i = fis.read(bs)) != -1) {
				for(byte b : bs) {
					System.out.println((char) b);
				}
				System.out.println(": " + i + "바이트 읽음");
			}
		} catch (IOException e) {
			e.printStackTrace();
		}
		System.out.println("end");
	} 
}
