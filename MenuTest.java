import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class MenuTest extends JFrame { // ���� 14-2 �ڵ� ����
	// ��� ���� ����
    // �޴� ������
	JMenuItem openItem, saveItem, closeItem;
	JMenuItem colorItem, fontItem, textItem;
	JMenuItem versionItem;
	JLabel lblText; //��
	
	public MenuTest() {
		setTitle("�޴� �����");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		createMenu(); //�޴� ����
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
		fileMenu = new JMenu("����");
		openItem = new JMenuItem("����");
		openItem.addActionListener(new ActionListener(){
			public void actionPerformed(ActionEvent e) {
				int ret = fc.showOpenDialog(null);
				if(ret == JFileChooser.APPROVE_OPTION)
					lblText.setText(fc.getSelectedFile().getPath());
				//���� �б� : File IO
				// FileReader, FileInputStream�� Ȱ���ؼ� ������
				// ȭ�鿡 ���..
				
			}
		});
		saveItem = new JMenuItem("����");
		saveItem.addActionListener(new ActionListener(){
			public void actionPerformed(ActionEvent e) {
				int ret = fc.showSaveDialog(null);
				if(ret == JFileChooser.APPROVE_OPTION)
					lblText.setText(fc.getSelectedFile().getPath());
			}
		});
		closeItem = new JMenuItem("����");
		closeItem.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				int rs = JOptionPane.showConfirmDialog(null,"���� �����Ͻðڽ��ϱ�?","���� Ȯ��",JOptionPane.YES_NO_OPTION);
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
		editMenu = new JMenu("����");
		colorItem = new JMenuItem("�� ����");
		colorItem.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				Color c = JColorChooser.showDialog(null,"���� ����",Color.red);
				lblText.setForeground(c);
			}
		});
		fontItem =  new JMenuItem("��Ʈ");
		textItem = new JMenuItem("�ؽ�Ʈ ����");
		textItem.addActionListener(new ActionListener() {
		   public void actionPerformed(ActionEvent e) {
			   String text = JOptionPane.showInputDialog("������ �ؽ�Ʈ�� �Է��ϼ���");
			   if(text.length()!= 0) //��ĭ�� �ƴ϶��
				   lblText.setText(text);
		   }
		});
		editMenu.add(colorItem);
		editMenu.add(fontItem);
		editMenu.add(textItem);
		mb.add(editMenu);
		//helpMenu
		helpMenu = new JMenu("����");
		versionItem = new JMenuItem("���� ����");
		versionItem.addActionListener(new ActionListener() {
			   public void actionPerformed(ActionEvent e) {
				   JOptionPane.showMessageDialog(null, "�ؽ�Ʈ v1.0");
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
