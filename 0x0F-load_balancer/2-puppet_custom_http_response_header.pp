# This Puppet manifest configures Nginx with a custom HTTP header

node default {
  # Ensure Nginx is installed
  package { 'nginx':
    ensure => installed,
  }

  # Ensure the Nginx service is running
  service { 'nginx':
    ensure     => running,
    enable     => true,
    subscribe  => File['/etc/nginx/sites-available/default'],
  }

  # Configure Nginx with a custom HTTP header
  file { '/etc/nginx/sites-available/default':
    ensure  => file,
    content => template('nginx/default.erb'),
    notify  => Service['nginx'],
  }

  # Create the template for Nginx configuration
  file { '/etc/puppetlabs/code/environments/production/modules/nginx/templates/default.erb':
    ensure  => file,
    content => '
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;

    server_name _;

    location / {
        add_header X-Served-By <%= @hostname %>;
    }
}
',
  }
}

