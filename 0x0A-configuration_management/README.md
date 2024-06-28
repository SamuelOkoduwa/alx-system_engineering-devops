#  0X0A. Configuration Mangement


This project contains Puppet manifests for managing system configurations on Ubuntu 20.04 LTS.

## Tasks

### 0. Create a file

This task involves creating a file at `/tmp/school` with the following attributes:
- File path: `/tmp/school`
- File permission: `0744`
- File owner: `www-data`
- File group: `www-data`
- File content: `I love Puppet`

#### Commands to run:

```bash
puppet-lint 0-create_a_file.pp
sudo puppet apply 0-create_a_file.pp
ls -l /tmp/school
cat /tmp/school

