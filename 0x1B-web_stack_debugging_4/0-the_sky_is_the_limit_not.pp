# This Puppet manifest updates the ULIMIT value

exec { 'update-ulimit':
  command => "sed -i 's/^ULIMIT=.*/ULIMIT=\"-n 65535\"/' /etc/default/nginx",
  path    => ['/bin', '/usr/bin'],
}

-> exec { 'restart-nginx':
  command  => 'service nginx restart',
  provider => 'shell',
}