# This Puppet manifest installs flask Version 2.1.0 and Werkzeug Version 2.1.1 from pip3.

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

# Install Werkzeug as a requirement for Flask
package { 'Werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
  require  => Package['Flask'],
}
