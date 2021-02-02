#!/bin/bash
if [ $(dpkg-query -W -f='${Status}' python3-distutils 2>/dev/null | grep -c "installed") -eq 0 ];
then
  apt install python3-distutils;
fi;

if [ $(ls | grep -c "SeqrepC-1.0.0") -eq 0 ];
then
  wget https://github.com/ednilsonlomazi/SeqrepC/archive/v1.0.0.zip;
  unzip v1.0.0.zip;
fi;

cd SeqrepC-1.0.0/seqrepc/;
python3 setup.py install;
pip3 install seqreppy;
