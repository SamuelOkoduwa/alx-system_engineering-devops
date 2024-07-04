# Puppet manifest to configure SSH client settings

# Ensure the SSH configuration directory exists
file { '/home/ubuntu/.ssh':
  ensure  => 'directory',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0700',
  require => Package['openssh-client'],
}

# Manage the SSH client configuration file
file { '/home/ubuntu/.ssh/config':
  ensure  => 'file',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0600',
  content => template('ssh/config.erb'),
  require => File['/home/ubuntu/.ssh'],
}

# Ensure SSH is configured to use the private key and disable password authentication
file_line { 'Declare identity file':
  path    => '/home/ubuntu/.ssh/config',
  line    => '    IdentityFile ~/.ssh/school',
  match   => '^#?\s*IdentityFile\s+~/.ssh/school',
}

file_line { 'Turn off passwd auth':
  path    => '/home/ubuntu/.ssh/config',
  line    => '    PasswordAuthentication no',
  match   => '^#?\s*PasswordAuthentication\s+no',
}

