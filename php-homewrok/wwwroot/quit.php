<?php include("common/checklogin.php"); ?>
<?php 
@session_start();
$_SESSION=[];
session_destroy();
exit("<script>alert('谢谢再见');location='index.php'</script>");

?>