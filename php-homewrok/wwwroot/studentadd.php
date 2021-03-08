<?php include("common/checklogin.php"); ?>
<?php include("db/conn.php"); ?>
<?php 
$sql="select * from class order by banjihao";
$res=$pdo->query($sql);

 ?>

<!DOCTYPE html>
<html lang="zh-cn">
<head>
	<meta charset="UTF-8">
	<title>添加学生</title>
	<!-- <link rel="stylesheet" href="css/reset.css"> -->
</head>
<body>
	<form action="" method="post">
		<div>
			<h3>添加学生</h3>
			<hr>
		</div>
		<div>
			<label for="">学号：</label>
			<input type="text" name="xuehao" id="">
		</div>
		<div>
			<label for="">姓名：</label>
			<input type="text" name="xm" id="">
		</div>
		<div>
			<label for="">性别：</label>
			<input type="radio" name="xb" id="" value="男" checked="">男
			<input type="radio" name="xb" id="" value="女">女
		</div>
		<div>
			<label for="">年龄：</label>
			<input type="number" name="age" id="">
		</div>
		<div>
			<label for="">出生日期：</label>
			<input type="date" name="csrq" id="">
		</div>

		<div>
			<label for="">身份证号：</label>
			<input type="text" name="sfzh" id="">
		</div>
		<div>
			<label for="">所属班级：</label>
			<select name="ssbanji" id="">
				<option value="">=请选择=</option>

				<?php foreach($res as $row): ?>
				<option value="<?php echo $row["banjihao"]; ?>"><?php echo $row["banjihao"]; ?></option>
				<?php endforeach; ?>

			</select>
		</div>
		<div>
			<label for="">身高：</label>
			<input type="number" name="height" id="" step="0.01">
		</div>
		<div>
			<label for="">家庭地址：</label>
			<input type="text" name="address" id="">
		</div>

		<div>
			<input type="submit" value="添加学生">
		</div>
	</form>
</body>
</html>

<?php 
if ($_POST) {
	// 取出数据
	$xuehao=$_POST["xuehao"];
	$xm=$_POST["xm"];
	$xb=$_POST["xb"];
	$age=$_POST["age"];
	$csrq=$_POST["csrq"];
	$sfzh=$_POST["sfzh"];
	$ssbanji=$_POST["ssbanji"];
	$height=$_POST["height"];
	$address=$_POST["address"];
	// 判断数据是否为空
	if ($xuehao=="" || $xm=="" || $xb=="" || $age=="") {
		exit("<script>alert('所有项目都不能为空！')</script>");
	}

	// 检测输入的学号是否已经存在
	$sql="select * from student where xuehao='{$xuehao}'";
	$res=$pdo->query($sql);
	if ($res && $res->rowCount()>0) {
		exit("<script>alert('此学号已经存在，请换一个!')</script>");
	}


	// 插入数据
	$sql="insert into student values(null,'{$xuehao}','{$xm}','{$xb}','{$age}','{$csrq}','{$sfzh}','{$ssbanji}','{$height}','{$address}')";
	$res=$pdo->query($sql);
	if ($res && $res->rowCount()>0) {
		exit("<script>alert('学生录入成功!');location='classlist.php'</script>");
	}else{
		exit("<script>alert('学生录入失败，请检查!')</script>");
	}
}
?>
