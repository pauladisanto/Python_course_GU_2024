import csv # Import the csv module to read the input CSV file 

path_to_the_file = '/Users/xdisga/Downloads/Python_for_biologists/'# Open the CSV file using your path

with open(path_to_the_file + 'brca_cnvs_tcga-1-2.csv', mode='r') as infile, \
     open(path_to_the_file + 'file_with_new_column.csv', mode='w', newline='') as outfile:

    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # Read the header and append "seq_length" to it
    header = next(reader)
    header.append('seq_length')
    writer.writerow(header)

    # Process each row, calculate seq_length, and write it to the new file
    for row in reader:
        loc_start = int(row[2])  # loc.start is in the 3rd column
        loc_end = int(row[3])    # loc.end is in the 4th column
        seq_length = loc_end - loc_start # Calculate the sequence length
        row.append(seq_length) # Append the calculated seq_length to the row
        writer.writerow(row)   # Write the row to the new file



 