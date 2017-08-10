#!/bin/bash
# dependence: jq & curl
# Author: Lyndon
# Usage: Replace with your dnspod info and install jq & curl then execute it.

TOKEN_ID="YOUR DNSPOD TOKEN ID"
TOKEN="YOUR DNSPOD TOKEN"
DOMAIN="YOUR DOMAIN"
SUBDOMAIN="YOUR SUBDOMAIN"
LOGIN_TOKEN="$TOKEN_ID,$TOKEN"

dnspod_get_id(){
    exestr="curl -s -k -X POST https://dnsapi.cn/Record.List  -d 'login_token=$LOGIN_TOKEN&format=json&domain=$DOMAIN'|jq '.domain.id'|sed 's/\"//g'"
    domain_id=$(eval $exestr)
    echo "domain_id: $domain_id"
    exestr="curl -s -k -X POST https://dnsapi.cn/Record.List  -d 'login_token=$LOGIN_TOKEN&format=json&domain=$DOMAIN&sub_domain=$SUBDOMAIN'|jq '.records[0].id'|sed 's/\"//g'"
    record_id=$(eval $exestr)
    echo "record_id: $record_id"
    exestr="curl -s -k -X POST https://dnsapi.cn/Record.List  -d 'login_token=$LOGIN_TOKEN&format=json&domain=$DOMAIN&sub_domain=$SUBDOMAIN'|jq '.records[0].line'|sed 's/\"//g'"
    record_line=$(eval $exestr)
    echo "record_line: $record_line"
}

dnspod_is_record_update(){
    exestr="curl -s -k -X POST https://dnsapi.cn/Record.List  -d 'login_token=$LOGIN_TOKEN&format=json&domain=$DOMAIN&sub_domain=$SUBDOMAIN'|jq '.records[0].value'|sed 's/\"//g'"
    resolve_ip=$(eval $exestr)
    echo "resolve_ip: $resolve_ip"
    exestr="curl -s ip.cn|awk -F ' ' '{print \$2}'|awk -F '：' '{print \$2}'"
    current_ip=$(eval $exestr)
    echo "current_ip: $current_ip"
    if [ "$resolve_ip" = "$current_ip" ]; then
        echo "Record updated."
        exit 0;
    fi
}

dnspod_update_record_ip(){
    exestr="curl -s -k -X POST https://dnsapi.cn/Record.Ddns -d 'login_token=$LOGIN_TOKEN&format=json&domain_id=$domain_id&record_id=$record_id&record_line=$record_line&sub_domain=$SUBDOMAIN'|jq '.status.message'"
    out=$(eval $exestr)
    echo $out
}

main(){
    echo "Start to check the ip address --- $(date +%Y%m%d-%H%M%S)"
    dnspod_is_record_update
    dnspod_get_id
    echo "Start to update the dns record --- $(date +%Y%m%d-%H%M%S)"
    dnspod_update_record_ip
}

main
