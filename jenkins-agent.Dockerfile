FROM jenkins/ssh-agent:4.1.0-jdk11
RUN apt-get update && \
    apt-get -y --no-install-recommends install git \
    build-essential \
    python3 python3-pip virtualenv \
    curl \
    npm \
    gnupg \
    lsb-release \
    unzip \
    jq \
    software-properties-common && \
    curl -fsSL https://apt.releases.hashicorp.com/gpg | apt-key add - && \
    apt-add-repository "deb [arch=amd64] https://apt.releases.hashicorp.com $(lsb_release -cs) main" && \
    apt-get update && apt-get -y --no-install-recommends install terraform&& \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && \
    unzip awscliv2.zip && \
    ./aws/install
RUN pip3 install --no-cache-dir -U pylint pytest checkov awscli-local
RUN npm i npm@7 -g
LABEL version="${TAG}"