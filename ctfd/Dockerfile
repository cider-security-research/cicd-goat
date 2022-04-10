FROM ctfd/ctfd:3.4.1
LABEL org.opencontainers.image.vendor="Cider Security" \
    org.opencontainers.image.title="CI/CD Goat - CTFd" \
    org.opencontainers.image.description="Deliberately vulnerable CI/CD environment." \
    org.opencontainers.image.url="https://hub.docker.com/r/cidersecurity/goat-ctfd" \
    org.opencontainers.image.source="https://github.com/cider-security-research/cicd-goat" \
    org.opencontainers.image.licenses="GPL-3.0" \
    org.opencontainers.image.version="${VERSION}" \
    org.opencontainers.image.revision="${COMMIT_SHA}"

COPY --chown=ctfd:ctfd data/CTFd/ctfd.db /opt/CTFd/CTFd/ctfd.db
COPY --chown=ctfd:ctfd data/CTFd/uploads/ /opt/CTFd/CTFd/uploads/
