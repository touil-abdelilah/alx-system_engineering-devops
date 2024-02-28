#!/usr/bin/env ruby -na
puts $F.grep(/from:|to:|flags:/).map{|x| x.split(':')[-1]}.join(',').gsub(/[\[\]]/, '')
