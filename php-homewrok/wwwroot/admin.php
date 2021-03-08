<?php include("common/checklogin.php"); ?>
<!DOCTYPE html>
<html lang="zh-cn">
<head>
	<meta charset="UTF-8">
	<title>后台管理</title>
	<link rel="stylesheet" href="css/reset.css">
	<link rel="stylesheet" href="css/admin.css">

</head>
<body>
	<div class="top">
		<h1>学生管理系统V1.0</h1>
	</div>
	<div class="left">
		<ul>
			<li><a href="#">班级管理</a>
				<ul>
					<li><a href="classadd.php" target="content">添加班级</a></li>
					<li><a href="classlist.php" target="content">班级列表</a></li>
				</ul>
			</li>
			<li><a href="#">学生管理</a>
				<ul>
					<li><a href="studentadd.php" target="content">添加学生</a></li>
					<li><a href="studentlist.php" target="content">学生列表</a></li>
				</ul>
			</li>
			<li><a href="#">管理员管理</a>
				<ul>
					<li><a href="adminadd.php" target="content">添加管理员</a></li>
					<li><a href="adminlist.php" target="content">管理员列表</a></li>
				</ul>
			</li>
			<li><a onclick="return confirm('确定要退出吗？')" href="quit.php">退出系统</a></li>
		</ul>
	</div>
	<div class="right">
		<iframe name="content" src="welcome.php" frameborder="0" width="100%" height="100%"></iframe>
	</div>
</body>
</html>