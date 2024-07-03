# This Puppet manifest installs and configures Nginx with a custom root page and a 301 redirect

# Ensure the Nginx package is installed
package { 'nginx':
  ensure => installed,
}

# Ensure the Nginx service is running and enabled at boot
service { 'nginx':
  ensure     => running,
  enable     => true,
  hasrestart => true,
  require    => Package['nginx'],
}

# Create the custom root page
file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
  require => Package['nginx'],
}

# Create the custom Nginx configuration file using a template
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('nginx/default.erb'),
  require => Package['nginx'],
  notify  => Service['nginx'],
}

