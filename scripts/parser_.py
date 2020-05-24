#!/usr/bin/env python
# Authors: Artem Kushner, Nicole Knoetze, Laura Gutierrez Funderburk
# Date created: May 23 2020
# Date last modified: May 24 2020

import pandas as pd
import sys
import argparse

def map_species(kvpair):
    # Would be great to have a reliable mapping betwen a common name to the taxonomic identifiers
    # Doing just human for now.

    species = str.upper(kvpair)

    taxonomicIds = {
          "HUMAN"    : ("Homo Sapiens", 9606),
          "MOUSE"    : ("Mus musacris", 10090),
          "ZEBRAFISH": ("Danio rerio", 7955),
          "E. COLI"  : ("Escherichia coli", 562),
          "FRUITFLY" : ("Drosophilia melanogaster", 7227),
        # ...        : ...
    }

    if str.upper(species) in taxonomicIds.keys():
        return [
            {
                "species.id": taxonomicIds[species][1]
            },
            {
                "species.label": taxonomicIds[species][0]
            }
        ]
    else:
        print(
            "Species [ {} ] does not have a defined mapping to id/tax.".format(species))
        return 1

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
        help="Indicate the full path to where the mapping file is found"
    )
    
    # TAG Directory - where tagging file will be stored 
    parser.add_argument(
        "tag_file",
        help="Indicate the full path to where the tagging file is found"
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
    display(mapping_df)
    
    print("Tagging")
    display(tagging_df.head())
    
    print("ImmunoSeq DF")
    display(tsv_immonuseq.head())

    taxonomicIds = {
          "HUMAN"    : ("Homo Sapiens", 9606),
          "MOUSE"    : ("Mus musacris", 10090),
          "ZEBRAFISH": ("Danio rerio", 7955),
          "E. COLI"  : ("Escherichia coli", 562),
          "FRUITFLY" : ("Drosophilia melanogaster", 7227),
        # ...        : ...
    }
    
    
    # rename columns using mapping
    new_col_dic = {}

    for item in mapping_df["Adaptive-name"].to_list():
        if type(mapping_df[mapping_df["Adaptive-name"]==item]["AIRR-name"].to_list()[0])==float:
            continue
        else:
            new_col_dic[item] = (mapping_df[mapping_df["Adaptive-name"]==item]["AIRR-name"].to_list()[0])

    new_col_dic["sample_id"] ="_id"
    
    # handle species tagging 
    species_id = []
    species_label = []
    for item in tsv_immonuseq["species"].to_list():

        species_id.append(map_species(item)[0]["species.id"])
        species_label.append(map_species(item)[1]['species.label'])

    tsv_immonuseq["species.id"] = species_id

    tsv_immonuseq["species.label"] = species_label
    
    # column renaming
    # drop species
    tsv_immonuseq = tsv_immonuseq.drop(['species'], axis=1)
    
    # rename others
    tsv_immonuseq = tsv_immonuseq.rename(columns=new_col_dic)
    
    print("Converted ImmunoSeq DF")
    display(tsv_immonuseq.head())

