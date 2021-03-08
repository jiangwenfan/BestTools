<?php 
header("content-type:text/html;charset=utf-8");
$dsn="mysql:host=localhost;dbname=jiangfan";
$username="jiangfan";
$password="EC2E1BE7CE63c6";
$pdo=new PDO($dsn,$username,$password);
$pdo->exec("set names utf8");
?>