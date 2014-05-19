
vhosts.local [Incomplete]
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

Run
=======

````
python vhost.py
````