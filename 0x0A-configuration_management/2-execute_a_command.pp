# This manifest kills a process named killmenow using pkill
exec { 'kill_killmenow':
  command => '/usr/bin/pkill killmenow',
  path    => '/usr/bin:/usr/sbin:/bin:/sbin',
}


### 2. Execute a command

This task involves killing a process named `killmenow` using `pkill` through the Puppet `exec` resource.

#### Commands to run:

```bash
puppet-lint 2-execute_a_command.pp
sudo puppet apply 2-execute_a_command.pp
ps aux | grep killmenow

