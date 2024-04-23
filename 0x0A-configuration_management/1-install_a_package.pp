# Puppet manifest to install Flask package from pip3

# Ensure Python 3 and pip3 are installed
package { ['python3', 'python3-pip']:
  ensure => installed,
}

# Install Flask package with version 2.1.0 using pip3
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
