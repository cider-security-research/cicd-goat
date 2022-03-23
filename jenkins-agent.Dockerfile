FROM jenkins/ssh-agent:4.1.0-jdk11 AS base
RUN apt-get update && \
    apt-get -y --no-install-recommends install python3.9 python3-pip \
    curl \
    build-essential \
    gnupg \
    lsb-release \
    unzip \
    software-properties-common
RUN curl -fsSL https://apt.releases.hashicorp.com/gpg | apt-key add - && \
    apt-add-repository "deb [arch=amd64] https://apt.releases.hashicorp.com $(lsb_release -cs) main" && \
    apt-get update && apt-get -y --no-install-recommends install terraform
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && \
    unzip awscliv2.zip && \
    ./aws/install
RUN python3.9 -m pip install --user --no-cache-dir -U pylint pytest checkov awscli-local

FROM jenkins/ssh-agent:4.1.0-jdk11
RUN apt-get update && \
    apt-get -y --no-install-recommends install python3.9 virtualenv npm git curl jq && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
COPY --from=base --chown=jenkins:jenkins /root/.local /home/jenkins/.local
COPY --from=base /usr/local/bin/aws /usr/local/bin/aws
COPY --from=base /usr/bin/terraform /usr/bin/terraform
COPY --from=base /usr/bin/jq /usr/bin/jq
LABEL version="${TAG}"