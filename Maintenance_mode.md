# How to enter maintenance mode

##Full maintenance mode:

* update maintenance site file with maintenance window (currently by hand; /var/www/maintenance_kbase_us/htdocs/index.html on staging.berkeley)
* modify main nginx proxy to point to maintenance page (currently by hand; stanzas are in site config file)
* modify both http and https virtual hosts!
* modify narrative nginx proxy to point to maintenance page (currently by hand; stanzas are in site config file)
* modify both http and https virtual hosts!
