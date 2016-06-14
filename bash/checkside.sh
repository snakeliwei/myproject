#!/bin/bash

# check the sidekiq process...
ps -fe|grep sidekiq |grep -v grep
if [ $? -ne 0 ]; then
  cd /app
  source /etc/profile.d/rvm.sh
  bundle exec sidekiq -C ./config/sidekiq.yml -d -e production
else
  echo "sidekiq is runing..."
fi
