#Using Puppet, create a file in `/tmp`.
file {'tmp/holberton':
  path    => '/tmp/holberton',
  content => 'I love Puppet',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
}
