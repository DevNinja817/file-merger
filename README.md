File Merger
===========

Introduction
------------
This is a simple Python script that takes multiple CSV files as input, merges their data based on IDs, and outputs the result into a single CSV file.

Requirements
------------
- Python 3.7 or later
- No external dependencies. The script only uses Python's built-in modules.

Running the Script
------------------
To run the script, navigate to the directory containing the script in your terminal, then run the following command:
    
- python main.py output.csv small_file_1.csv small_file_2.csv small_file_3.csv small_file_4.csv small_file_5.csv

Observations and Thoughts
-------------------------
This script was an interesting challenge! The merging process is fairly straightforward, but keeping track of the properties for each ID in a way that's both efficient and easy to understand was quite difficult and took some thought. The defaultdict was a lifesaver though 🤣!

I've learnt a fair bit with writing this script.

The performance of this script really largely depends on the size and number of input files. On my computer which is the Apple MBP M1 Max, merging five files with 1000 rows each took about 1.2409687042236328 milliseconds.

Time Spent on the Challenge
---------------------------
It took me approximately just over 2 hours to complete this challenge from start to finish. This includes initial planning, writing the code, testing, and writing this README.
