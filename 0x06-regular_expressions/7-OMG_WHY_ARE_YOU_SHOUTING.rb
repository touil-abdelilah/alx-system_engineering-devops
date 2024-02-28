#!/usr/bin/env ruby

# Function to extract capital letters from the input string
def extract_capital_letters(str)
  # Regular expression to match capital letters
  regex = /[A-Z]/

  # Extract capital letters from the input string
  capital_letters = str.scan(regex).join

  # Print the extracted capital letters
  puts capital_letters
end

# Main code
if ARGV.length != 1
  puts "Usage: #{$PROGRAM_NAME} <string>"
  exit(1)
end

# Get the input string from the command-line argument
input_str = ARGV[0]

# Call the extract_capital_letters method to extract capital letters from the input string
extract_capital_letters(input_str)
