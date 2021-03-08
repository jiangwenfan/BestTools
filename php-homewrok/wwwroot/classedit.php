<?php include("common/checklogin.php"); ?>
<?php include("db/conn.php"); ?>
<?php 
if (empty($_GET["id"])) {
	exit("<script>alert('参数传递非法，滚!');location='classlist.php'</script>");
}
$id=(int)$_GET["id"];


// 通过ID查询当前班级
$sql="select * from class where id={$id}";
$res=$pdo->query($sql);
if ($res && $res->rowCount()>0) {
	$row=$res->fetch(); // 找到了这个班级，把这个班级取出来放到row变量中
	//print_r($row);
} else {
	exit("<script>alert('没有这个班级，请检查参数');location='classlist.php'</script>");
}

?>


<!DOCTYPE html>
<html lang="zh-cn">
<head>
	<meta charset="UTF-8">
	<title>修改班级</title>
	<!-- <link rel="stylesheet" href="css/reset.css"> -->
</head>
<body>
	<form action="" method="post">
		<div>
			<h3>修改班级</h3>
			<hr>
		</div>
		<div>
			<label for="">班级号：</label>
			<input type="text" name="banjihao" id="" value="<?php echo $row["banjihao"]; ?>">
		</div>
		<div>
			<label for="">专业：</label>
			<input type="text" name="zhuanye" id="" value="<?php echo $row["zhuanye"]; ?>">
		</div>
		<div>
			<label for="">所属院系：</label>
			<input type="text" name="ssxi" id="" value="<?php echo $row["ssxi"]; ?>">
		</div>
		<div>
			<label for="">相关介绍：</label>
			<textarea name="intro" id="" cols="30" rows="10"><?php echo $row["intro"]; ?></textarea>
		</div>
		<div>
			<input type="submit" value="修改班级">
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

	// 检测修改完成的班级是否在表中已经存在了
	$sql="select * from class where banjihao='{$banjihao}' and id<>{$id}";
	$res=$pdo->query($sql);
	if ($res && $res->rowCount()>0) {
		exit("<script>alert('{$banjihao}已经存在了');</script>");
	}

	// 开始修改啦(修改 class表)
	$sql="update class set banjihao='{$banjihao}',zhuanye='{$zhuanye}',ssxi='{$ssxi}',intro='{$intro}' where id={$id}";
	$res=$pdo->query($sql);
	if ($res && $res->rowCount()>0) {
		// 如果class表中的班级号修改了，还需要修改student表中的ssbanji
		$oldbanji=$row["banjihao"];
		$sql="update student set ssbanji='{$banjihao}' where ssbanji='{$oldbanji}'";
		$res=$pdo->query($sql);
		exit("<script>alert('修改成功！');location='classlist.php'</script>");
	} else {
		exit("<script>alert('没有修改任何内容!');location='classlist.php'</script>");
	}	

	
}
?>
