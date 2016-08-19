#unicorn config
app_path = "/app"
pid "#{app_path}/tmp/pids/unicorn.pid"
stderr_path "#{app_path}/log/unicorn.log"
stdout_path "#{app_path}/log/unicorn.log"

# rails env
rails_env = ENV['RAILS_ENV'] || 'production'
# rails_env = ENV['RAILS_ENV'] || 'develop'

worker_processes (rails_env == 'production' ? 4 : 2)

# Restart any workers that haven't responded in 30 seconds
timeout 30

# Listen on a Unix data socket
listen "#{app_path}/tmp/sockets/unicorn.sock", :backlog => 2048
listen 8091, :tcp_nopush => false

preload_app true

before_exec do |server|
  ENV['BUNDLE_GEMFILE'] = "#{app_path}/Gemfile"
end

before_fork do |server, worker|
  defined?(ActiveRecord::Base) and
    ActiveRecord::Base.connection.disconnect!
end

after_fork do |server, worker|
  defined?(ActiveRecord::Base) and
    ActiveRecord::Base.establish_connection
end
