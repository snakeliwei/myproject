#!/bin/bash

# install elrepo
rpm --import https://www.elrepo.org/RPM-GPG-KEY-elrepo.org
yum install -y https://www.elrepo.org/elrepo-release-7.el7.elrepo.noarch.rpm

# install kernel-ml
yum update -y
yum --enablerepo=elrepo-kernel install kernel-ml -y

# add BBR config
bash -c 'echo "# Enable BBR" >> /usr/lib/sysctl.d/50-default.conf'
bash -c 'echo "net.core.default_qdisc = fq" >> /usr/lib/sysctl.d/50-default.conf'
bash -c 'echo "net.ipv4.tcp_congestion_control=bbr" >> /usr/lib/sysctl.d/50-default.conf'

# modify grub menu
grub2-set-default 0
grub2-mkconfig -o /boot/grub2/grub.cfg

# check the kernel list
rpm -qa | grep kernel
