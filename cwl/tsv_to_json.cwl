#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: CommandLineTool

doc: Based upon scripts/tsv_to_json.py by Artem Kushner, Laura Gutierrez Funderburk

hints:
  DockerRequirement:
    dockerPull: airr-seqaa

inputs:
  tsv:
    type: File
    format: iana:text/tab-separated-values

baseCommand: [ python3, -c ]

arguments:
  - |
    import pandas as pd
    dataframe = pd.read_csv("$(inputs.tsv.path)", sep='\t')
    with open("$(inputs.tsv.nameroot).json", 'w') as f:
      f.write(dataframe.to_json(orient='records'))

outputs:
   json:
     type: File
     format: iana:application/json
     outputBinding:
       glob: $(inputs.tsv.nameroot).json

$namespaces: { iana: https://www.iana.org/assignments/media-types/ }
