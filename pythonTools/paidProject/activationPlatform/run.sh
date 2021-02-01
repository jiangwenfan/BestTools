#!/usr/bin/bash

if [ $1 == "start" ] 2> /dev/null
then
    echo "start server1..."
    screen -dmS pythonServer1 python manage.py runserver 0.0.0.0:7878
    if [ $? == 0 ]
    then
        echo -e "server1 status : \033[32m success \033[0m"
    else
        echo -e "server1 status : \033[31m fail \033[0m"
    fi
    echo "start server2 ..."
    screen -dmS pythonServer2 python static/demo.py
    if [ $? == 0 ]
    then
        echo -e "server2 status : \033[32m success \033[0m"
    else
        echo -e "server2 status : \033[31m fail \033[0m"
    fi
elif [ $1 == "stop" ] 2> /dev/null
then
    echo "stop server1..."
    pid1=`screen -ls |grep pythonServer1|cut -d"." -f1` 
    kill $pid1
    echo -e "server1 status :\033[31m dead \033[0m"
    echo "stop server2..."
    pid2=`screen -ls |grep pythonServer2|cut -d"." -f1` 
    kill $pid2
    echo -e "server2 status : \033[31m dead \033[0m"
else
    echo "
        usage: ./run.sh [options]
        
        eg:
            ./run.sh start 开启服务
            ./run.sh stop 关闭服务
        "
fi
