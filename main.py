# We need the stuff to allow reading and writing CSV files, the sys for command line arguments, 
# time is to time our script, and defaultdict is for easy dictionary creation.
import csv
import sys
import time
from collections import defaultdict

# Defining our class
class FileMerger:

    def __init__(self, output_path):

        # Thank the lord dictionaries are a thing!
        self.data_set = defaultdict(list)
        self.output_path = output_path

    # This reads a single file
    def read_file(self, filepath):
        # Open up that file and let's get reading
        with open(filepath, 'r') as file:
            read = csv.reader(file)
            next(read)  # We don't care about the header, let's skip it
            # For every row in the file, add its data to our dictionary
            for row in read:
                # The first column is the ID, the rest are just the properties, 
                # it reads the file until there's nothing else more to read
                self.data_set[row[0]].append(row[1])
                
    # This writes a single file
    def write_file(self):
        # Open the output file and get ready to write the data
        with open(self.output_path, 'w', newline='') as file:
            write = csv.writer(file)
            # For each ID in our dictionary, we're going to write a row in the file
            for key, values in self.data_set.items():
                write.writerow([key] + values)

    # We're now merging all the 5 files and their data together
    def merge_files(self, filepaths):
        # For each file, we're gonna read it and process its data
        for filepath in filepaths:
            self.read_file(filepath)
        # Let's write to the output file.
        self.write_file()

def main():
    # We need at least 1 output file and 1 input file. If not, it'll have a paddy and stop.
    if len(sys.argv) < 3:
        print("You forgot to add the output file and at least one input file when running this script!")
        sys.exit(1)  # Stops the script
    # Record users input so the name of the output file and the names of the input files
    output_path = sys.argv[1]
    filepaths = sys.argv[2:]

    # Start up our machine
    merger = FileMerger(output_path)

    # Tracks the time before and after to see how fast the script runs
    start_time = time.time()
    merger.merge_files(filepaths)
    end_time = time.time()

    # Find out how long it took in milliseconds
    total_time = (end_time - start_time) * 1000

    # Display the final results
    print(f"The script took {total_time} milliseconds to merge the data!")

main()