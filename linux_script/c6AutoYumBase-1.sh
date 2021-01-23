#!/bin/bash

echo -e "配置腾云的yum源\n"

yum install wget -y

echo "备份自带的yum源"
mkdir ~/yum-backup
mv /etc/yum.repos.d/*  ~/yum-backup

echo "下载tecent源"
wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.cloud.tencent.com/repo/centos6_base.repo

#报错修复
#sed -i 's#http#https#g' /etc/yum.repos.d/CentOS-Base.repo

echo "重建缓存"
yum clean all
yum makecache

