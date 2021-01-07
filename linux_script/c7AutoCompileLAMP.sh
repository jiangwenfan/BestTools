#!/bin/bash
#将软件包下载到web服务器上，然后输入输入web服务器的地址，脚本会自动下载并解压，进行安装。

echo -e "使用源码编译安装LAMP环境 \n"

echo -e "编译的各版本号为：
httpd version：httpd-2.4.16
apr version：apr-1.5.2
pcre version：pcre-8.37
apr-util version：apr-util-1.5.4
mysql version：mysql-5.6.26
php version：php-5.6.13
"
echo "获取软件包的连接:"
echo -e "https://drive.google.com/drive/folders/1WCkMHWi3lxd2qCKzkyFrsnk1qHcNki8H?usp=sharing\n"

echo "输入源码获取的文件服务器："
read -e -p "" address

echo "安装基本所需工具及其依赖"
yum install wget

echo "正在获取编译所需的软件安装包"
address="http://"$address"/lampCompileSoftwarePackage.7z"
echo $address
wget address


#yum install 
echo "正在解压到当前目录"

