$path = "/tmp/school"

file { $path:
 ensure => "file",
 owner => "www-data",
 group => "www-data",
 mode => 744
}

file { $path:
 ensure => "present",
 content => "I love Puppet",
 require => File[$path]
}
