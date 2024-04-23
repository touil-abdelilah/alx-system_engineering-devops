class python {
  package { 'python3':
    ensure => installed,
  }
}

# Install Flask 2.1.0 with pip3 on Ubuntu 20.04

class { 'python': }

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Class['python'],
}

package { 'python3-pip':
  ensure => installed,
}

