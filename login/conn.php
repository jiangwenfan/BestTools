<?php   

   
//用于连接数据库
 $conn = mysql_connect("127.0.0.1","root","") or die("数据库链接错误".mysql_error());  

 mysql_select_db("info_db",$conn) or die("数据库访问错误".mysql_error());  

 mysql_query("set names gb2312");  

?>