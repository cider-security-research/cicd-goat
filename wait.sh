#!/bin/bash
for i in {1..120}
do
  gitlab_status_code=$(curl --write-out %{http_code} --silent --output /dev/null "localhost:4000/api/v4/user?access_token=998b5802ec365e17665d832f3384e975")
  if [ "$gitlab_status_code" -eq 200 ]; then
    echo break
    break
  fi
  sleep 5
done