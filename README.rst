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

Recommended (but perhaps not required):

Update nodejs (example updating to latest v14)::

   n 14

Or, updating to latest LTS::

   n lts

Update Ghost CLI (to latest)::

   npm install -g ghost-cli@latest

Then update ghost itself. Become ghost_user and update::

    su - ghost_user
    ghost update

Once finished, exit back to the root user::

   exit

**Note:** ghost-cli may ask for your sudo password, by default the
"ghost_user" sudo password is the same password you set for the Ghost UI
admin password at firstboot.

Ghost does not have a security only newsletter so we recommend that 
you subcribe to the `Ghost Blog`_ to keep up to date.

Credentials *(passwords set at first boot)*
-------------------------------------------

-  Webmin, SSH, MySQL, Adminer: username **root**
-  Ghost: username [email set at firstboot]


.. _Ghost: https://ghost.org/
.. _TurnKey Core: https://www.turnkeylinux.org/core
.. _Ghost Blog: https://blog.ghost.org/
