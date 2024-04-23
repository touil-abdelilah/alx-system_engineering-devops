# Puppet manifest to install Flask package from pip3

# Ensure Python 3 and pip3 are installed
package { 'python3':
  ensure => installed,
}

package { 'python3-pip':
  ensure => installed,
  require => Package['python3'],
}

# Install Flask package with version 2.1.0 using pip3
exec { 'install_flask':
  command   => '/usr/bin/pip3 install --upgrade Flask==2.1.0',
  path      => '/usr/bin',
  unless    => '/usr/bin/pip3 show Flask | grep -q "Version: 2.1.0"',
  provider  => 'shell',
}
