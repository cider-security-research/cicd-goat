FROM docker:20.10.21-dind
ARG VERSION
ARG COMMIT_SHA

LABEL org.opencontainers.image.vendor="Cider Security" \
    org.opencontainers.image.title="CI/CD Goat - GitLab Runner" \
    org.opencontainers.image.description="Deliberately vulnerable CI/CD environment." \
    org.opencontainers.image.url="https://hub.docker.com/r/cidersecurity/goat-gitlab-runner" \
    org.opencontainers.image.source="https://github.com/cider-security-research/cicd-goat-runner" \
    org.opencontainers.image.licenses="Apache-2.0" \
    org.opencontainers.image.version=$VERSION \
    org.opencontainers.image.revision=$COMMIT_SHA

RUN apk add --no-cache gitlab-runner curl bash
COPY . /setup/
ENTRYPOINT ["/setup/run.sh"]