<?php require("db/conn.php"); ?>
<!DOCTYPE html>
<html lang="zh-cn">
<head>
	<meta charset="UTF-8">
	<title>学生管理系统V1.0</title>
	<link rel="stylesheet" href="css/reset.css">
	<link rel="stylesheet" href="css/index.css">
</head>
<body>
	<div class="login">
		<h2>学生管理系统后台入口</h2>
		<form action="" method="post">
			<div>
				<label for="">管理员账号：</label>
				<input type="text" name="user" id="">
			</div>
			<div>
				<label for="">管理员密码：</label>
				<input type="password" name="pass" id="">
			</div>
			<div>
				<input type="submit" value="登 录">
			</div>
		</form>
		<p class="intro">21703班全体同学制作2019.05.29</p>
	</div>
</body>
</html>
<?php 
// 判断用户所输入的账号和密码是否合法
if ($_POST) {
	$user=$_POST["user"];
	$pass=md5($_POST["pass"]);

	if($user=="" || $pass==""){
		exit("<script>alert('用户名和密码都不能为空!')</script>");
	}

	$sql="select * from admin where user='{$user}' and pass='{$pass}'";
	$res=$pdo->query($sql);

	if ($res && $res->rowCount()>0) { // 判断sql语句是否正确并且是否找到了某个管理员
		// 登录成功后把用户的账号和密码保存在session变量中
		session_start();
		$_SESSION["user"]=$user;
		$_SESSION["pass"]=$pass;
		header("location:admin.php");
	}else{
		exit("<script>alert('用户名或密码填写错误!')</script>");
	}
}


?>