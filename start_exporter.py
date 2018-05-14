# -*- coding: UTF-8 -*-
# author=baird_xiang
import os
import sys

if __name__ == "__main__":
    node_path = '/var/node_exporter/node_exporter/node_exporter-0.15.0.linux-amd64'
    os.chdir(node_path)
    os.system('sudo cp /etc/rc.local  /etc/rc.local.bak')
    os.system('sudo chmod 777 /etc/rc.local')
    fp1 = open('/etc/rc.local','r')
    fp= fp1.readlines()
    lines = []
    for line in fp:
        lines.append(line)
    fp1.close()
    if lines[26] == '\n' :
        lines.insert(26,'python %s/start_exporter.py'%node_path)
        s = ''.join(lines)
        fp2 = open('/etc/rc.local', 'w')
        fp2.write(s)
        fp2.close()
    else:
        pass
        
   
    
    if_up = os.popen('netstat -nultp |grep 9100')
    if_port_up = if_up.read()
    if_node_up = os.popen('sudo ps -ef |pgrep node_exporter')
    node_up_pid = if_node_up.read()
    if if_port_up:
        if node_up_pid :
            print 'node_exporter already start' 
        else:
            os.system('sudo  nohup ./node_exporter &')
    else:
        
        if if_node_up:
            os.system('sudo kill -9 %s'%node_up_pid)
            os.system('sudo nohup ./node_exporter &')
        else:
            os.system('sudo nohup ./node_exporter &')