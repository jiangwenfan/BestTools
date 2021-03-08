<?php include("common/checklogin.php"); ?>
<!DOCTYPE html>
<html lang="zh-cn">
<head>
	<meta charset="UTF-8">
	<title>Document</title>
	<style>
		h2{
			text-align: center;
		}
		table{
			width: 100%;
			border-collapse: collapse;
		}
		table td{
			line-height: 35px;
			border: 1px solid #ccc;
			text-align: center;
		}
		footer{
			text-align: center;
			line-height: 50px;
			color: #666;
		}
	</style>
</head>
<body>
	<h2>学生管理系统功能介绍</h2>
	<table>
		<tr>
			<td>序号</td>
			<td>功能模块</td>
			<td>详细介绍</td>
		</tr>
		<tr>
			<td>1</td>
			<td>班级管理</td>
			<td>提供有班级的添加、删除、修改、查询等功能</td>
		</tr>
		<tr>
			<td>2</td>
			<td>学生管理</td>
			<td>提供有学生信息的添加、删除、修改、查询等功能</td>
		</tr>
		<tr>
			<td>3</td>
			<td>管理员管理</td>
			<td>提供对管理员的添加、删除、修改、查询等功能</td>
		</tr>
		<tr>
			<td>4</td>
			<td>系统登录和退出</td>
			<td>提供管理员登录和退出功能</td>
		</tr>
	</table>
	<footer>版权所有：贵州电子信息职业技术学院计算机科学系计算机网络技术21703班所有</footer>
</body>
</html>