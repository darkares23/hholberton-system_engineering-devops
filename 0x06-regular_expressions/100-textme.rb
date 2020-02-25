#!/usr/bin/env ruby
puts ARGV[0].scan(/\[from:(.*?)\]/).join(",")
puts ARGV[0].scan(/\[to:(.*?)\]/).join(separator=",")
puts ARGV[0].scan(/\[flags:(.*?)\]/).join
