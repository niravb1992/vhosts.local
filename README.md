
vhosts.local
===============

A simple script to create an apache virtual host in mac

Prerequisites
================

1. Install:
	1. Apache
	2. Python (Not if you have Xcode installed)
2. In your httpd.conf, virtual hosts have been enabled by uncommenting the line below

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
sudo python vhost.py
````
<strong>NOTE: You must run the above vhost.py as sudo since certain system files need to be modified.</strong>