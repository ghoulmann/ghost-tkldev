#!/usr/bin/python3
"""Set Ghost admin password, email, name and domain
Option:
    --password=     unless provided, will ask interactively
    --email=        unless provided, will ask interactively
    --uname=        unless provided, will ask interactively
    --domain=       unless provided, will ask interactively
"""

import sys
import getopt
import bcrypt
import sqlite3
from dialog_wrapper import Dialog
import re
from mysqlconf import MySQL
import subprocess

DEFAULT_UNAME = 'Blogger Unknown'

def usage(s=None):
    if s:
        print("Error:", s, file=sys.stderr)
    print("Syntax: %s [options]" % sys.argv[0], file=sys.stderr)
    print(__doc__, file=sys.stderr)
    sys.exit(1)

def main():
    try:
        opts, args = getopt.gnu_getopt(sys.argv[1:], "h",
                                       ['help', 'pass=', 'email=',
                                        'uname=', 'domain='])
    except getopt.GetoptError as e:
        usage(e)

    password = ''
    email = ''
    uname = ''
    domain = ''

    for opt, val in opts:
        if opt in ('-h', '--help'):
            usage()
        elif opt == '--pass':
            password = val
        elif opt == '--email':
            email = val
        elif opt == '--uname':
            uname = val
        elif opt == '--domain':
            domain = val

    if not password:
        d = Dialog('Turnkey Linux - First boot configuration')
        password = d.get_password(
            "Ghost Password",
            "Enter a new password for the Ghost blogger account.")

    if not email:
        if 'd' not in locals():
            d = Dialog('Turnkey Linux - First boot configuration')

        email = d.get_email(
            "Ghost Email",
            "Please enter email address for the Ghost blogger account.",
            "admin@example.com")

    if not uname:
        if 'd' not in locals():
            d = Dialog('Turnkey Linux - First boot configuration')

    uname = d.get_input(
        "Ghost Account Name",
        "Enter the Ghost blogger's name (real name recommended).",
        DEFAULT_UNAME)

    if uname == "DEFAULT":
        uname = DEFAULT_UNAME

    if not domain:
        if 'd' not in locals():
            d = Dialog('Turnkey Linux - First boot configuration')

        domain = d.get_input(
            "Ghost Domain",
            "Enter the domain to serve Ghost, include http(s) protocol, defaults to https.",
            "https://www.example.com")

        if not domain.startswith('https://') and not domain.startswith('http://'):
            domain = 'https://'+domain

    with open('/opt/ghost/config.production.json', 'r') as fob:
        all_config = fob.read()

    current_url = re.findall(r'(https?://\S+)', all_config)[0] # third occurance in file
    current_url = current_url.replace('"', '').replace(',', '')
    all_config = all_config.replace(current_url, domain)

    with open('/opt/ghost/config.production.json', 'w') as fob:
        fob.write(all_config)

    password = password.encode('utf8')    

    hashed_pw = bcrypt.hashpw(password, bcrypt.gensalt())

    cur = MySQL()
    cur.execute('UPDATE ghost.users SET password=%s WHERE id="1";', (hashed_pw,))
    cur.execute('UPDATE ghost.users SET name=%s WHERE id="1";', (uname,))
    cur.execute('UPDATE ghost.users SET email=%s WHERE id="1";', (email,))
    cur.execute('UPDATE ghost.users SET status=\"active\" WHERE id="1";')

    subprocess.run(["chpasswd"], input=b"ghost_user:" + password)
    subprocess.run(["service", "ghost_localhost", "restart"])

if __name__ == '__main__':
    main()
