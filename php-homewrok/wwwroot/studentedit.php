<?php include("common/checklogin.php"); ?>
<?php include("db/conn.php"); ?>
<?php 
$sql="select * from class order by banjihao";
$res22=$pdo->query($sql);

?>
<?php 
if (empty($_GET["id"])) {
	exit("<script>alert('参数传递非法，滚!');location='studentlist.php'</script>");
}
$id=(int)$_GET["id"];


// 通过ID查询当前学生
$sql="select * from student where id={$id}";
$res=$pdo->query($sql);
if ($res && $res->rowCount()>0) {
	$row=$res->fetch(); // 找到了这个学生，把这个学生取出来放到row变量中
	//print_r($row);
} else {
	exit("<script>alert('没有这个学生，请检查参数');location='studentlist.php'</script>");
}

?>


<!DOCTYPE html>
<html lang="zh-cn">
<head>
	<meta charset="UTF-8">
	<title>修改学生</title>
	<!-- <link rel="stylesheet" href="css/reset.css"> -->
</head>
<body>
	<form action="" method="post">
		<div>
			<h3>修改学生</h3>
			<hr>
		</div>
		<div>
			<label for="">学号：</label>
			<input type="text" name="xuehao" id="" value="<?php echo $row["xuehao"]; ?>">
		</div>
		<div>
			<label for="">姓名：</label>
			<input type="text" name="xm" id="" value="<?php echo $row["xm"]; ?>">
		</div>
		<div>
			<label for="">性别：</label>
			<?php
				$sex=$row["xb"]; 
				if ($sex == "男"){ ?>
					<input type="radio" name="xb" id="" value="男" checked="">男
					<input type="radio" name="xb" id="" value="女">女	
				<?php }else{ ?>
					<input type="radio" name="xb" id="" value="男" >男
					<input type="radio" name="xb" id="" value="女" checked="">女
				<?php }
				?>
			
		</div>
		<div>
			<label for="">年龄：</label>
			<input type="number" name="age" id="" value="<?php echo $row["age"]; ?>">
		</div>
		<div>
			<label for="">出生日期：</label>
			<input type="date" name="csrq" id="" value="<?php echo $row["csrq"]; ?>">
		</div>

		<div>
			<label for="">身份证号：</label>
			<input type="text" name="sfzh" id="" value="<?php echo $row["sfzh"]; ?>">
		</div>
		<div>
			<label for="">所属班级：</label>
		
			<select name="ssbanji" id="">
				<?php $old=$row["ssbanji"]; ?>
				<option selected value="<?php echo $old ?>"><?php echo $old ?></option>
				
				<?php foreach($res22 as $row22): ?>
				
				<option value="<?php echo $row22["banjihao"]; ?>"><?php echo $row22["banjihao"]; ?></option>
				<?php endforeach; ?>
			</select>
		</div>
		<div>
			<label for="">身高：</label>
			<input type="number" name="height" id="" value="<?php echo $row["height"]; ?>">
		</div>
		<div>
			<label for="">家庭地址：</label>
			<input type="text" name="address" id="" value="<?php echo $row["address"]; ?>">
		</div>

		<div>
			<input type="submit" value="修改学生">
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
	
	// 检测修改完成的学生是否在表中已经存在了
	$sql="select * from student where xuehao='{$xuehao}' and id<>{$id}";
	$res=$pdo->query($sql);
	if ($res && $res->rowCount()>0) {
		exit("<script>alert('{$xuehao}已经存在了');</script>");
	}

	// 开始修改啦(修改 student表)
	$sql99="update student set xuehao='{$xuehao}',xm='{$xm}',xb='{$xb}',age='{$age}',csrq='{$csrq}',sfzh='{$sfzh}',ssbanji='{$ssbanji}',height='{$height}',address='{$address}' where id={$id}";
	$res99=$pdo->query($sql99);	
	if ($res99 && $res99->rowCount()>0) {
		exit("<script>alert('修改成功！');location='studentlist.php'</script>");
	} else {
		echo "#########################错误##################";
		echo "$xuehao";
		echo "$xb";
		echo "<hr>";
		echo "$sfzh";
		echo "<hr>";
		echo "$ssbanji";
		echo "<hr>";
		echo "$sql99";
		
		
	}	

}
?>
