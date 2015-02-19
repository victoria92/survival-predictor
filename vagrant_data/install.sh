#!/bin/bash

echo -e "\n\n"
echo "####################"
echo "## Installing Git ##"
echo "####################"

apt-get install -y git=1:1.9.1-1



echo -e "\n\n"
echo "#######################"
echo "## Installing Python ##"
echo "## Version 3.4.2     ##"
echo "#######################"

# to be able to compile Python Source, we will need few packages
apt-get install -y build-essential libncursesw5-dev libreadline6-dev
apt-get install -y libssl-dev libgdbm-dev libc6-dev libsqlite3-dev tk-dev
apt-get install -y zlib1g-dev libssl-dev python3-dev
# these are extra needed for scipy
apt-get install -y libopenblas-dev libatlas-dev libatlas3-base liblapack-dev gfortran libpng12-dev libblas-dev
# self explanatory
apt-get install -y python3-numpy python3-scipy

# download and build Python 3.4.2
mkdir /home/vagrant/downloads
cd /home/vagrant/downloads
wget -O Python-3.4.2.tgz https://www.python.org/ftp/python/3.4.2/Python-3.4.2.tgz
tar xvzf Python-3.4.2.tgz
cd /home/vagrant/downloads/Python-3.4.2
# Python 3.4.2 will be installed in /opt/python3
./configure --prefix=/opt/python3
make
make install



echo -e "\n\n"
echo "############################################"
echo "## Creating survival-predictor virtualenv ##"
echo "############################################"

apt-get install -y python-pip
pip install virtualenv==1.11.6
pip install virtualenvwrapper==4.3

echo "source /usr/local/bin/virtualenvwrapper.sh" >> /home/vagrant/.bashrc
mkdir /home/vagrant/.virtualenvs
WORKON_HOME=/home/vagrant/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh

cd /home/vagrant/survival-predictor
mkvirtualenv -a `pwd` -p /opt/python3/bin/python3.4 survival-predictor
# Set vagrant as owner for virtualenvs
chown -R vagrant:vagrant /home/vagrant/.virtualenvs



echo -e "\n\n"
echo "#############################"
echo "## Install python packages ##"
echo "#############################"


# temporary we will enable swap as the memory of the VM may not be sufficiant
# for compiling that scipy... killed me to find out
/bin/dd if=/dev/zero of=/var/swap.1 bs=1M count=1024
/sbin/mkswap /var/swap.1
/sbin/swapon /var/swap.1

workon survival-predictor
pip install -U setuptools
pip install -U pip
pip install numpy==1.8.2
pip install scipy==0.15.1
pip install -r requirements.txt
# disable swapping after requirements are installed
swapoff /var/swap.1
rm /var/swap.1



echo -e "\n\n"
echo "#################################################"
echo "## Removing packages that are no longer needed ##"
echo "#################################################"
apt-get autoremove -y



echo -e "\n\n"
echo "#############################"
echo "## Successful installation ##"
echo "#############################"
exit 0
