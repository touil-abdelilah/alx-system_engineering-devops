#!/usr/bin/env ruby
puts ARGV[0].scan(/\[from:(.*?)\]|\[to:(.*?)\]|\[flags:(.*?)\]/).map { |match| match.compact.last }.join(',')
