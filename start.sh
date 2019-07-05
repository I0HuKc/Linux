#!/bin/bash
#Version: for Kali Linux
#Date: 05.07.2019
#Author: Egor Sobolev
#Disclaimer: Editing author will not make you the real coder )

SETCOLOR_SUCCESS="echo -en \\033[1;32m"
SETCOLOR_FAILURE="echo -en \\033[1;31m"
SETCOLOR_NORMAL="echo -en \\033[0;39m"

# Функция проверяющая успешность выполнения команды
checkStatus() {
  if [ $? -eq 0 ]
   then
      $SETCOLOR_SUCCESS
      echo -n "$(tput hpa $(tput cols))$(tput cub 6)[OK]"
      $SETCOLOR_NORMAL
      echo
  else
      $SETCOLOR_FAILURE
      echo -n "$(tput hpa $(tput cols))$(tput cub 6)[fail]"
      $SETCOLOR_NORMAL
      echo
  fi
}

echo "Включение TOR..."
service tor start
checkStatus

echo "Включение Proxy..."
service privoxy start
checkStatus

echo "TOR и Proxy включены"
echo " "

#проверяю обновления | обновляюсь
apt-get update #всместо apt-get пропитсать команду обновления для своего дистрибутива
checkStatus
apt-get upgrade
checkStatus
apt-get dist-upgrade
checkStatus
apt-get autoclean
checkStatus

clear
echo "Хозяин, всё сделано"
