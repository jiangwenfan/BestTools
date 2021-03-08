<?php include("common/checklogin.php"); ?>
<?php include("db/conn.php"); ?>

<!DOCTYPE html>
<html lang="zh-cn">
<head>
	<meta charset="UTF-8">
	<title>添加班级</title>
	<!-- <link rel="stylesheet" href="css/reset.css"> -->
</head>
<body>
	<form action="" method="post">
		<div>
			<h3>添加班级</h3>
			<hr>
		</div>
		<div>
			<label for="">班级号：</label>
			<input type="text" name="banjihao" id="">
		</div>
		<div>
			<label for="">专业：</label>
			<input type="text" name="zhuanye" id="">
		</div>
		<div>
			<label for="">所属院系：</label>
			<input type="text" name="ssxi" id="">
		</div>
		<div>
			<label for="">相关介绍：</label>
			<textarea name="intro" id="" cols="30" rows="10"></textarea>
		</div>
		<div>
			<input type="submit" value="添加班级">
		</div>
	</form>
</body>
</html>

<?php 
if ($_POST) {
	// 取出数据
	$banjihao=$_POST["banjihao"];
	$zhuanye=$_POST["zhuanye"];
	$ssxi=$_POST["ssxi"];
	$intro=$_POST["intro"];

	// 判断数据是否为空
	if ($banjihao=="" || $zhuanye=="" || $ssxi=="" || $intro=="") {
		exit("<script>alert('所有项目都不能为空！')</script>");
	}

	// 检测输入的班级号是否已经存在
	$sql="select * from class where banjihao='{$banjihao}'";
	$res=$pdo->query($sql);
	if ($res && $res->rowCount()>0) {
		exit("<script>alert('此班级号已经存在，请换一个!')</script>");
	}


	// 插入数据
	$sql="insert into class values(null,'{$banjihao}','{$zhuanye}','{$ssxi}','{$intro}')";
	$res=$pdo->query($sql);
	if ($res && $res->rowCount()>0) {
		exit("<script>alert('班级录入成功!');location='classlist.php'</script>");
	}else{
		exit("<script>alert('班级录入失败，请检查!')</script>");
	}
}
?>
