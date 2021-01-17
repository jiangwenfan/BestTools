#!/bin/bash
#set git to github

echo "git config"
yum -y install git

echo "git"
name=`hostname`
git config --global user.name $name
git config --global user.name "zhan2103208467@163.com"
git config --global color.ui.auto 

echo "创建ssh-keygen"
ssh-keygen -t rsa -C "zhan2103208467@163.com"
echo "将公钥内容添加到github上"
cat /root/.ssh/id_rsa.pub
sleep 30
echo "进行测试连接"
echo "ssh -T git@github.com"
ssh -T git@github.com 
