#!/usr/bin/env python

import tempfile, os, time, sys, subprocess, shutil, json

class Vhost(object):
    
    def print_error_msg_and_exit(self, message):
        print "%(color)s%(message)s%(end)s" % {"color": '\033[91m', "end":'\033[0m', "message":message}
        sys.exit(0)
        
    def print_success_msg(self, message):
        print "%(color)s%(message)s%(end)s" % {"color": '\033[92m', "end":'\033[0m', "message":message}
        
    def print_notice_msg(self, message):
        print "%(color)s%(message)s%(end)s" % {"color": '\033[93m', "end":'\033[0m', "message":message}
        
    def create_vhost(self):
        current_dir = os.getcwd()

        if(not os.path.exists("%s/config.json" % current_dir)):
            self.print_notice_msg("config.json not found. Creating a new one in %s" % current_dir)
            shutil.copy('config.json.sample','config.json')

        with open('config.json', 'r') as f:
            try:
                config = json.loads(f.read())
                if(not os.path.exists(config['vhosts_file'])):
                    self.print_error_msg_and_exit("Error: Invalid vhosts_file setting in config.json - Path doesn't exist")
                if(not os.path.exists(config['apachectl'])):
                    self.print_error_msg_and_exit("Error: Invalid apachectl setting in config.json - Path doesn't exist")
            except:
                self.print_error_msg_and_exit("Error: Error reading configuration")

        site_name = raw_input("Enter the name of your site: ")

        if(not site_name):
            self.print_error_msg_and_exit("Error: Invalid site name")

        site_root_dir = raw_input("Enter the root directory of your site: ")

        if(not os.path.exists(site_root_dir)):
            self.print_error_msg_and_exit("Error: Site root directory does not exist")

        with open('.base-vhost.txt', 'r') as f:
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
    
        self.print_notice_msg("Restarting apache...")
    
        apacheprocess = subprocess.Popen([config['apachectl'], '-k', 'restart'], stdout=subprocess.PIPE)
        output = apacheprocess.communicate()
        print output[0]

        if(apacheprocess.returncode == 0):
            self.print_success_msg("Successfully created virtual host! Visit http://"+site_name+".local in your browser to view your site.")
            
Vhost().create_vhost()