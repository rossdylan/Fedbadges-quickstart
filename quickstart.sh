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
