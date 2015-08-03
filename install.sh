#! /bin/sh
sudo apt-get -y install mysql-server libapache2-mod-auth-mysql
sudo apt-get -y install libmysqlclient-dev
sudo apt-get -y install python-pip
sudo apt-get -y install python-dev

pip install -r requirements.txt
