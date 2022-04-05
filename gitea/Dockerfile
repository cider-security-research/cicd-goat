FROM gitea/gitea:1.16.5 AS base

ARG USERNAME=red_queen
ARG PASSWORD=ciderland5#
ENV PYTHONUNBUFFERED=1

COPY --chown=git:git app.ini /data/gitea/conf/
RUN apk add --update --no-cache python3 py3-pip && \
    ln -sf python3 /usr/bin/python && \
    python3 --version

RUN python3 -m pip install pipenv

COPY Pipfile* /setup/

RUN cd /setup && pipenv install --system --deploy

COPY . /setup/

RUN chmod u+x /setup/giteacasc/askpass.py

RUN /usr/bin/entrypoint & \
    sleep 20 && \
    su -c "gitea admin user create --username $USERNAME --password $PASSWORD --email queen@localhost --admin" git && \
    cd /setup && \
    python3 -m giteacasc /setup/gitea.yaml -u $USERNAME -p $PASSWORD

FROM gitea/gitea:1.16.5
COPY --from=base --chown=git:git /data/ /data
LABEL org.opencontainers.image.vendor="Cider Security" \
    org.opencontainers.image.title="CI/CD Goat - Gitea" \
    org.opencontainers.image.description="Deliberately vulnerable CI/CD environment." \
    org.opencontainers.image.url="https://hub.docker.com/r/cidersecurity/goat-gitea" \
    org.opencontainers.image.source="https://github.com/cider-security-research/cicd-goat" \
    org.opencontainers.image.licenses="GPL-3.0" \
    org.opencontainers.image.version="${VERSION}" \
    org.opencontainers.image.revision="${COMMIT_SHA}"
ENTRYPOINT su -c "gitea" git