FROM jenkins/jenkins:2.320
ENV JAVA_OPTS "-Djenkins.install.runSetupWizard=false"
ENV SECRETS_FILE /var/jenkins_home/secrets.properties
ENV CASC_JENKINS_CONFIG /var/jenkins_home/casc.yaml
COPY --chown=jenkins:jenkins secrets.properties /var/jenkins_home/secrets.properties
COPY --chown=jenkins:jenkins casc.yaml /var/jenkins_home/casc.yaml
COPY --chown=jenkins:jenkins plugins.txt /usr/share/jenkins/ref/plugins.txt
RUN jenkins-plugin-cli --clean-download-directory -f /usr/share/jenkins/ref/plugins.txt
COPY --chown=jenkins:jenkins jobdsl/ /var/jenkins_home/jobdsl/
LABEL version="${TAG}"