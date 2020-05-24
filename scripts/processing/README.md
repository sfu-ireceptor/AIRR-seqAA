# Scripting

Keep .py and .sh scripts (document) here.

## Usage

### parser_.py 

    usage: parser_.py [-h] [-v] TSV_file map_file tag_file study_id

    positional arguments:
      TSV_file       Indicate the full path to where the TSV from adaptive file is
                     found
      map_file       Indicate the full path to where the mapping file is
                     found
      tag_file       Indicate the full path to where the tagging file is
                     found
      study_id       Indicate the study_id

    optional arguments:
      -h, --help     show this help message and exit
      -v, --verbose  Run the program in verbose mode.

Example

    python3 parser_.py "./5eaca36e-c0b9-4be5-aeaa-bc1d230af791.samples.tsv" "./Mapping_Files/NK_ColumnMappings.tsv" "./Mapping_Files/NK_TagMappings.tsv" "5eaca36e-c0b9-4be5-aeaa-bc1d230af791"
      
### tsv_to_json.py

    usage: tsv_to_json.py [-h] [-v] TSV_file

    positional arguments:
      TSV_file       Indicate the full path to where the TSV from adaptive file is
                     found

    optional arguments:
      -h, --help     show this help message and exit
      -v, --verbose  Run the program in verbose mode.
