#! /usr/bin/python3

import re

# Compile regexes to match the fund numbers and assessment data
fund_num_regex = re.compile(r'\s*FUND NUMBER\s*(\d{6})')
assessment_data_regex = re.compile(r'\s*\d{3}-\d{3}-\d{2}-\d{2}')

# Pass a blank string to populate the fund_num variable before we process the in-file
fund_num = ''
with open('FCSA 2015-16-p0001 - p51670.txt', 'r') as infile:
    with open('outfile.csv', 'w') as outfile:
        outfile.write('"FUND NUMBER","PARCEL NUMBER","NET FEE"\n')
        # Iterate through the infile line-by-line
        for line in infile:
            # First, determine whether the current line has a fund number
            if fund_num_regex.match(line):
                fund_num_match = fund_num_regex.match(line)
                fund_num = fund_num_match.group(1)
            # If that fails, determine whether the current line has assessment data
            elif assessment_data_regex.match(line):
                # Split the matched lines into columns based on white space
                bits = line.split()
                print("bits = {0}".format(bits))
                # Populate two line_out variables with the fund number and the assessment
                # data for the first and (when applicable) second set of assessment data
                line_out_1 = '"{0}","{1}","{2}"\n'.format(
                    fund_num, bits[0], bits[2])
                outfile.write(line_out_1)
                if len(bits) > 4:
                    line_out_2 = '"{0}","{1}","{2}"\n'.format(
                        fund_num, bits[3], bits[5])
                    outfile.write(line_out_2)
