#!/usr/bin/env bash
# Auto install latest kernel for TCP BBR
# System Required: Ubuntu12+ 64bit
# Copyright (C) 2016-2018 Lyndon <i@lyndon.pw>
# URL: http://blog.lyndon.pw

red='\033[0;31m'
green='\033[0;32m'
yellow='\033[0;33m'
plain='\033[0m'

cur_dir=$(pwd)

[[ $EUID -ne 0 ]] && echo -e "${red}Error:${plain} This script must be run as root!" && exit 1

[[ -d "/proc/vz" ]] && echo -e "${red}Error:${plain} Your VPS is based on OpenVZ, not be supported." && exit 1

get_latest_version() {

    latest_version=$(wget -qO- http://kernel.ubuntu.com/~kernel-ppa/mainline/ | awk -F'\"v' '/v[4-9]./{print $2}' | cut -d/ -f1 | grep -v -  | sort -V | tail -1)

    [ -z ${latest_version} ] && return 1

    deb_name=$(wget -qO- http://kernel.ubuntu.com/~kernel-ppa/mainline/v${latest_version}/ | grep "linux-image" | grep "generic" | awk -F'\">' '/amd64.deb/{print $2}' | cut -d'<' -f1 | head -1)
    deb_kernel_url="http://kernel.ubuntu.com/~kernel-ppa/mainline/v${latest_version}/${deb_name}"
    deb_kernel_name="linux-image-${latest_version}-amd64.deb"

    deb_header_name=$(wget -qO- http://kernel.ubuntu.com/~kernel-ppa/mainline/v${latest_version}/ | grep "linux-headers" | awk -F'\">' '/all.deb/{print $2}' | cut -d'<' -f1 | head -1)
    deb_headers_url="http://kernel.ubuntu.com/~kernel-ppa/mainline/v${latest_version}/${deb_header_name}"
    deb_headers_name="linux-headers-${latest_version}-all.deb"

    [ ! -z ${deb_name} ] && return 0 || return 1
    [ ! -z ${deb_header_name} ] && return 0 || return 1
}

check_bbr_status() {
    local param=$(sysctl net.ipv4.tcp_available_congestion_control | awk '{print $3}')
    if [[ x"${param}" == x"bbr" ]]; then
        return 0
    else
        return 1
    fi
}

version_ge(){
    test "$(echo "$@" | tr " " "\n" | sort -rV | head -n 1)" == "$1"
}

check_kernel_version() {
    local kernel_version=$(uname -r | cut -d- -f1)
    if version_ge ${kernel_version} 4.9; then
        return 0
    else
        return 1
    fi
}

sysctl_config() {
    sed -i '/net.core.default_qdisc/d' /etc/sysctl.conf
    sed -i '/net.ipv4.tcp_congestion_control/d' /etc/sysctl.conf
    echo "net.core.default_qdisc = fq" >> /etc/sysctl.conf
    echo "net.ipv4.tcp_congestion_control = bbr" >> /etc/sysctl.conf
    sysctl -p >/dev/null 2>&1
}

install_config() {
    /usr/sbin/update-grub
}

reboot_os() {
    echo
    echo -e "${green}Info:${plain} The system needs to reboot."
    reboot
}

install_bbr() {
    check_bbr_status
    if [ $? -eq 0 ]; then
        echo
        echo -e "${green}Info:${plain} TCP BBR has been installed. nothing to do..."
        exit 0
    fi
    check_kernel_version
    if [ $? -eq 0 ]; then
        echo
        echo -e "${green}Info:${plain} Your kernel version is greater than 4.9, directly setting TCP BBR..."
        sysctl_config
        echo -e "${green}Info:${plain} Setting TCP BBR completed..."
        exit 0
    fi

    get_latest_version
    [ $? -ne 0 ] && echo -e "${red}Error:${plain} Get latest kernel version failed." && exit 1
    wget -c -t3 -T60 -O ${deb_kernel_name} ${deb_kernel_url}
    if [ $? -ne 0 ]; then
        echo -e "${red}Error:${plain} Download ${deb_kernel_name} failed, please check it."
        exit 1
    fi
    wget -c -t3 -T60 -O ${deb_headers_name} ${deb_headers_url}
    if [ $? -ne 0 ]; then
        echo -e "${red}Error:${plain} Download ${deb_headers_name} failed, please check it."
        exit 1
    fi
    dpkg -i ${deb_kernel_name} ${deb_headers_name}
    rm -fv ${deb_kernel_name} ${deb_headers_name}

    install_config
    sysctl_config
    reboot_os
}


clear
echo "----------------------------------------"
echo " Auto install latest kernel for TCP BBR on Ubuntu 64bit"
echo "----------------------------------------"

install_bbr 2>&1 | tee ${cur_dir}/install_bbr.log