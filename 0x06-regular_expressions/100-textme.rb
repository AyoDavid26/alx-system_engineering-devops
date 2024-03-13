#!/usr/bin/env ruby
# Regular Expressions task

puts ARGV[0].scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/).join(",")
