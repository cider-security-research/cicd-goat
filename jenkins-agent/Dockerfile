FROM jenkins/ssh-agent:4.1.0-jdk11 AS base
LABEL org.opencontainers.image.vendor="Cider Security" \
    org.opencontainers.image.title="CI/CD Goat - Jenkins agent" \
    org.opencontainers.image.description="Deliberately vulnerable CI/CD environment." \
    org.opencontainers.image.url="https://hub.docker.com/r/cidersecurity/goat-jenkins-agent" \
    org.opencontainers.image.source="https://github.com/cider-security-research/cicd-goat" \
    org.opencontainers.image.licenses="GPL-3.0" \
    org.opencontainers.image.version="${VERSION}" \
    org.opencontainers.image.revision="${COMMIT_SHA}"

RUN apt-get update && \
    apt-get -y --no-install-recommends install python3 python3-pip \
    curl \
    git
# Install Terraform
RUN curl -OL https://golang.org/dl/go1.16.7.linux-amd64.tar.gz && \
    tar -C /usr/local -xvf go1.16.7.linux-amd64.tar.gz && \
    export PATH=$PATH:/usr/local/go/bin && \
    git clone https://github.com/hashicorp/terraform.git && \
    cd terraform && \
    go install
# Install Python packages
RUN python3 -m pip install --user --no-cache-dir -U pylint pytest checkov awscli-local

FROM jenkins/ssh-agent:4.1.0-jdk11
RUN apt-get update && \
    apt-get -y --no-install-recommends install unzip python3 virtualenv npm git curl jq make && \
    curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && \
    unzip awscliv2.zip && \
    apt-get -y purge unzip && \
    /home/jenkins/aws/install && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /home/jenkins/aws && \
    rm awscliv2.zip
COPY --from=base --chown=jenkins:jenkins /root/.local /home/jenkins/.local
COPY --from=base /usr/bin/terraform /usr/bin/terraform
