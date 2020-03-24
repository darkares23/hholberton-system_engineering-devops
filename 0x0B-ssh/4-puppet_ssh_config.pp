# set up your client SSH configuration file so that you can connect to a server without typing a password.
file_line { 'Remove passwd authentication':
  ensure => 'present',
  path => '/etc/ssh/ssh_config',
  line => 'PasswordAthentication no',
  }
file_line { 'Identity File':
  ensure => 'present',
  path => '/etc/ssh/ssh_config',
  line => 'IdentityFile /home/juan/.ssh/holberton'
}
