FROM gitea/gitea:1.16.0 as base
ARG SLEEP=15
ARG USERNAME=red_queen
ARG PASSWORD=ciderland5#
COPY --chown=git:git app.ini /data/gitea/conf/
RUN timeout $SLEEP /usr/bin/entrypoint
# Create parameter for username and password
RUN su -c "gitea admin user create --username $USERNAME --password $PASSWORD --email queen@localhost --admin" git
ENV PYTHONUNBUFFERED=1
RUN apk add --update --no-cache python3 py3-pip && \
    ln -sf python3 /usr/bin/python && \
    python3 --version
RUN python3 -m pip install pipenv
COPY Pipfile* /setup/
RUN cd /setup && pipenv install --system --deploy
COPY giteacasc /setup/giteacasc
COPY gitea.yaml /setup/
COPY gitea.yaml /setup/
RUN /usr/bin/entrypoint & \
    sleep $SLEEP && \
    cd /setup && \
    python3 -m giteacasc /setup/gitea.yaml -u $USERNAME -p $PASSWORD

FROM gitea/gitea:1.16.0
COPY --from=base --chown=git:git /data/gitea/gitea.db /data/gitea/gitea.db
COPY --from=base --chown=git:git /data/gitea/conf /data/gitea/conf/
COPY --from=base --chown=git:git /data/git /data/git/
#LABEL version="${TAG}"
