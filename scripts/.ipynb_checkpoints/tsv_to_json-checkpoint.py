# Authors: Artem Kushner, Laura Gutierrez Funderburk
# Date created: May 22 2020
# Date last modified: May 22 2020

import csv
import os
import json
import pandas as pd
import sys
import argparse

def getArguments():
    # Set up the command line parser
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=""
    )

    # Output Directory - where Performance test results will be stored 
    parser.add_argument(
        "TSV_file",
        help="Indicate the full path to where the TSV from adaptive file is found"
    )
    
    # Verbosity flag
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Run the program in verbose mode.")

    # Parse the command line arguements.
    options = parser.parse_args()
    return options


    
if __name__ == "__main__":
    
    options = getArguments()
    tsv_file = options.TSV_file
    
    try:
        dataframe = pd.read_csv(tsv_file, sep='\t')
    except:
        print("\n\nFile {} not found.".format(tsvpath),
              "\nUsage: python3 tsv_to_json.py [path to tsv file]"
              "\nExiting.\n\n\n")

        raise FileNotFoundError
        exit

    out = dataframe.to_json(orient='records')
    jsonpath = tsv_file[:-3]+"json"
    with open(jsonpath, 'w') as f: 
        f.write(out)
        print("Written successfully to {}".format(jsonpath))
        
    f.close()

    with open(jsonpath) as f:
        data = json.loads(f.read())
    f.close()

    