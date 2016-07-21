#! /usr/bin/python3

import re

# Compile a regex to match the fund numbers
fund_num_regex = re.compile(r'\s*\d{4}-\d{2}')

with open('Data/CFD Lists/cfds_1516.txt', 'r') as infile:
    with open('Data/CFD Lists/clean_cfds_1516.csv', 'w') as outfile:
        # Write the header to the outfile
        outfile.write('"FUND NUMBER","FUND DESCRIPTION"\n')
        # Iterate through the infile line-by-line
        for line in infile:
            # Determine if the current line has a fund number
            if fund_num_regex.match(line):
                # If so, split the matched line into columns based on
                # two or more white space characters
                columns = re.split(r'\s{2,}', line)
                # To ensure all lines begin with the fund number, pass
                # all columns that are not blank to the variable bits
                bits = [column for column in columns if column != '']
                # Print the fund number and fund description to the terminal
                print('"{0}","{1}"'.format(bits[0], bits[1]))
                # Populate a line_out variable with the fund number and
                # fund description and write it to the outfile
                line_out = '"{0}","{1}"\n'.format(bits[0], bits[1])
                outfile.write(line_out)
