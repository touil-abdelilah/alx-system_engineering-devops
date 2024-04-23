# Puppet manifest to kill a process named killmenow

exec { 'killmenow':
  command => 'killall -q -SIGTERM killmenow',
  path    => '/usr/bin',
}

