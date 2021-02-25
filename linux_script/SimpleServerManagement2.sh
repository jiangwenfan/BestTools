#!/bin/bash

blue_font_prefix="\033[34m"
green_font_prefix="\033[32m"
font_color_suffix="\033[0m"
sequence1=1
sequence2=2
sequence3=3
line(){
  echo -e "\t${sequence1}.${blue_font_prefix}$1${font_color_suffix} \t\t\t${sequence2}.${blue_font_prefix}$2${font_color_suffix} \t\t${sequence3}.${blue_font_prefix}$3${font_color_suffix}"
	sequence1=$((${sequence1}+3))
	sequence2=$((${sequence2}+3))
	sequence3=$((${sequence3}+3))
}
log(){
	if [ $# == 0 ]
	then
		echo "-----------------------------------------------" >> log.txt
	else
		echo "[log:] $1" >> log.txt
	fi
}
install_http(){
	echo "installing http...."
	read -e -p "anonymous or user:" name

	echo "start install http"
	echo $name
	echo "............."
	echo "end install http"
	read $n
	main
}
install_tomcat(){
	echo "wait..."
}
install_mysql57(){
	log && log "install_mysql57:" 
	echo -e "start install mysql57...\n" 
	yum install yum-utils -y || log yum-utils 
	rpm -ivh https://dev.mysql.com/get/mysql80-community-release-el7-1.noarch.rpm || log "rpm -ivh"
	yum-config-manager --disable mysql80-community || log "yum-config-manager: disable"
	yum-config-manager --enable mysql57-community  || log "yum-config-manager:enable"
	yum -y install mysql-community-server mysql-community-client || log "install mysql-community"
	systemctl start mysqld ||log "systemctl"
	systemctl enable mysqld ||log "systemctl"
	clear
	echo -e "mysql临时密码：\n" 
	grep 'temporary password' /var/log/mysqld.log |cut -d":" -f 4  || log "password:"
	log 
}
yum_install(){
	log "yum----"
	rm -rf /etc/yum.repos.d/* || log "rm"
	wget http://mirrors.aliyun.com/repo/Centos-7.repo || log "wget"
	mv Centos-7.repo /etc/yum.repos.d/CentOS-Base.repo || log "mv"
	yum clean all || log "clean"
	yum makecache || log "makecache"
}
software_install(){
	yum install wget vim curl -y
	yum install gcc gcc-c++ java-1.8.0-opendjk-devel -y
}
openssh_config(){
	yum install -y openssh-server
	sed -i '38 s/#Per/Per/' /etc/ssh/sshd_config
	sed -i '17 s/#Po/Po/' /etc/ssh/sshd_config
	systemctl restart sshd
	systemctl enable sshd
}
python37_install(){
	log && log "python37:"
	mwget_install
	yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gcc make libffi-devel
	mwget https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tgz
	tar -zxvf Python-3.7.0.tgz
	cd Python-3.7.0
	./configure prefix=/usr/local/python3 
	make && make install
	ln -s /usr/local/python3/bin/python3.7 /usr/bin/python3
	ln -s /usr/local/python3/bin/pip3.7 /usr/bin/pip3	
	clear 
	python3 --version
	pip3 --version
}
php72_install(){

	yum -y install epel-release
	rpm -ivh https://mirror.webtatic.com/yum/el7/webtatic-release.rpm
	yum -y install mod_php72w php72w-cli php72w-devel
	yum -y install php72w-fpm php72w-common php72w-gd 
	yum -y install php72w-mbstring php72w-posix 
	yum -y install php72w-dom unzip php72w-pdo
	yum -y install php72w-pdo_mysql
	clear && php -version
}
static_ip(){
	sed -i 's/ONBOOT=no/ONBOOT=yes/' /etc/sysconfig/network-script/ifcfg-ens33
	sed -i 's/BOOTPROTO=dhcp/BOOTPROTO=static/' /etc/sysconfig/network-script/ifcfg-ens33 	
	read -e -p "IP地址" $ip
	read -e -p "gateway" $gateway
	read -e -p "dns" $dns
	echo "
		IPADDR=$ip
		NETMASK=255.255.255.0
		GATEWAY=$gateway
		DNS=$dns
	" >> /eyc/sysconfig/network-script/ifcfg-ens33
	systemctl restart network
}
mwget_install(){
	yum install bzip2 gcc gcc-c++ openssl-devel intltool wget -y 
	cd /usr/local/src 
        wget http://jaist.dl.sourceforge.net/project/kmphpfm/mwget/0.1/mwget_0.1.0.orig.tar.bz2
	tar -xjvf mwget_0.1.0.orig.tar.bz2
	cd mwget_0.1.0.orig
	./configure
	make 
	make install
	clear
	mwget
}
axel_install(){
	wget http://download-ib01.fedoraproject.org/pub/epel/7/x86_64/Packages/a/axel-2.4-9.el7.x86_64.rpm
	rpm -ivh axel-2.4-9.el7.x86_64.rpm
}
centos7_optimize(){
	log && log "centos7 optimize log:"
	echo "1.yum源配置"
	echo "2.常用软件安装"
	echo "3.ssh服务安装配置"
	echo "4.python3.7安装"
	echo "5.mwget安装"
	echo "6.axel安装"
	echo "7.php72安装"
	echo "8. 配置IP地址"
	read -e -p "input number:" nu
	case $nu in
		1) yum_install
		;;
		2) software_install
		;;
		3) openssh_config
		;;
		4) python37_install
		;;
		5) mwget_install
		;;
		6) axel_install
		;;
		7) php72_install	
		;;
		8) static_ip
		;;
		*) echo "invalid argu"
		;;
	esac
	read -p "回车完成安装" 
	main
}
main(){
sequence1=1
sequence2=2
sequence3=3
clear && echo -e "\n"
echo -e "\t\t\t\t\tcentos配置脚本\n"
line "install http " "install tomcat " "install nginx"
line "install vsftp" "install liteFtp" "install dns  "
line "install dhcp " "install mail   " "nstall apache"
line "ins  mysql5.7" "install mysql80" "install dvwa "
line "centos7优化  "   
echo "q键退出"
read -e -p "please input number:" num
case $num in
	1) install_http
	;;
	2) echo "install tomcat"
	;;
	10) install_mysql57
	;;
	13) centos7_optimize
	;;
	14) echo 0
	;;
	q) echo "退出" && exit
	;;
	*) echo "invalid number"
	;;	
esac
}
echo " " > log.txt
main
