# Puppet manifest to install Flask package from pip3

# Ensure Python 3 and pip3 are installed
package { ['python3', 'python3-pip']:
  ensure => installed,
}

# Update pip3 package
exec { 'update_pip3':
  command     => '/usr/bin/pip3 install --upgrade pip',
  path        => '/usr/bin',
  refreshonly => true,
}

# Install Flask package with version 2.1.0 using pip3
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Exec['update_pip3'],
}
