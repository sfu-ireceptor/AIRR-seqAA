#!/usr/bin/env python
# Authors: Nicole Knoetze, Laura Gutierrez Funderburk
# Date created: May 23 2020
# Date last modified: May 23 2020

import pandas as pd
import sys
import argparse

def getArguments():
    # Set up the command line parser
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=""
    )

    # TSV Directory - where TSV file will be stored 
    parser.add_argument(
        "TSV_file",
        help="Indicate the full path to where the TSV from adaptive file is found"
    )
    
    # Mapping Directory - where mapping file will be stored 
    parser.add_argument(
        "map_file",
        help="Indicate the full path to where the TSV from adaptive file is found"
    )
    
    # TAG Directory - where tagging file will be stored 
    parser.add_argument(
        "tag_file",
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
    
    # Read file
    options = getArguments()
    tsv_file = options.TSV_file
    mapp_f = options.map_file
    tagg_f = options.tag_file
    
    
    # Store as pandas dataframe
    mapping_df = pd.read_csv(mapp_f,sep="\t")
    tagging_df = pd.read_csv(tagg_f,sep="\t")
    tsv_immonuseq = pd.read_csv(tsv_file,sep="\t")
    
    print("Mapping")
    display(mapping_df.head())
    
    print("Tagging")
    display(tagging_df.head())
    
    print("ImmunoSeq DF")
    display(tsv_immonuseq.head())

    # explore entries in sample_catalog_tags
    values = []
    for item in tsv_immonuseq["sample_catalog_tags"].to_list():
        #print(item.split("Cluster of Differentiation (CD):"))
        values.append(item.split("Cluster of Differentiation (CD):")[1:3])

        # NEED TO SPLIT VALUES INTO APPROPRIATE AIRR NAME
