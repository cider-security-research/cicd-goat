FROM jenkins/jenkins:2.332.1-jdk11
#ARG COMMIT_SHA
#ARG VERSION
ENV JAVA_OPTS "-Djenkins.install.runSetupWizard=false"
ENV SECRETS_FILE /var/jenkins_home/secrets.properties
ENV CASC_JENKINS_CONFIG /var/jenkins_home/casc.yaml
COPY --chown=jenkins:jenkins flag5.txt /var/jenkins_home/flag5.txt
COPY --chown=jenkins:jenkins plugins.txt /usr/share/jenkins/ref/plugins.txt
RUN jenkins-plugin-cli --clean-download-directory -f /usr/share/jenkins/ref/plugins.txt
COPY --chown=jenkins:jenkins secrets.properties /var/jenkins_home/secrets.properties
COPY --chown=jenkins:jenkins casc.yaml /var/jenkins_home/casc.yaml
COPY --chown=jenkins:jenkins jobdsl/ /var/jenkins_home/jobdsl/
#LABEL org.opencontainers.image.vendor="Jenkins project" \
#    org.opencontainers.image.title="Official Jenkins SSH Agent Docker image" \
#    org.opencontainers.image.description="A Jenkins agent image which allows using SSH to establish the connection" \
#    org.opencontainers.image.url="https://www.jenkins.io/" \
#    org.opencontainers.image.source="https://github.com/jenkinsci/docker-ssh-agent" \
#    org.opencontainers.image.licenses="MIT" \
#    org.opencontainers.image.version="${VERSION}" \
#    org.opencontainers.image.revision="${COMMIT_SHA}"