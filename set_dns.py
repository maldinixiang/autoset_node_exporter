# -*- coding: UTF-8 -*-
# author=baird_xiang
import os
import time
import sys
def set_dns():
    fp = file('/etc/resolvconf/resolv.conf.d/head')
    lines = []
    for line in fp: # 内置的迭代器, 效率很高
        lines.append(line)
    fp.close()
 
    lines.append('nameserver 114.114.114.114') # 在第二行插入
    s = '\n'.join(lines)
    fp = file('/etc/resolvconf/resolv.conf.d/head', 'w')
    fp.write(s)
    fp.close()
    os.system('sudo resolvconf -u')