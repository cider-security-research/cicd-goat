FROM docker:dind
ARG COMMIT_SHA
ARG VERSION

LABEL org.opencontainers.image.vendor="Cider Security" \
    org.opencontainers.image.title="CI/CD Goat - Prod" \
    org.opencontainers.image.description="Deliberately vulnerable CI/CD environment." \
    org.opencontainers.image.url="https://hub.docker.com/r/cidersecurity/goat-prod" \
    org.opencontainers.image.source="https://github.com/cider-security-research/cicd-goat" \
    org.opencontainers.image.licenses="Apache-2.0" \
    org.opencontainers.image.version=$VERSION \
    org.opencontainers.image.revision=$COMMIT_SHA

RUN apk add --no-cache openssh-client-default \
    && apk add --no-cache openssh \
    && ssh-keygen -A \
    && mkdir /root/.ssh \
    && chmod 0700 /root/.ssh
COPY authorized_keys /root/.ssh/
COPY entrypoint.sh /usr/sbin
COPY sshd_config /etc/ssh/
RUN chmod 600 /root/.ssh/authorized_keys && \
    chmod 755 /usr/sbin/entrypoint.sh && \
    apk update \
    && apk add --no-cache lighttpd
COPY reportcov.sh /var/www/localhost/htdocs
COPY server.crt /etc/ssl/certs/

# Only for testing of hearts challenge
RUN adduser agent -D && \
    echo "agent:B1A648E1-FD8B-4D66-8CAF-78114F55D396" | chpasswd --md5 agent

EXPOSE 22
EXPOSE 80

CMD ["sh", "/usr/sbin/entrypoint.sh"]
