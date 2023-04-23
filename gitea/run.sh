#!/bin/bash
set -m
USERNAME=red_queen
PASSWORD=ciderland5#
/usr/bin/entrypoint &
while true
do
  gitea_status_code=$(curl --write-out %{http_code} --silent --output /dev/null localhost:3000/ )
  if [ "$gitea_status_code" -eq 200 ]; then
    echo "Gitea ready. Continue with setup..."
    break
  fi
  echo "Gitea is not ready. Waiting 5 seconds..."
  sleep 5
done
su -c "gitea admin user create --username $USERNAME --password $PASSWORD --email queen@localhost --admin" git
cd /setup
python3 -m giteacasc /setup/gitea.yaml -u $USERNAME -p $PASSWORD
fg #/usr/bin/entrypoint