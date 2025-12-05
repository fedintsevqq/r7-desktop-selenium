#!/bin/bash

sudo dnf -y update
sudo dnf -y install wget gcc openssl-devel bzip2-devel libffi-devel xz-devel tk-devel
sudo dnf -y install autoconf automake  binutils bison flex gcc-c++ gdb glibc-devel libtool make pkgconf strace
sudo dnf -y install byacc ccache cscope ctags elfutils indent ltrace perf valgrind

cd /tmp/
wget https://github.com/libffi/libffi/releases/download/v3.4.5/libffi-3.4.5.tar.gz
tar xzf libffi-3.4.5.tar.gz
cd libffi-3.4.5
./configure
make
sudo make install

cd /tmp/
wget https://www.python.org/ftp/python/3.13.9/Python-3.13.9.tgz
tar xzf Python-3.13.9.tgz
cd Python-3.13.9
sudo ./configure --prefix=/opt/python/3.13.9/ --enable-optimizations \
	LIBFFI_LIBS="-L/usr/local/lib64 -lffi -Wl,-rpath -Wl,/usr/local/lib64" \
	LIBFFI_CFLAGS="-I/usr/local/include" 
sudo make -j "$(grep -c ^processor /proc/cpuinfo)"
sudo make altinstall
#sudo rm /tmp/Python-3.13.9.tgz
#sudo rm /tmp/libffi-3.4.5.tar.gz
echo "Python 3.13.9 is installed in /opt/python/3.13.9/"
echo "To create venv, while in the project folder, use the next command:"
echo "/opt/python/3.13.9/bin/python3.13 -m venv .venv"
