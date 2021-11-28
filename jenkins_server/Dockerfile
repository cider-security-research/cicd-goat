FROM jenkins/jenkins:2.320
USER root
# RUN apt-get update && apt-get install -y --no-install-recommends \
#       apt-transport-https \
#       ca-certificates curl gnupg2 \
#       software-properties-common && \
#       apt-get autoremove -y && \
#       apt-get clean && \
#       rm -rf /var/lib/apt/lists/*
COPY jenkins_home /var/jenkins_home
RUN chmod -R 700 /var/jenkins_home

FROM jenkins/jenkins:2.320
COPY --from=0 --chown=jenkins:jenkins /var/jenkins_home /var/jenkins_home
USER jenkins
LABEL version="${TAG}"