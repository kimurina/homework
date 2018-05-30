<%@ page contentType="text/html; charset=UTF-8" %>
<%@ page import="java.sql.*" %>
<%
 	String dbdriver = "oracle.jdbc.driver.OracleDriver";
	Class.forName(dbdriver);
	Connection myConn = null;
	
	String dburl = "jdbc:oracle:thin:@localhost:1521:orcl";
	String user = "db";
	String passwd = "db";
	
	Statement stmt = null;
	String mySQL = null;
	ResultSet rs = null;
	
	String userID = request.getParameter("userID");
	String userPassword = request.getParameter("userPassword");
	String id = "";
	
	try{
		myConn = DriverManager.getConnection(dburl, user, passwd);
		stmt = myConn.createStatement();
	}
	catch(Exception e){
		System.out.println("에러발생");
	}
	mySQL = "select s_id from student where s_id='" + userID + "' and s_password='" + userPassword + "'";
	rs = stmt.executeQuery(mySQL);
	if(rs != null && rs.next()){
		id = rs.getString(1); //"s_id"
	}
	session.setAttribute("user", id); //이 id로 접근을 했다고 알려준다. jsp의 한 기능
	%>
		<script>
			alert("login success!");
			location.href("main.jsp");
		</script>
	<%	
	
	stmt.close();
	myConn.close();
%>
