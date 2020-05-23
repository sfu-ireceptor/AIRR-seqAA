import csv
import os
import json
import pandas as pd
import sys

args    = sys.argv[1:]
tsvpath = args[0]
try:
    dataframe = pd.read_csv(tsvpath, sep='\t')
except:
    print("\n\nFile {} not found.".format(tsvpath),
          "\nUsage: python3 tsv_to_json.py [path to tsv file]"
          "\nExiting.\n\n\n")

    raise FileNotFoundError
    exit

out      = dataframe.to_json(orient='records')
jsonpath = tsvpath[:-3]+"json"
with open(jsonpath, 'w') as f:
    f.write(out)
    print("Written successfully to {}".format(jsonpath))
