<?php 
// 检测管理员是否已经登录
header("content-type:text/html;charset=utf-8");
session_start();
if (empty($_SESSION["user"])) {
	exit("<script>alert('请先登录!');location='../index.php'</script>");
}
?>