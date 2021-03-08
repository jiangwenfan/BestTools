<?php include("common/checklogin.php"); ?>
<?php include("db/conn.php"); ?>

<?php 
// 查询数据
if (empty($_POST["banjihao"])) {
	$sql="select * from class order by id desc";
} else {
	$abc=$_POST["banjihao"];
	$sql="select * from class where banjihao='{$abc}' order by id desc";
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
	<title>班级列表</title>
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
		<input type="text" name="banjihao" id="" placeholder="请输入班级号">
		<input type="submit" value="搜 索">
	</form>


	<?php if($flag==0): ?>
	<table width="100%">
		<tr>
			<td>ID编号</td>
			<td>班级号</td>
			<td>专业</td>
			<td>所属院系</td>
			<td>相关介绍</td>
			<td>删除</td>
			<td>修改</td>
		</tr>
		<tr>
			<td colspan="7">没有班级数据，请<a href='classadd.php'>添加</a></td>
		</tr>
	</table>
	<?php else: ?>
	
	<table width="100%">
		<tr>
			<td>ID编号</td>
			<td>班级号</td>
			<td>专业</td>
			<td>所属院系</td>
			<td>相关介绍</td>
			<td>删除</td>
			<td>修改</td>
		</tr>
		<?php foreach($res as $row): ?>
		<tr>
			<td><?php echo $row["id"]; ?></td>
			<td><?php echo $row["banjihao"]; ?></td>
			<td><?php echo $row["zhuanye"]; ?></td>
			<td><?php echo $row["ssxi"]; ?></td>
			<td><?php echo $row["intro"]; ?></td>
			<td><a href="classdel.php?banjihao=<?php echo $row["banjihao"]; ?>" onclick="return confirm('确定要删除吗？')">删除</a></td>
			<td><a href="classedit.php?id=<?php echo $row["id"]; ?>">修改</a></td>
		</tr>
		<?php endforeach; ?>
	</table>
	
	<?php endif; ?>


</body>
</html>