#!/bin/bash
#version 1.0
echo "gcc install script..." && echo

if [ $# == 2 ];
then
	echo "start install gcc ..."
	#centos7
	if [ $1 == "c7" ];
	then	
		echo "centos7 log---------------" >> error.log
		if [ $2 == "old" ];
		then	
			echo "centos7 old log:" >> error.log
			yum install gcc gcc-c++ -y 2>> error.log 
		elif [ $2 == "new" ];
		then
			echo "centos7 new log:" >> error.log
			./1.sh c7 old
			cd /usr/local/src 
			wget http://ftp.mirrorservice.org/sites/sourceware.org/pub/gcc/releases/gcc-7.3.0/gcc-7.3.0.tar.gz
			tar zxvf gcc-7.3.0.tar.gz #zxf
			cd gcc-7.3.0
			yum -y install bzip2
			echo "下载组件，预计需要几分钟..."
			./contrib/download_prerequisites
			./configure --disable-multilib --enable-languages=c,c++
			echo "编译...预计需要几个小时"
			make -j 4
			make install
			clear
			gcc --version
		else
			echo "The first parameter is invalid..."
		fi
	elif [ $1 == "u18" ]; #ubuntu18
	then
		if [ $2 == "old" ];
		then
			apt install gcc g++ -y 2>> error.log #old==new
		elif [ $2 == "new" ];
		then
			apt install gcc g++ -y 2>> error.log
		else
			echo "The second parameter is invalid..."
		fi
	else
		echo "argu error.."
	fi
else
	echo "Use the format: ./1.sh [system] [gcc_version] "
	echo "	system: 
			centos7 ---> c7
			ubuntu18 ---> u18"
	echo "	gcc_version:
			gcc 4.5 ----> old
			gcc 7.4 ----> new
		"
	echo "eg: ./1.sh c7 old"
fi
