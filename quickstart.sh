#!/bin/bash

sudo pip install virtualenv virtualenvwrapper
sudo yum install mysql-devel zeromq-devel git

source /usr/bin/virtualenvwrapper.sh

rmvirtualenv tahrir
rmvirtualenv fedmsg

mkvirtualenv fedmsg
deactivate
mkvirtualenv tahrir
deactivate

git clone https://github.com/rossdylan/fedmsg.git
git clone https://github.com/ralphbean/tahrir.git

cd fedmsg
git checkout fedbadges
workon fedmsg
python setup.py install
deactivate

cd ../

cd tahrir
git checkout develop
workon tahrir
python setup.py install
deactivate

sudo service mysqld start

read -p "Enter mysql username for fedbadges: " username
read -s -p "Enter password for fedbadges user: " password
read -p "Enter database name for fedbadges: " dbname

mysql -u root -p -e "grant all privileges on *.* TO '$username'@'localhost' identified by '$password'; create database $dbname"

