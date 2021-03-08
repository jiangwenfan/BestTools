<?php include("common/checklogin.php"); ?>
<?php include("db/conn.php"); ?>

<?php 
// 1、如果没有传递ID过来，直接退回到classlist.php
if(empty($_GET["xuehao"])){
	exit("<script>alert('参数传递非法');location='classlist.php'</script>");
}
$xuehao=(int)$_GET["xuehao"]; // 接收上个页面传递过来的xuehao的值


// 2、真正开始删除
$sql="delete from student where xuehao='{$xuehao}'";
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