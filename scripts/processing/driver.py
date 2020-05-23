import map_fields as mapper
from argparse import ArgumentParser
import json
import sys

argparser = ArgumentParser(
    description="Sequential ontology transform for AdaptiveBio -> AIRR")
argparser.add_argument('path', action='store',  default=False)
arguments = argparser.parse_args()

try:
    with open(arguments.path) as infile:
        data = json.load(infile)
except:
    print('Try better.')
    raise FileExistsError


study_sample = data[0]
ssentries    = study_sample.items()
processed    = {
    "airr_compliant": {},

}

for entry in ssentries:
    if entry[0] in mapper.adaptive_to_airr.keys():
        adaptives_key = entry[0]
        [processed['airr_compliant'].update(
            transformed_kvpair) for transformed_kvpair in mapper.adaptive_to_airr[adaptives_key](entry)]
    else:
        processed.update([entry])

with open('transformed_first-pass.json', 'w') as outfile:
    json.dump(processed, outfile)

# TODO:
# 1.Whatever can be extracted automatically is extracted automatically to 'airr_compliant'
# 2.The rest is sent to be curated at the command line with regex search for likely matches in the target schema:
# Not sure how to programmatically curate one-to-many mappings as in "species".
