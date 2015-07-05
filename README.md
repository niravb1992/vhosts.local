
About
===============
This project provides a Python script to create Apache virtual hosts in OS X.

Prerequisites
================

In your Apache's httpd.conf, virtual hosts have been enabled by uncommenting the line below

````
Include conf/extra/httpd-vhosts.conf
````

Run
======
Download the latest release from the releases tab, extract it, and simply:

````
sudo ./vhost.py
````
**NOTE: You must run vhost.py as sudo since httpd-vhosts.conf and /etc/hosts need to be modified.**
