FROM alpine:3.15.3
RUN apk add --no-cache \
        openssh \
    && ssh-keygen -A \
    && mkdir /root/.ssh \
    && chmod 0700 /root/.ssh
COPY authorized_keys /root/.ssh/
COPY entrypoint.sh /usr/sbin
COPY sshd_config /etc/ssh/
RUN chmod 600 /root/.ssh/authorized_keys && \
    chmod 755 /usr/sbin/entrypoint.sh && \
    apk update \
    && apk add lighttpd \
    && rm -rf /var/cache/apk/* \
    && passwd -u root
COPY reportcov.sh /var/www/localhost/htdocs

EXPOSE 22
EXPOSE 80

CMD ["sh", "/usr/sbin/entrypoint.sh"]