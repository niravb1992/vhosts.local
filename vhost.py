#!/usr/bin/env python

import tempfile, os, time, sys, subprocess, shutil, json

if(not os.path.exists(os.getcwd()+'/config.json')):
    shutil.copy('config.json.sample','config.json')

if (not os.path.exists('/etc/hosts')):
    print "Error: /etc/hosts doesn't exist"
    sys.exit(0)

with open('config.json', 'r') as f:
    try:
        config = json.loads(f.read())
        if(not os.path.exists(config['vhosts_file'])):
            print "Error: Invalid vhosts_file setting in config.json - Path doesn't exist"
            sys.exit(0)
        if(not os.path.exists(config['apachectl'])):
            print "Error: Invalid apachectl setting in config.json - Path doesn't exist"
            sys.exit(0)
    except:
        print "Error: Error reading configuration"
        sys.exit(0)

site_name = raw_input("Enter the name of your site: ")
site_root_dir = raw_input("Enter the root directory of your site: ")

if(not os.path.exists(site_root_dir)):
    print "Error: This directory doesn't exist"
    sys.exit(0)

with open('sample-vhost.txt', 'r') as f:
    vhost_lines = f.readlines()
    vhost_lines.insert(0,"\n\n")
    vhost_lines.insert(2,'\tDocumentRoot "'+site_root_dir+'"\n')
    vhost_lines.insert(3, "\tServerName "+site_name+".local\n")
    vhost_lines.insert(8, '\t<Directory "'+site_root_dir+'">\n')

with open(config['vhosts_file'], 'a') as f:
    for line in vhost_lines:
        f.write(line)

with open('/etc/hosts', 'a') as f:
    f.write('\n127.0.0.1\t'+site_name+'.local')
    
print "Restarting apache..."
    
apacheprocess = subprocess.Popen([config['apachectl'], '-k', 'restart'], stdout=subprocess.PIPE)
output = apacheprocess.communicate()
print output[0]

if(apacheprocess.returncode == 0):
    print "Successfully created virtual host! Visit http://"+site_name+".local in your browser to view your site."    