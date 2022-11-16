FROM gitlab/gitlab-ee:15.4.2-ee.0 AS base
ARG VERSION
ARG COMMIT_SHA

LABEL org.opencontainers.image.vendor="Cider Security" \
    org.opencontainers.image.title="CI/CD Goat - GitLab" \
    org.opencontainers.image.description="Deliberately vulnerable CI/CD environment." \
    org.opencontainers.image.url="https://hub.docker.com/r/cidersecurity/goat-gitlab" \
    org.opencontainers.image.source="https://github.com/cider-security-research/cicd-goat" \
    org.opencontainers.image.licenses="Apache-2.0" \
    org.opencontainers.image.version=$VERSION \
    org.opencontainers.image.revision=$COMMIT_SHA

# Install Terraform
RUN apt-get update && apt-get install -y lsb-release gnupg software-properties-common && \
    wget -O- https://apt.releases.hashicorp.com/gpg | \
    gpg --dearmor | \
    tee /usr/share/keyrings/hashicorp-archive-keyring.gpg && \
    gpg --no-default-keyring \
    --keyring /usr/share/keyrings/hashicorp-archive-keyring.gpg \
    --fingerprint && \
    echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] \
    https://apt.releases.hashicorp.com $(lsb_release -cs) main" | \
    tee /etc/apt/sources.list.d/hashicorp.list && \
    apt update && \
    apt-get install terraform=1.3.4

# Install Docker CLI
RUN apt-get install -y ca-certificates curl && \
    mkdir -p /etc/apt/keyrings && \
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg && \
    echo \
      "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
      $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null && \
    apt-get update && \
    apt-get install -y docker-ce-cli

RUN pip3 install --user --no-cache-dir twine==4.0.1

FROM gitlab/gitlab-ee:15.4.2-ee.0
COPY --from=base /root/.local /root/.local
COPY --from=base /usr/bin/terraform /usr/bin/terraform
COPY --from=base /usr/bin/docker /usr/bin/docker
# openssl req -x509 -newkey rsa:4096 -sha256 -days 3560 -nodes -keyout server.key -out server.crt -subj "/CN=gitlab" -extensions san -config <(echo '[req]';echo 'distinguished_name=req';echo '[san]'; echo 'subjectAltName=DNS:gitlab')
COPY cert/server.crt etc/gitlab/ssl/gitlab.crt
COPY cert/server.key /etc/gitlab/ssl/gitlab.key
COPY . /setup/
RUN /setup/check_git.py

CMD ["/setup/run.sh"]
