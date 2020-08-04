#!/bin/bash

# This needs a few things to work.
# - It needs a ~/.iseq file, example of which is in this directory. This requires your username and password.
# - It us using my workspace - "SimonFraserUniversity-GFunderburk" you will need to change this.
# - It is using a project ID that I got from logging in to ImmunoSeq going to the page for the study, and grabbing the ID from the URL 8-)


study_id="b2bc098c-da25-4e98-80d1-161f59d856e0"
output="/home/lgfunderburk/Documents/AIRR-seqAA/Output/"

./iseq analyzer SimonFraserUniversity-GFunderburk ${study_id} < export_all_samples.sql > ${output}${study_id}.samples.tsv

cd /home/lgfunderburk/Documents/AIRR-seqAA/scripts/

python3 parser_.py ${output}${study_id}".samples.tsv" "/home/lgfunderburk/Documents/AIRR-seqAA/Mapping_Files/NK_ColumnMappings.tsv" "/home/lgfunderburk/Documents/AIRR-seqAA/Mapping_Files/NK_TagMappings.tsv" ${study_id}

python3 tsv_to_json.py ${study_id}".tsv"

cp ${study_id}".tsv" ${output}
cp ${study_id}".json" ${output}

rm ${study_id}".tsv" ${study_id}".json"