# Changes the ULIMIT for nginx
exec { 'ulimit change':
  command => 'sed -i "s/-n 15/-n 2000/g" /etc/default/nginx; service nginx restart',
  path    => ['/bin', '/usr/sbin', '/usr/bin'],
}
