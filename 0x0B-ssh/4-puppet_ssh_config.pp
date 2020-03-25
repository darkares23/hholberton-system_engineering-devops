# set up your client SSH configuration file so that you can connect to a server without typing a password.
file_line { 'Remove passwd authentication':
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAthentication no',
  match  => 'PasswordAuthentication yes',
  }
file_line { 'Identity File':
  path => '/etc/ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/holberton',
}
