#!/bin/bash
#Version: 2.3 for Debian
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

#проверяю обновления | обновляюсь
echo "\033[93mПроверка обновлений...\033[00m"
sudo apt-get update
checkStatus

echo "\033[93mОтключение Sophos...\033[00m"
sudo /opt/sophos-av/bin/savdctl disableOnBoot savd
checkStatus

echo "\033[93mУстановка обновлений...\033[00m"
sudo apt-get upgrade
checkStatus

sudo apt-get dist-upgrade
checkStatus
echo "\033[93mОчистка обновлений...\033[00m"
sudo apt-get autoclean
sudo apt autoremove
checkStatus

# Блокировка icmp пакетов
echo "\033[93mВключаю блокировку ICMP запросов...\033[00m"
iptablas -I OUTPUT -p icmp -j DROP
checkStatus

read -p 'Включать TOR и Proxy? [Y/n] ' fistQ
case $fistQ in
  y|Y)
    echo "Включение TOR..."
    service tor start
    checkStatus

    echo "Включение Proxy..."
    service privoxy start
    checkStatus

    echo "TOR и Proxy включены"
    echo " "
    ;;
  n|N)

    ;;
  *)
    echo "Использована неверная команда..."
    ;;
esac

echo "\033[92mВключение Sophos...\033[00m"
sudo /opt/sophos-av/bin/savdctl enableOnBoot savd
checkStatus

clear
echo "\033[92mХозяин, все сделано\033[00m"
