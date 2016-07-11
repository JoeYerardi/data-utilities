#! /usr/bin/python3

import csv
import re

# Compile a regex to match the company name
company_regex = re.compile(r"^(.+)\s+Source ID: ([0-9]*)$", re.IGNORECASE)
address_regex = re.compile(r"^(.+)\s+Contact:")
zip_regex = re.compile("^(.+)\s+Phone Number:")
pollutant_regex = re.compile("""^Carbon Monoxide \(CO\)|Nitrogen Oxides \(NOx\)|
Particulate Matter \(PM10\)|Reactive Organic Gases \(ROG\)|Sulfur Oxides \(SOx\)|
Total Organic Gases \(TOG\)""")

last_company = ''
# Pass a blank string to populate the company variable before we process the in-file
with open('APCD_Emissions_Inventory_Report_2013.txt', 'r') as infile:
    with open('outfile.csv', 'w') as outfile:
        outfile.write('"Company", "Source ID", "Address", "Criteria", "Annual Emissions", "Max Hourly Emissions"\n')
        # Iterate through the in-file line-by-line
        company = ''
        source_id = ''
        address = ''
        zip_code = ''
        for line in infile:
            # First, determine whether the current line has a company name
            company_match = company_regex.search(line)
            if company_match:
                company = company_match.group(1).strip()
                source_id = company_match.group(2)
            address_match = address_regex.search(line)
            if address_match:
                address = address_match.group(1).strip()
            zip_match = zip_regex.search(line)
            if zip_match:
                address += " {0}".format(zip_match.group(1).strip())
            pollutant_match = pollutant_regex.search(line)
            if pollutant_match:
                print('{0}\n'.format(line))
                result = re.split(r"(?i)\s{2,}", line)
                pollutant = result[0]
                annual = result[1]
                hourly = result[2]
                # Write all matched companies to a single line
                outfile.write('"{0}", {1}, "{2}", "{3}", {4}, {5}\n'.format(company,
                    source_id, address, pollutant, annual, hourly))
