#! /usr/bin/python3

import re

# Compile a regex to match the company name
company_regex = re.compile(r'(^.+)\s+source id:', re.IGNORECASE)

# Pass a blank string to populate the company variable before we process the in-file
company = ''
with open('APCD_Emissions_Inventory_Report_2013.txt', 'r') as infile:
    with open('outfile.csv', 'w') as outfile:
        outfile.write('"COMPANY"\n')
        # Iterate through the in-file line-by-line
        for line in infile:
            # First, determine whether the current line has a company name
            if company_regex.match(line):
                company_match = company_regex.match(line)
                company = company_match.group(1)
                # Write all matched companies to a single line
                outfile.write(company)