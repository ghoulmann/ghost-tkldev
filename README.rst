Ghost - A publishing platform for professional bloggers
=======================================================

`Ghost`_ is an open source publishing platform which is beautifully 
designed, easy to use, and free for everyone. Start a blog with Ghost 
today and learn to blog! Ghost is a lightning-fast Node.js 
application with an Ember.js admin client and Handlebars.js themes.

This appliance includes all the standard features in `TurnKey Core`_,
and on top of that:

- Ghost configurations:

   - Ghost installed from upstream source code to /opt/ghost

     **Security note**: Updates to Ghost may require supervision so
     they **ARE NOT** configured to install automatically. See below for
     updating Ghost.

   
   - Ghost process managed by `pm2`_.
   - Includes Nginx (webserver); pre-configured to proxy Ghost.

- SSL support out of the box.
- Postfix MTA (bound to localhost) to allow sending of email (e.g.,
  password recovery).
- Webmin module for configuring Postfix.

Supervised Manual Ghost Update
------------------------------

**Note:** Check the Ghost docs to ensure that upgrading your 
current version to the latest is supported. Always ensure that 
you have a tested backup before proceeding with software updates.

Assuming that updating to the latest Ghost version is supported. 
update from the command line::

    su ghost_user
    cd ~
    ghost update

.. note:

   ghost may ask for your sudo password, in this case this will be
   the "ghost_user" password which is set to the same password as
   your ghost admin password.

Ghost does not have a security only newsletter so we recommend that 
you subcribe to the `Ghost Blog`_ to keep up to date.

Credentials *(passwords set at first boot)*
-------------------------------------------

-  Webmin, SSH, MySQL, Adminer: username **root**
-  Ghost: username **admin**


.. _Ghost: https://ghost.org/
.. _TurnKey Core: https://www.turnkeylinux.org/core
.. _pm2: http://pm2.keymetrics.io/
.. _Ghost Blog: https://blog.ghost.org/

