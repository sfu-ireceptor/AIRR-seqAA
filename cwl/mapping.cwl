#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: CommandLineTool

hints:
  DockerRequirement:
    dockerPull: airr-seqaa

inputs:
  tsv:
    type: File
    format: iana:text/tab-separated-values

  mapping:
    type: File

  tags:
    type: File

  study_id:
    type: string

baseCommand: parser_.py

arguments: [ $(inputs.tsv.path), $(inputs.mapping.path), $(inputs.tags.path), $(inputs.study_id) ]

outputs:
  results:
    type: File
    format: $(inputs.tsv.format)
    outputBinding:
      glob: $(inputs.study_id).tsv

$namespaces:
  iana: https://www.iana.org/assignments/media-types/
