# This Puppet manifest creates a file with content "I love Puppet", permissions '0744', owner 'www-data', and group "www-data".

file { '/tmp/school':
  ensure  => file,
  content => 'I love Puppet',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
}
