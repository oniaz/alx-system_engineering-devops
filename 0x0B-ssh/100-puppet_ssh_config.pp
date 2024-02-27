# This Puppet manifest modifies the configuration file to enable authentication without a password using the private key ~/.ssh/school.

file_line { 'add_ssh_config_entry':
  ensure  => present,
  path => '/etc/ssh/ssh_config',
  line => "
    Host *
        IdentityFile ~/.ssh/school
        PasswordAuthentication no
  ",
}
