FROM jenkins/ssh-agent:4.2.1-jdk11
RUN apt-get update
RUN apt-get -y install git
RUN apt-get -y install build-essential
RUN apt-get -y install python3 python3-pip virtualenv
RUN pip3 install pylint pytest
RUN apt-get -y install curl
RUN pip3 install -U checkov
RUN apt-get install -y npm
RUN npm i npm@7 -g