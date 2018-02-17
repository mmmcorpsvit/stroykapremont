# stroykapremont
Django LandPage based project

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

***TODO to read:***
* http://djangosuit.com/
* https://stackoverflow.com/questions/29091014/how-do-i-leverage-browser-caching-for-google-fonts
* https://github.com/caktus/django-scribbler
* https://github.com/mbi/django-front
* https://github.com/matthiask/django-content-editor/



***Deploy:***

* add alias for favicon.ico, use:

ou can put it directly in your http-vhosts.conf file

<VirtualHost *:80>
             ServerName crucial-systems.com
             DocumentRoot /home/crucial/crucial-stack/crucialwww
... etc...

Alias /favicon.ico "/home/crucial/crucial-stack/crucialwww/favicon.ico"

...

WSGIScriptAlias / /home/crucial/crucial-stack/crucial/crucial.wsgi



note that even though the document root appears to be mapped to the crucialwww directory, in practice the WSGIScriptAlias / means that everything is directed to django.

all image and css directories I also use Alias (before the WSGIScriptAlias) to map those to the correct directories.

I used to do a lot of symlinks and juggling of my directories.  I'm preferring this method now as its much easier to change and move things.
