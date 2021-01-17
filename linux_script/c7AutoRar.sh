#!/bin/bash

echo -e "快速编译安装rar压缩软件\n"

echo "从官网获取软件包"
wget "https://www.rarlab.com/rar/rarlinux-x64-5.9.1.tar.gz" && echo "获取成功ok!"

echo "解压到/usr/local"
tar zxvf rarlinux* -C /usr/local/

echo "设置环境变量"
ln -s /usr/local/rar/rar /usr/local/bin/rar   
ln -s /usr/local/rar/unrar /usr/local/bin/unrar

echo "rar压缩软件安装成功!"

rar
