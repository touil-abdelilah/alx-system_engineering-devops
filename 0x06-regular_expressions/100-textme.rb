#!/usr/bin/env ruby
puts File.read(ARGV[0]).scan(/(Sent|Receive) SMS.*?\[from:(.*?)\].*?\[to:(.*?)\].*?\[flags:(.*?)\]/).map { |entry| "#{entry[1]},#{entry[2]},#{entry[3]}" }
