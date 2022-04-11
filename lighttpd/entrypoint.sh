#!/bin/bash
/usr/sbin/sshd -D -e &
lighttpd -D -f /etc/lighttpd/lighttpd.conf