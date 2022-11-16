#!/bin/bash
for i in {1..120}
do
  cmd=`docker logs gitlab | grep 'GitLab is ready!'`
  if [ $? -eq 0 ]; then
    break
  fi
  sleep 5
done