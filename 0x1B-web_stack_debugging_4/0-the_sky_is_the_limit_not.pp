# Increase the number of worker processes in Nginx to improve performance
# under load

class nginx::config {
  file { '/etc/nginx/nginx.conf':
    ensure => present,
    owner => 'root',
    group => 'root',
    mode => '0644',
    content => template('nginx::config/nginx.conf.erb'),
  }
}

nginx::config::params { 'worker_processes':
  value => 4,  # Adjust the number of workers as needed
}

service { 'nginx':
  ensure => running,
  enable => true,
}
