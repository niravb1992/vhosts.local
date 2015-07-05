
About
===============
This project provides a Python script to create Apache virtual hosts in OS X.

Prerequisites
================

In your Apache's httpd.conf, virtual hosts have been enabled by uncommenting the line below

````
Include conf/extra/httpd-vhosts.conf
````

Setup
======
1. Download the latest release from the releases tab
2. Extract the downloaded file

Run
=======

````
cd path/to/vhosts.local/directory
sudo ./vhost.py
````
**NOTE: You must run vhost.py as sudo since httpd-vhosts.conf and /etc/hosts need to be modified.**
