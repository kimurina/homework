import java.util.*;
import java.io.*;

class Movie implements Serializable {
	String title, director, genre;
	int year;
	
	public Movie(String title, String director, String genre, int year) {
		this.title = title;
		this.director = director;
		this.genre = genre;
		this.year = year;
	}
	public void SetTitle(String title) {
		this.title = title;
	}
	public String GetTitle() {
		return title;
	}
	public void SetDirector(String director) {
		this.director = director;
	}
	public String GetDirector() {
		return director;
	}
	public void SetGenre(String genre) {
		this.genre = genre;
	}
	public String GetGenre() {
		return genre;
	}
	public void SetYear(int year) {
		this.year = year;
	}
	public int GetYear() {
		return year;
	}
}

public class MovieTest {
	HashMap<String, Movie> dept = new HashMap<String, Movie>();
	Scanner scanner = new Scanner(System.in);

	public void input() {
		System.out.print("����:");
		String title = scanner.nextLine();
		
		System.out.print("����:");
		String director = scanner.nextLine();
	
	    System.out.print("�帣:");
		String genre = scanner.nextLine();
	
	    System.out.print("�⵵:");
		int year = scanner.nextInt();
		scanner.nextLine();
			
		Movie A = new Movie(title, director, genre, year);
		
		if(dept.containsKey(title)) 
			System.out.println(title+"�� �̹� �ִ� ��ȭ�Դϴ�.");
		
		else 
			dept.put(title,A);
		}
	
	public void output() {
		Set<String>keys = dept.keySet();
		Iterator<String>it = keys.iterator();
		
		while(it.hasNext()) {
			String title = it.next();
			Movie A = dept.get(title);
			
			System.out.println("[����:"+A.GetTitle()+", ����:"+A.GetDirector()+", �帣:"+A.GetGenre()+", �����⵵:"+A.GetYear()+"]");
			}
		}
	
	public void search() {
		System.out.print("�˻� ���� �Է�:");
		String title = scanner.nextLine();
		Movie A = dept.get(title);
		if(A == null)
			System.out.println(title+"�� ���� ��ȭ�Դϴ�.");
		else
			System.out.println("[����:"+A.GetTitle()+", ����:"+A.GetDirector()+", �帣:"+A.GetGenre()+", �����⵵:"+A.GetYear()+"]");
		}
	
	public void filewrite() throws IOException {
		File file = new File("movie.dat");
		FileOutputStream f = new FileOutputStream(file);
		ObjectOutputStream s = new ObjectOutputStream(f);
		s.writeObject(dept);
		s.flush();
		System.out.println("movie.dat�� ����Ǿ����ϴ�.");
		}
	
	public void fileread() throws IOException, ClassNotFoundException{
		File file = new File("movie.dat");
		FileInputStream f = new FileInputStream(file);
		ObjectInputStream s = new ObjectInputStream(f);
		dept = (HashMap<String, Movie>)s.readObject();
		s.close();
		System.out.println("movie.dat�κ��� ������ �ҷ��Խ��ϴ�.");
	}
	
	public static void main(String[] args) throws IOException, ClassNotFoundException {
		Scanner scanner = new Scanner(System.in);
		MovieTest t = new MovieTest();
		
		while(true) {
			System.out.print("1.��ȭ �Է�/");
			System.out.print("2.��ȭ ���/");
			System.out.print("3.��ȭ �˻�/");
			System.out.print("4.���� ����/");
			System.out.print("5.���� ����/");
			System.out.println("6.����");
			System.out.print("�޴��Է�>>");
			int menu = scanner.nextInt();
			
			switch(menu) {
			      case 1 : t.input(); break;
			      case 2 : t.output(); break;
 			      case 3 : t.search(); break;
			      case 4 : t.filewrite(); break;
			      case 5 : t.fileread(); break;
			      case 6 : return;
			}
		}
	}
}
	


