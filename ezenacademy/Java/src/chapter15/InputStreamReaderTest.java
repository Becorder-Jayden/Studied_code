package chapter15;

import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;

public class InputStreamReaderTest {

	public static void main(String[] args) {
		try(InputStreamReader isr = new InputStreamReader(new FileInputStream("reader.txt"))) { 		// 보조 스트림인 InputStreamReader의 매개 변수로 기반 스트림인 FileInputStrea을 받아 생성함
				
		int i;
		while((i=isr.read()) != -1) {
			System.out.println((char)i);
		}
		} catch (IOException e) {
			e.printStackTrace();
		}
	}	
}
