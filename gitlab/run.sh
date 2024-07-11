#!/bin/bash
if test -f "/setup/ready"; then
    echo "GitLab is running"
    /assets/wrapper > /dev/null 2>&1
fi
echo "GitLab is starting..."
set -m
/assets/wrapper > /dev/null 2>&1 &
while true
do
  gitlab_status_code=$(curl --write-out %{http_code} --silent --output /dev/null localhost/users/sign_in )
  if [ "$gitlab_status_code" -eq 200 ]; then
    break
  fi
  sleep 5
done
echo "Starting setup"
gitlab-rails runner "
user = User.find_by_username('root');
user.password = 'ciderland5#';
user.save!;
puts 'root password changed';
token = user.personal_access_tokens.create(scopes: [:api], name: 'Automation token');
token.set_token('60b6c7ba41475b2ebdded2c0d3b079f0');
token.save!;
puts 'root token created';
"
cd /setup
terraform init
terraform apply -target=null_resource.gryphon_sh -auto-approve
terraform apply -auto-approve
./repositories.sh
./resources/gryphon/pygryphon.sh
gitlab-rails runner "
user = User.find_by_username('alice');
token = user.personal_access_tokens.create(scopes: [:api, :read_repository, :write_repository, :read_registry, :write_registry], name: 'testing token');
token.set_token('998b5802ec365e17665d832f3384e975');
token.save!;
puts 'alice token created';
"
cd /
echo "GitLab is ready!" > /setup/ready
echo "GitLab is ready!"
fg # /assets/wrapper
