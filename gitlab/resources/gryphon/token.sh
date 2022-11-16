#!/bin/bash

gitlab-rails runner "
user = User.find_by_username('gryphon');
token = user.personal_access_tokens.create(scopes: [:api], name: 'Automation token');
token.set_token('8225526e2656be28b1dfdcb48988746c');
token.save!;
citoken = user.personal_access_tokens.create(scopes: [:write_registry, :read_registry], name: 'CI token');
citoken.set_token('04b6bdf425dbd720a34705a398500937');
citoken.save!;
rtoken = user.personal_access_tokens.create(scopes: [:read_api], name: 'read token');
rtoken.set_token('cd79dd622c6d463a574635e874765c0b');
rtoken.save!;
puts 'gryphon tokens created';
"