#!/usr/bin/env ruby

# Function to check if the input string matches the regular expression
def match_pattern(str)
  # Regular expression to match the pattern
  regex = /hbn|hbt{1,}n/

  # Check if the input string matches the regular expression
  if str.match?(regex)
    puts str
  end
end

# Main code
if ARGV.length != 1
  puts "Usage: #{$PROGRAM_NAME} <string>"
  exit(1)
end

# Get the input string from the command-line argument
input_str = ARGV[0]

# Call the match_pattern method to check if the input string matches the regular expression
match_pattern(input_str)

