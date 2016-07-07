#! /usr/bin/python3
​
import re
​
# The line
line = '''SOURCE EMISSIONS
2013 EMISSIONS INVENTORY REPORT
CANYON ROCK - MISSION GORGE       Source ID: 27
7500 MISSION GORGE RD             Contact: BROUWER'''
​
# Compile a regex to find the line containing the company name
company_regex = re.compile(r'(^.+)\s+source id: ', re.IGNORECASE | re.MULTILINE)
​
# Run the regex on the line
company_match = company_regex.match(line)
​
# Return the company name
company = company_match.group(1)
​
# Print the company name
print(company)