<?php include("common/checklogin.php"); ?>
<?php include("db/conn.php"); ?>

<?php 
// 1、如果没有传递ID过来，直接退回到classlist.php
if(empty($_GET["banjihao"])){
	exit("<script>alert('参数传递非法');location='classlist.php'</script>");
}
$banjihao=(int)$_GET["banjihao"]; // 接收上个页面传递过来的banjihao的值


// 2、判断此班是否有人
$sql="select * from student where ssbanji='{$banjihao}'";
$res=$pdo->query($sql);
if ($res && $res->rowCount()>0) {
	exit("<script>alert('{$banjihao}班有人，不能删除');location='classlist.php'</script>");
}


// 3、真正开始删除
$sql="delete from class where banjihao='{$banjihao}'";
$res=$pdo->query($sql);
if ($res && $res->rowCount()>0) {
	exit("<script>alert('删除成功');location='classlist.php'</script>");
} else {
	exit("<script>alert('删除失败，请检查参数');location='classlist.php'</script>");
}



?>
<!DOCTYPE html>
<html lang="zh-cn">
<head>
	<meta charset="UTF-8">
	<title>Document</title>
</head>
<body>
	
</body>
</html>