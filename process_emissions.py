#! /usr/bin/python3

import re

# Compile regexes to match the company names and source IDs, street addresses,
# city and state, pollutant criteria types and pollutants data
company_regex = re.compile(r'(.+)\s*Source ID: ([0-9]*)', re.IGNORECASE)
address_regex = re.compile(r'(.+)\s+Contact:')
city_state_regex = re.compile(r'(.+)\s+Phone Number:')
criteria_type_regex = re.compile(r'^(Pollutant|Contaminant)', re.IGNORECASE)
pollutant_regex = re.compile(r'\d+\.\d+')

with open('Emissions Reports/APCD_Emissions_Inventory_Report_2012.txt', 'r') as infile:
    with open('2012 Emissions Data/emissions12.csv', 'w') as outfile:
        # Write the headers to the outfile
        outfile.write('"Company Name", "Source ID", "Company Address", "Criteria Type", "Pollutant", "Annual Emissions", "Max Hourly Emissions"\n')
        # Iterate through the in-file line-by-line
        for line in infile:
            # First, search the current line for a company name and source ID
            # and pass what is returned to the variable company_match
            company_match = company_regex.search(line)
            # Then, determine if the current line has a company name and source ID
            if company_match:
                # Pass the company name to the variable name and strip whitespace
                name = company_match.group(1).strip()
                # Pass the source ID to the variable source_id
                source_id = company_match.group(2)
            # Next, search the current line for a street address and pass what is
            # returned to the variable address_match
            address_match = address_regex.search(line)
            # Then, determine if the current line has a street address
            if address_match:
                # Pass the street address to the variable address and strip whitespace
                address = address_match.group(1).strip()
            # Next, search the current line for a city and state and pass what is
            # returned to the variable city_state_match
            city_state_match = city_state_regex.search(line)
            # Then, determine if the current line has a city and state
            if city_state_match:
                # Concatenate the city and state to the variable address and strip whitespace
                address += " {0}".format(city_state_match.group(1).strip())
            # Next, search the current line for criteria type and pass what is
            # returned to the variable criteria_type_match
            criteria_type_match = criteria_type_regex.search(line)
            # Then, determine if the current line has a criteria type
            if criteria_type_match:
                # Pass the criteria type to the variable criteria_type
                criteria_type = criteria_type_match.group(1)
            # Finally, search the current line for pollutants data and pass what is
            # returned to the variable pollutant_match
            pollutant_match = pollutant_regex.search(line)
            # Next, determine if the current line has pollutants data
            if pollutant_match:
                # Split the line into columns based on two or more white space characters
                # and pass it to the variable result
                result = re.split(r'\s{2,}', line)
                # Pass the pollutant name to the variable pollutant
                pollutant = result[0]
                # Then, determine if the current line has only three columns
                if len(result) == 3:
                    # Pass the second column to the variable annual
                    annual = result[1]
                    # Pass the third column to the variable hourly
                    hourly = result[2]
                # Then, determine if the current line has more than three columns
                elif len(result) > 3:
                    # Then, determine if the second column is equal to the less than character
                    if result[1] == '<':
                        # Concatenate the second and third columns and pass the result
                        # to the variable annual
                        annual = result[1] + ' ' + result[2]
                    # Otherwise, pass the second column to the variable annual
                    else:
                        annual = result[1]
                    # Then, determine if the fourth column is equal to the less than character
                    if result[3] == '<':
                        # Concatenate the fourth and fifth columns and pass the result
                        # to the variable hourly
                        hourly = result[3] + ' ' + result[4]
                    # Otherwise, pass the fourth column to the variable hourly
                    else:
                        hourly = result[3]
                # Pass the company name, source ID, address, criteria type, pollutant name,
                # annual data and hourly data to the variable line_out
                line_out = '"{0}", "{1}", "{2}", "{3}", "{4}", "{5}", "{6}"\n'.format(name,
                    source_id, address, criteria_type, pollutant, annual, hourly)
                # Print the line_out variable to the terminal
                print(line_out)
                # Write the line_out variable to the outfile
                outfile.write(line_out)
