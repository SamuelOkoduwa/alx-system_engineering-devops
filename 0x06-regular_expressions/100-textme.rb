#!/usr/bin/env ruby

# Define a regular expression pattern to extract required information
pattern = /\[from:([\w+\s]+)\] \[to:(\+\d+)\] \[flags:([\d:-]+)\]/

# Loop through each line of the log file provided as an argument
File.open(ARGV[0]).each do |line|
  # Match the pattern against the line
  match_data = line.match(pattern)
  # Output the matched data in the required format
  puts "#{match_data[1]},#{match_data[2]},#{match_data[3]}" if match_data
end

