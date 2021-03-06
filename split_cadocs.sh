#!/bin/bash
tail -n +2 cadocs.csv | split -l 200000 - cadocs_ # Grab the master file, from the second line through to the end, split it every 200,000 lines and save those files as 'ca_docs_'
for file in cadocs_* # Iterate through each of the 'cadocs_' files
do
	head -n 1 cadocs.csv > header_file # Grab the first line (the header) of the master file and save that line to a new file (header_file)
	cat $file >> header_file # Concantenate the current 'cadocs_' file to the end of the header file
	mv header_file $file # Rename and save the header file as the current 'cadocs_' file
	mv $file $file.csv # Rename and save the current 'cadocs_' file as 'cadocs_.csv'
	done
