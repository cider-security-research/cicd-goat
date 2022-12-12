#!/bin/bash
echo "Waiting for GitLab to setup..."
while true
do
  gitlab_status_code=$(curl --write-out %{http_code} --silent --output /dev/null gitlab/users/sign_in )
  if [ "$gitlab_status_code" -eq 200 ]; then
    break
  fi
  sleep 1
done
dockerd --tls=false &
gitlab-runner register --non-interactive -url "http://gitlab" --registration-token "GR1348hansd87fyzDiqyZeuHuxe" --executor "docker" --docker-image alpine:3.16.3 --docker-network-mode host
gitlab-runner run
