#!/usr/local/bin/env python

# -*- coding: utf-8 -*-

from itertools import combinations
import subprocess
import os
import paramiko

file = open('/home/jxie/drop_all.sh','r')
iptables_list = []
#while 1:
#    lines = file.readlines(1000)
#    if not lines:
#       break
#    for line in lines:
#		iptables_list.append(line)
#print iptables_list
for line in file:
    iptables_list.append(line.rstrip())

def find_all_sublist(mylist):
     #for len in range(1,len(mylist)):
    for len in range(1,6):
	for c in combinations(iptables_list,len):
	   yield  c

def vyos_ping_check():
	hostname=raw_input('10.61.34.102')
	username='jxie'
	password='!'
	ssh=paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(hostname,22,username,password)
	stdin,stdout,stderr=ssh.exec_command('ping -c 5 10.141.177.14')
	print stdout.readlines()
	ssh.close
	if 'ttl=64' in stdout.readline:
		return True
	else:
		return False
	
def main():
    print 'hhhhh'
    with open('/tmp/result.txt','w') as f:
        for sub in find_all_sublist(iptables_list):
	    for s in sub:
                print s
                print type(s)
	        subprocess.call(s.split())

		if vyos_ping_check == True:
		    f.write(sub + os.linesep)
		    for rule in sub:
	                subprocess.call(('echo iptables -A ' + rule[15:]).split())
	        else:
		    for l in sub:
		        subprocess.call(('echo iptables -A ' + l[15:]).split())

if __name__ == '__main__':
    print 'hahah'
    main()
