<?php include("common/checklogin.php"); ?>
<?php include("db/conn.php"); ?>

<?php 
// 查询数据
if (empty($_POST["xuehao"])) {
	$sql="select * from student";
} else {
	$abc=$_POST["xuehao"];
	$sql="select * from student where xuehao='{$abc}' order by id";
}


$res=$pdo->query($sql);
if ($res && $res->rowCount()>0) {
	$flag=1; // 表示有数据
}else{
	$flag=0; // 表示无数据
}


?>

<!DOCTYPE html>
<html lang="zh-cn">
<head>
	<meta charset="UTF-8">
	<title>学生列表</title>
	<style>
		table{
			border-collapse: collapse;
		}
		table td{
			line-height: 35px;
			text-align: center;
			border: 1px solid #ccc;
		}
	</style>
</head>
<body>

	<!-- 搜索 -->
	<form action="" method="post">
		<input type="text" name="xuehao" id="" placeholder="请输入学号">
		<input type="submit" value="搜 索">
	</form>


	<?php if($flag==0): ?>
	<table width="100%">
		<tr>
			<td>ID编号</td>
			<td>学号</td>
			<td>姓名</td>
			<td>性别</td>
			<td>年龄</td>
			<td>出生日期</td>
			<td>身份证号</td>
			<td>班级号</td>
			<td>身高/td>
			<td>地址</td>
			<td>删除</td>
			<td>修改</td>
		</tr>
		<tr>
			<td colspan="7">没有学生数据，请<a href='studentadd.php'>添加</a></td>
		</tr>
	</table>
	<?php else: ?>
	
	<table width="100%">
		<tr>
			<<td>ID编号</td>
			<td>学号</td>
			<td>姓名</td>
			<td>性别</td>
			<td>年龄</td>
			<td>出生日期</td>
			<td>身份证号</td>
			<td>班级号</td>
			<td>身高/td>
			<td>地址</td>
			<td>删除</td>
			<td>修改</td>
		</tr>
		<?php foreach($res as $row): ?>
		<tr>
			<td><?php echo $row["id"]; ?></td>
			<td><?php echo $row["xuehao"]; ?></td>
			<td><?php echo $row["xm"]; ?></td>
			<td><?php echo $row["xb"]; ?></td>
			<td><?php echo $row["age"]; ?></td>
			<td><?php echo $row["csrq"]; ?></td>
			<td><?php echo $row["sfzh"]; ?></td>
			<td><?php echo $row["ssbanji"]; ?></td>
			<td><?php echo $row["height"]; ?></td>
			<td><?php echo $row["address"]; ?></td>
			<td><a href="studentdel.php?xuehao=<?php echo $row["xuehao"]; ?>" onclick="return confirm('确定要删除吗？')">删除</a></td>
			<td><a href="studentedit.php?id=<?php echo $row["id"]; ?>">修改</a></td>
		</tr>
		<?php endforeach; ?>
	</table>
	
	<?php endif; ?>


</body>
</html>