#!/bin/bash
/usr/bin/tini -- /usr/local/bin/jenkins.sh &
while true
do
  jenkins_status_code=$(curl --write-out %{http_code} --silent --output /dev/null localhost/login )
  if [ "$jenkins_status_code" -eq 200 ]; then
    break
  fi
  sleep 5
done
rm -rf /var/jenkins_home/jobdsl
rm /var/jenkins_home/secrets.properties
rm /var/jenkins_home/jenkins.yaml
fg
