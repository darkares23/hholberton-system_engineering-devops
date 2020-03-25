# set up your client SSH configuration file so that you can connect to a server without typing a password.
file_line { 'holberton':
  path => '/etc/ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/holberton',
}
file_line { 'password':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no',
  match  => 'PasswordAuthentication yes',
}
