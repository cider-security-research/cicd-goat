FROM gitea/gitea:1.16.0
COPY --chown=git:git data/gitea/gitea/gitea.db /data/gitea/gitea.db
COPY --chown=git:git data/gitea/gitea/conf /data/gitea/conf/
COPY --chown=git:git data/gitea/git /data/git
LABEL version="${TAG}"
