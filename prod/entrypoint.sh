#!/bin/bash
dockerd --host=tcp://localhost:2376 --tls=false &
/usr/sbin/sshd -D -e &
lighttpd -D -f /etc/lighttpd/lighttpd.conf