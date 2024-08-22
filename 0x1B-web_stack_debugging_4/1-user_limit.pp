# Increase the file descriptor limit for the holberton user

exec { 'change-os-configuration-for-holberton-user':
  path => '/bin/bash',
  command => 'echo "ulimit -n 65536" >> /home/holberton/.bashrc',
  creates => '/home/holberton/.bashrc',
}
