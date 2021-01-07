#!/bin/bash

echo -e "快速安装python3的 virtualenv虚拟环境\n"

echo "需要提前安装python3 及其 pip3"

echo "安装虚拟环境"
pip3 install virtualenv
echo "安装虚拟环境扩展包"
pip3 install virtualenvwrapper

echo "在当前用户的.bashrc中追加相关环境变量"
echo "
	export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
	export WORKON_HOME=$HOME/.virtualenvs  #python的安装路径
	source /usr/local/bin/virtualenvwrapper.sh 
" >> ~/.bashrc

echo "重载当前环境变量"
source ~/.bashrc

echo "安装完成。。。"

