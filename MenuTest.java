import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class MenuTest extends JFrame { // 에제 14-2 코드 참고
	// 멤버 변수 선언
    // 메뉴 아이템
	JMenuItem openItem, saveItem, closeItem;
	JMenuItem colorItem, fontItem, textItem;
	JMenuItem versionItem;
	JLabel lblText; //라벨
	
	public MenuTest() {
		setTitle("메뉴 만들기");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		createMenu(); //메뉴 생성
		Container c = getContentPane();
		c.setLayout(new FlowLayout());
		lblText = new JLabel("text");
		c.add(lblText);
		setSize(300,200);
		setVisible(true);
		}
	void createMenu() {
		JMenuBar mb = new JMenuBar();
		JMenu fileMenu, editMenu, helpMenu;
		JFileChooser fc = new JFileChooser();
		//fileMenu
		fileMenu = new JMenu("파일");
		openItem = new JMenuItem("열기");
		openItem.addActionListener(new ActionListener(){
			public void actionPerformed(ActionEvent e) {
				int ret = fc.showOpenDialog(null);
				if(ret == JFileChooser.APPROVE_OPTION)
					lblText.setText(fc.getSelectedFile().getPath());
				//파일 읽기 : File IO
				// FileReader, FileInputStream을 활용해서 내용을
				// 화면에 출력..
				
			}
		});
		saveItem = new JMenuItem("저장");
		saveItem.addActionListener(new ActionListener(){
			public void actionPerformed(ActionEvent e) {
				int ret = fc.showSaveDialog(null);
				if(ret == JFileChooser.APPROVE_OPTION)
					lblText.setText(fc.getSelectedFile().getPath());
			}
		});
		closeItem = new JMenuItem("종료");
		closeItem.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				int rs = JOptionPane.showConfirmDialog(null,"정말 종료하시겠습니까?","종료 확인",JOptionPane.YES_NO_OPTION);
				if(rs == JOptionPane.YES_OPTION)
					System.exit(0);
				}
			});
		fileMenu.add(openItem);
		fileMenu.add(saveItem);
		fileMenu.addSeparator();
		fileMenu.add(closeItem);
		mb.add(fileMenu);
		//editMenu
		editMenu = new JMenu("편집");
		colorItem = new JMenuItem("색 선택");
		colorItem.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				Color c = JColorChooser.showDialog(null,"색상 선택",Color.red);
				lblText.setForeground(c);
			}
		});
		fontItem =  new JMenuItem("폰트");
		textItem = new JMenuItem("텍스트 변경");
		textItem.addActionListener(new ActionListener() {
		   public void actionPerformed(ActionEvent e) {
			   String text = JOptionPane.showInputDialog("변경할 텍스트를 입력하세요");
			   if(text.length()!= 0) //빈칸이 아니라면
				   lblText.setText(text);
		   }
		});
		editMenu.add(colorItem);
		editMenu.add(fontItem);
		editMenu.add(textItem);
		mb.add(editMenu);
		//helpMenu
		helpMenu = new JMenu("도움말");
		versionItem = new JMenuItem("버전 정보");
		versionItem.addActionListener(new ActionListener() {
			   public void actionPerformed(ActionEvent e) {
				   JOptionPane.showMessageDialog(null, "텍스트 v1.0");
			   }
		});
		helpMenu.add(versionItem);
		mb.add(helpMenu);
		
		setJMenuBar(mb);
	}
	public static void main(String[] args) {
		new MenuTest();

	}

}
