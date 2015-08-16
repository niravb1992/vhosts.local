
About
===============
This project provides a Python script to create Apache virtual hosts in OS X.

Prerequisites
================

In your Apache's httpd.conf, virtual hosts have been enabled by uncommenting the line below

````
Include conf/extra/httpd-vhosts.conf
````

Getting Started
================
1. Download the latest release from the releases tab and extract it
2. Copy the config.json.sample file and rename it to config.json
3. Inside config.json, update the value of the `vhosts_file` key to the path to your httpd-vhosts.conf file, and update the value of the `apachectl` key to the path to your apachectl. 
4. That's it! Now, you can run:

   ````
   sudo ./vhost.py
   ````
    **You must run vhost.py as sudo since httpd-vhosts.conf and /etc/hosts need to be modified.**

## Removing a virtual host created by vhost.py
1. Open your httpd-vhosts.conf file, and delete the `<VirtualHost *:80>` entry corresponding to your virtual host
2. Open `/etc/hosts/` and delete the `127.0.0.1	<some site name>.local` entry corresponding to your virtual host
3. Restart apache
