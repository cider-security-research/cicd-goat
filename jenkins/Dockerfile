FROM jenkins/jenkins:2.320
USER root
RUN apt-get update && apt-get install -y --no-install-recommends \
       apt-transport-https \
       ca-certificates curl gnupg2 \
       software-properties-common

COPY jenkins_home /var/jenkins_home
RUN chown -R jenkins /var/jenkins_home
RUN chmod -R 700 /var/jenkins_home
USER jenkins
