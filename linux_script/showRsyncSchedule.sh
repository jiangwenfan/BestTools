#!/bin/bash

path1="/root/1t/yum-repo-data/centos/" #***需要监控的目录1****
path2="/root/1t/yum-repo-data/epel/" #*****需要监控的目录2****

previousSizeC="0" #目录的初始大小。
previousSizeE="0"

while :
do
	sizec=`du -s ${path1}|cut -d"/" -f1`
	sizech=`du -sh ${path1}|cut -d"/" -f1`
	sizee=`du -s ${path2}|cut -d"/" -f1`
	sizeeh=`du -sh ${path2}|cut -d"/" -f1`

	if [ ${sizec} -gt ${previousSizeC} ]; then
		#echo ${previousSizeC}
		echo -e "\033[42;30m centos官方源正在进行同步\033[0m"
		echo "当前大小是:" ${sizech}
		previousSizeC=${sizec}
	else
		#echo -e "\033[41;30m centos官方源同步速度为0\033[0m"
        process=`ps aux|grep rsync | grep -v auto |grep -v SCREEN|wc -l`
        if [ $process -lt 4 ]; then
            echo "有进程中断了!"
            echo "当前进程数:" $process
        else
		    echo -e "\033[41;30m centos官方源同步速度为0\033[0m"
        fi
	fi
	
	if [ ${sizee} -gt ${previousSizeE} ]; then
		#echo ${previousSizeE}
		echo -e "\033[42;30m epel扩展源正在进行同步\033[0m"
		echo "当前大小是:" ${sizeeh}
		previousSizeE=${sizee}
	else
		#echo -e  "\033[41;30m epel扩展源同步速度为0\033[0m"
        process=`ps aux|grep rsync | grep -v auto |grep -v SCREEN|wc -l`
        if [ $process -lt 4 ]; then
            echo "有进程中断了!"
            echo "当前进程数:" $process
        else
		    echo -e  "\033[41;30m epel扩展源同步速度为0\033[0m"
        fi
	fi
	
	echo -e "\n\n"
	sleep 600 #根据需求可以修改。
done
