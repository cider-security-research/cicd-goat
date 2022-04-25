FROM gitea/gitea:1.16.5 AS base
ARG VERSION
ARG COMMIT_SHA

LABEL org.opencontainers.image.vendor="Cider Security" \
    org.opencontainers.image.title="CI/CD Goat - Gitea" \
    org.opencontainers.image.description="Deliberately vulnerable CI/CD environment." \
    org.opencontainers.image.url="https://hub.docker.com/r/cidersecurity/goat-gitea" \
    org.opencontainers.image.source="https://github.com/cider-security-research/cicd-goat" \
    org.opencontainers.image.licenses="Apache-2.0" \
    org.opencontainers.image.version=$VERSION \
    org.opencontainers.image.revision=$COMMIT_SHA

ENV PYTHONUNBUFFERED=1

RUN apk add --update --no-cache python3 py3-pip && \
    ln -sf python3 /usr/bin/python && \
    python3 --version
RUN python3 -m pip install --no-cache-dir pipenv

COPY Pipfile* /setup/
RUN cd /setup && pipenv install --system --deploy

COPY . /setup/
RUN /setup/check_git.py && chmod 755 /setup/giteacasc/askpass.py /setup/run
COPY --chown=git:git app.ini /data/gitea/conf/

ENTRYPOINT ["/setup/run"]


