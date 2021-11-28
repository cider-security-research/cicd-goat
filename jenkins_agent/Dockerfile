FROM jenkins/ssh-agent:4.2.1-jdk11
RUN apt-get update && \
    apt-get -y --no-install-recommends install git \
    build-essential \
    python3 python3-pip virtualenv \
    curl \
    npm && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
RUN pip3 install --no-cache-dir -U pylint pytest checkov
RUN npm i npm@7 -g
LABEL version="${TAG}"