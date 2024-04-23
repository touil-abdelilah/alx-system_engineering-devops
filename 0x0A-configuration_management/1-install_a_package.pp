# Puppet manifest to install Python and Flask package from pip3

# Install Python and pip3
package { ['python3', 'python3-pip']:
  ensure => installed,
}

# Install Flask package using pip3
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['python3-pip'],
}
