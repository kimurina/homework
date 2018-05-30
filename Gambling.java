import java.util.Scanner;

class Person{
	String name;
	
	public Person(String name) {
		this.name = name;
	}
	
	public void pause() {
	try {
		System.in.read();
		}
	catch(Exception e) {}
	}
}

public class Gambling {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		System.out.print("1번째 선수 이름>>");
		String i = scanner.next();
		System.out.print("2번째 선수 이름>>");
		String j = scanner.next();
		
		Person a = new Person(i);
		Person b = new Person(j);
		
		while(true) {
			System.out.print("["+a.name+"]:"+"<Enter>");
			a.pause();
			a.pause();
		    int n1 = (int)(Math.random()*3+1);
		    System.out.print("\t\t"+n1);
		    int n2 = (int)(Math.random()*3+1);
		    System.out.print("\t"+n2);
		    int n3 = (int)(Math.random()*3+1);
		    System.out.print("\t"+n3+"\t");
			if(n1!=n2 || n2!=n3 || n3!=n1)
				System.out.println("아쉽군요!");
			else if(n1==n2 && n2==n3) {
				System.out.println(a.name+"님이 이겼습니다!");
				break;
			}
		
			System.out.print("["+b.name+"]:"+"<Enter>");
			b.pause();
			b.pause();
			int m1 = (int)(Math.random()*3+1);
			System.out.print("\t\t"+m1);
			int m2 = (int)(Math.random()*3+1);
			System.out.print("\t"+m2);
			int m3 = (int)(Math.random()*3+1);
			System.out.print("\t"+m3+"\t");
			if(m1!=m2 || m2!=m3 || m3!=m1)
				System.out.println("아쉽군요!");
			else if(m1==m2 && m2==m3) {
				System.out.println(b.name+"님이 이겼습니다!");
				break;
			}
		}
		scanner.close();
	}
}



	
	
