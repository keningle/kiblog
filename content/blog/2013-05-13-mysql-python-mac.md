Title: Python and MySQL
Date: 2013-05-13 
Tags: python, mysql, mac, osx
Slug: mysql-python-mac

I ran into a problem today I hadn’t experienced in a long time.  I was trying to get mysql-python installed when running the .dmg for MySQL and it kept giving the following error:

```bash
EnvironmentError: mysql_config not found
```

After a bit of refreshing my memory I remembered that it was actually pretty simple to fix.  The mac is a little different in where it stores the mysql_config file.  Just run the following command from and all is good:

```bash
$ export PATH=/usr/local/mysql/bin/:$PATH
```

You will then need to add a symlink to the libmysqlclient in /usr/lib:

```bash
$ sudo ln -s /usr/local/mysql/lib/libmysqlclient.18.dylib /usr/lib/libmysqlclient.18.dylib
```

Then you can run pip install mysql-python.
