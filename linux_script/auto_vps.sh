#!/bin/bash
#centos7
echo "test" 1> /root/auto_vps.log

echo "install docker ...."
yum install docker-io -y 2>> /root/auto_vps.log  
systemctl start docker 2>> /root/auto_vps.log
systemctl enable docker 2>> /root/auto_vps.log

echo "install java jdk ...."
yum install java-1.8.0-openjdk-devel -y 2>> /root/auto_vps.log

echo "install gcc (asm or c or c++)... "
yum install gcc -y 2>> /root/auto_vps.log

echo "install system tools..."
yum install wget lrzsz -y 2>> /root/auto_vps.log

echo "install ftp server... from adlerED"
wget "https://github.com/AdlerED/LiteFTPD-UNIX/releases/download/v1.2/LiteFTPD-UNIX.jar" 2>> /root/auto_vps.log

echo "end" 1>> /root/auto_vps.log
