# data-utilities
This repo holds scripts that were written to accomplish a particular task but will likely come in handy in the future.

CONTENTS

split_cadocs.sh

This shell (Bash) script was written to take a csv file of payments from drug makers and medical device manufactures to California doctors that contained more than 1.1 million records and split it into multiple csv files of at most 200,000 records.

process_assessments.py

This Python script was written to take a minimally formatted text file of annual parcel-level assessment (property tax) data from the San Diego County Auditor and Controller and process it into a clean, comma-separated text file.

process_emissions.py

This Python script was written to take a text file converted from a PDF listing emissions estimates from the San Diego Air Pollution Control District and process it into a clean, comma-separated text file.

mapzen_geocoder.py

This Python script was written to take a comma-separated text file of addresses and geocode them using Mapzen's geocoding service.
