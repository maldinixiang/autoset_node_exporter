# -*- coding: UTF-8 -*-
# author=baird_xiang
import os
import time
import sys
import paramiko

def ssh_to_ras(ip,port,username,passwd):
    ss = paramiko.SSHClient()
    ss.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ss.connect(ip,port,username,passwd)
    stdin, stdout1, stderr = ss.exec_command ('pwd') 
    setdns_command = "sudo tee /etc/resolv.conf  <<< 'nameserver 114.114.114.114' "
    stdin3, stdout3, stderr = ss.exec_command(setdns_command,get_pty=True )
    stdin3.write(passwd+'\n')
    stdin2, stdout2, stderr = ss.exec_command('cd  /var ;sudo mkdir node_exporter ; sudo chmod 777 node_exporter/ ;\
    cd  /var/node_exporter ; \
    ls ; wget http://files.dev-rs.com/QA/Performance_Testing/environment/node_exporter.zip ;unzip node_exporter.zip',get_pty=True)
    stdin2.write(passwd+'\n')  
    
    stdin2.write("Y") # Generally speaking, the first connection, need a simple interaction. 
    print stdout2.read() 
    ss.close() 

    
if __name__ == "__main__":
    ip = ''
    port = ''
    username = ''
    passwd = ''
    dir_path = os.getcwd()
    ssh_to_ras(ip,port,username,passwd)
     
    
