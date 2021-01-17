#!/bin/bash

echo -e "自动快速安装lnmp的环境"

echo "安装yum拓展源,安装yum工具"
yum install epel-release -y
yum -y install yum-utils 
yum -y install elinks

# -------------
echo "安装nginx"
yum install nginx -y

nginx -v
sleep 5

systemctl start nginx
systemctl enable nginx

#------------------

echo -e "安装php7.2\n"
echo -e "安装含有php7.2版本的yum源\n"
rpm -ivh https://mirror.webtatic.com/yum/el7/webtatic-release.rpm
echo -e "安装php7.2相关的软件包\n"
yum -y install mod_php72w php72w-cli php72w-devel
yum -y install php72w-fpm php72w-common php72w-gd 
yum -y install php72w-mbstring php72w-posix 
yum -y install php72w-dom unzip php72w-pdo
yum -y install php72w-pdo_mysql

echo -e "重启httpd服务\n"
systemctl restart httpd

echo -e "写入php测试文件\n"
echo "<?php phpinfo(); ?>" > /var/www/html/index2.php

echo -e "查看php版本\n"
php -v
sleep 5

echo "测试访问:"
elinks http:127.0.0.1/index2.php

echo -e "安装mysql5.7\n"
echo -e "安装含有mysql5.7的yum源头\n"
rpm -ivh https://dev.mysql.com/get/mysql80-community-release-el7-1.noarch.rpm 
echo -e "关闭yum源中的80包，开启57包\n"
yum-config-manager --disable mysql80-community  
yum-config-manager --enable mysql57-community  
echo -e "开始安装服务端和客户端\n"
yum -y install mysql-community-server mysql-community-client 
echo -e "开启mysql服务\n"
systemctl start mysqld
echo -e "mysql服务设置为开启启动\n"
systemctl enable mysqld

echo -e "查看mysql默认密码\n"
grep 'temporary password' /var/log/mysqld.log 
sleep 5

echo -e "取消密码复杂度设置\n"
set global validate_password_policy=0;
set global validate_password_mixed_case_count=0;
set global validate_password_number_count=3;
set global validate_password_special_char_count=0;
set global validate_password_length=3;	

