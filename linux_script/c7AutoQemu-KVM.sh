#!/bin/bash

echo "quickly install kvm virtual"
#仅支持单网卡单ip
#仅支持prefix形式的掩码
#仅支持一个dns


yum install epel-release -y 

echo "安装一些必备的工具模块"
yum install qemu-kvm  #kvm主程序，kvm虚拟化模块

yum install	libvirt  #虚拟化服务

yum install	libguestfs-tools  #虚拟机系统管理工具

yum install	virt-install #安装虚拟机的实用工具。

yum install	virt-manager  #kvm图形化管理工具

yum install bridge-utils  #安装网桥br0

yum install	libvirt-python  #python调用libvirt虚拟化服务的api接口库文件。

systemctl start libvirtd  #启动服务 

systemctl enable libvirtd  #开机启动

echo "修改网络为桥接模式"
read -e -p "网卡名:" name
echo $name

echo "备份相关配置文件"
echo  /etc/sysconfig/network-scripts/ifcfg-$name  
cp  /etc/sysconfig/network-scripts/ifcfg-$name  /etc/sysconfig/network-scripts/ifcfg-$name-bakup

echo "获取网卡配置信息---！！！只针对于网卡的单地址"
ip=`cat /etc/sysconfig/network-scripts/ifcfg-$name |grep IPADDR |cut -d"=" -f2`
prefix=`cat /etc/sysconfig/network-scripts/ifcfg-$name |grep PREFIX |cut -d"=" -f2`
netmask=`cat /etc/sysconfig/network-scripts/ifcfg-$name |grep NETMASK |cut -d"=" -f2`
gateway=`cat /etc/sysconfig/network-scripts/ifcfg-$name |grep GATEWAY |cut -d"=" -f2`
dns1=`cat /etc/sysconfig/network-scripts/ifcfg-$name |grep DNS1 |cut -d"=" -f2`
dns2=`cat /etc/sysconfig/network-scripts/ifcfg-$name |grep DNS2 |cut -d"=" -f2`

echo "ip:" $ip 
echo "prefix:" $prefix 
echo "netmask:" $netmask 
echo "gate:" $gateway 
echo "dns1,2:" $dns1 $dns2


echo "修改网卡"$name"配置文件"
cp /etc/sysconfig/network-scripts/ifcfg-$name /etc/sysconfig/network-scripts/ifcfg-$name-tem #tem file

sed "s/IPADDR/#IPADDR/g" /etc/sysconfig/network-scripts/ifcfg-$name-tem > /etc/sysconfig/network-scripts/ifcfg-$name
cat /etc/sysconfig/network-scripts/ifcfg-$name > /etc/sysconfig/network-scripts/ifcfg-$name-tem
sed "s/NETMASK/#NETMASK/g" /etc/sysconfig/network-scripts/ifcfg-$name-tem > /etc/sysconfig/network-scripts/ifcfg-$name
cat /etc/sysconfig/network-scripts/ifcfg-$name > /etc/sysconfig/network-scripts/ifcfg-$name-tem
sed "s/PREFIX/#PREFIX/g" /etc/sysconfig/network-scripts/ifcfg-$name-tem > /etc/sysconfig/network-scripts/ifcfg-$name
cat /etc/sysconfig/network-scripts/ifcfg-$name > /etc/sysconfig/network-scripts/ifcfg-$name-tem
sed "s/GATEWAY/#GATEWAY/g" /etc/sysconfig/network-scripts/ifcfg-$name-tem > /etc/sysconfig/network-scripts/ifcfg-$name
cat /etc/sysconfig/network-scripts/ifcfg-$name > /etc/sysconfig/network-scripts/ifcfg-$name-tem
sed "s/DNS1/#DNS1/g" /etc/sysconfig/network-scripts/ifcfg-$name-tem > /etc/sysconfig/network-scripts/ifcfg-$name
cat /etc/sysconfig/network-scripts/ifcfg-$name > /etc/sysconfig/network-scripts/ifcfg-$name-tem
sed "s/DNS2/#DNS2/g" /etc/sysconfig/network-scripts/ifcfg-$name-tem > /etc/sysconfig/network-scripts/ifcfg-$name
echo 'BRIDGE="br0"' >> /etc/sysconfig/network-scripts/ifcfg-$name 
rm -rf /etc/sysconfig/network-scripts/ifcfg-$name-tem

cat /etc/sysconfig/network-scripts/ifcfg-$name

echo "生成桥设备配置文件"
echo "DEVICE="br0"  
NM_CONTROLLED="yes"   
ONBOOT="yes"  
TYPE="Bridge" 	
BOOTPROTO=none  
IPADDR=$ip   
PREFIX=$prefix
GATEWAY=$gateway
DNS1=$dns1
" > /etc/sysconfig/network-scripts/ifcfg-br0

cat /etc/sysconfig/network-scripts/ifcfg-br0

echo "重启网络"
systemclt restart network
