#! /usr/bin/python3

import re

# Compile a regex to match the fund numbers and descriptions
fund_regex = re.compile(r'\s*(\d{4}-\d{2})\s+(\S+\s?\S+\s?\S+\s?\S+\s?\S+\s?\S+\s?\S+)')

with open('Data/CFD Lists/cfds_1516.txt', 'r') as infile:
    with open('Data/CFD Lists/clean_cfds_1516.csv', 'w') as outfile:
        # Write the header to the outfile
        outfile.write('"FUND NUMBER","FUND DESCRIPTION"\n')
        # Iterate through the infile line-by-line
        for line in infile:
            # Determine if the current line has a fund number
            if fund_regex.match(line):
                fund_match = fund_regex.match(line)
                fund_num = fund_match.group(1)
                fund_desc = fund_match.group(2)
                line_out = '"{0}","{1}"\n'.format(fund_num, fund_desc)
                outfile.write(line_out)
