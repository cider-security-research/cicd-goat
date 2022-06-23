#!/bin/bash
set -m
USERNAME=red_queen
PASSWORD=ciderland5#
/usr/bin/entrypoint &
sleep 40
su -c "gitea admin user create --username $USERNAME --password $PASSWORD --email queen@localhost --admin" git
cd /setup
python3 -m giteacasc /setup/gitea.yaml -u $USERNAME -p $PASSWORD
fg #/usr/bin/entrypoint