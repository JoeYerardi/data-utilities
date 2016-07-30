#! /usr/bin/python3

import re

# Compile regexes to match fund numbers, assessment data with the SZE column blank   
# and assessment data with the SZE column not blank
fund_num_regex = re.compile(r'\s*FUND NUMBER\s*(\d{6})')
assessment_data_regex_no_sze = re.compile(r'\s*\d{3}-\d{3}-\d{2}-\d{2}')
assessment_data_regex_sze = re.compile(r'\s*\w{1}\s*\d{3}-\d{3}-\d{2}-\d{2}')

with open('Data/Assessments Data/assessments_1516.txt', 'r') as infile:
    with open('Data/Assessments Data/clean_assessments_1516.csv', 'w') as outfile:
        # Write the headers to the outfile
        outfile.write('"FUND NUMBER","PARCEL NUMBER","NET FEE"\n')
        # Iterate through the infile line-by-line
        for line in infile:
            # First, determine if the current line has a fund number
            if fund_num_regex.match(line):
                fund_num_match = fund_num_regex.match(line)
                fund_num = fund_num_match.group(1)
            # If that fails, determine if the current line has assessment data with 
            # the SZE column blank
            elif assessment_data_regex_no_sze.match(line):
                # Split the matched line into columns based on white space
                columns = line.split()
                # Pass all columns other than odd cent (those equal to .01)
                # to the variable bits
                bits = [column for column in columns if column != '.01']
                # Pass the fund number, parcel number and net fee from the first
                # (or only) set of assessment data to the variable line_out_1
                line_out_1 = '"{0}","{1}","{2}"\n'.format(fund_num, bits[0], bits[2])
                # Print the line_out_1 variable to the terminal
                print(line_out_1)
                # Write the line_out_1 variable to the outfile
                outfile.write(line_out_1)
                # Determine if the current line has a second set of assessment data
                if len(bits) > 3:
                    # Pass the fund number, parcel number and net fee from the
                    # second set of assessment data to the variable line_out_2
                    line_out_2 = '"{0}","{1}","{2}"\n'.format(fund_num, bits[3], bits[5])
                    # Print the line_out_2 variable to the terminal
                    print(line_out_2)
                    # Write the line_out_2 variable to the terminal
                    outfile.write(line_out_2)
            # If that fails, determine if the current line has assessment data with 
            # the SZE column not blank
            elif assessment_data_regex_sze.match(line):
                # Split the matched line into columns based on white space
                columns = line.split()
                # Pass all columns other than odd cent (those equal to .01)
                # to the variable bits
                bits = [column for column in columns if column != '.01']
                # Determine if the current line has a Z in the SZE column
                if bits[0] == 'Z':
                	# Pass the fund number, parcel number and net fee from the first
                    # (or only) set of assessment data to the variable line_out_1
                    line_out_1 = '"{0}","{1}","{2}"\n'.format(fund_num, bits[1], bits[3])
                    # Write the line_out_1 variable to the outfile
                    outfile.write(line_out_1)
                    # Print the line_out_1 variable to the terminal
                    print(line_out_1)
                    # Determine if the current line has a second set of assessment data
                    if len(bits) > 4:
                        # Pass the fund number, parcel number and net fee from the
                        # second set of assessment data to the variable line_out_2
                        line_out_2 = '"{0}","{1}","{2}"\n'.format(fund_num, bits[4], bits[6])
                        # Print the line_out_2 variable to the terminal
                        print(line_out_2)
                        # Write the line_out_2 variable to the terminal
                        outfile.write(line_out_2)
                # Determine if the current line has an S in the SZE column
                elif bits[0] == 'S':
                	# Pass the fund number, parcel number and net fee from the first 
                	# (or only) set of assessment data to the variable line_out_2
                    line_out_1 = '"{0}","{1}","{2}"\n'.format(fund_num, bits[1], bits[4])
                    # Write the line_out_1 variable to the outfile
                    outfile.write(line_out_1)
                    # Print the line_out_1 variable to the terminal
                    print(line_out_1)
                    # Determine if the current line has a second set of assessment data
                    if len(bits) > 5:
                        # Pass the fund number, parcel number and net fee from the
                        # second set of assessment data to the variable line_out_2
                        line_out_2 = '"{0}","{1}","{2}"\n'.format(fund_num, bits[5], bits[7])
                        # Print the line_out_2 variable to the terminal
                        print(line_out_2)
                        # Write the line_out_2 variable to the terminal
                        outfile.write(line_out_2)
