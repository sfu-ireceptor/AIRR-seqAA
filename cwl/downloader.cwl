#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: CommandLineTool

requirements:
  InitialWorkDirRequirement:
    listing:
      - entry: $(inputs.credentials)
        entryname: .iseq  # in CWL, $HOME is set to the working directory

hints:
  DockerRequirement:
    dockerPull: airr-seqaa
      
inputs:
  credentials:
    type: File
    label: Format is tag:user:pass:url
    doc: |
      File name doesn't matter, will be made available to the iseq tool as $HOME/.iseq
  tag:
    type: string
    label: which entry in the credential file to use
    doc: must match the first element in one of the lines of the credentials input
  workspace:
    type: string
    label: workspace UUID or name
  project:
    type: string
    label: project UUID, or name within the given 'workspace'
  query:
    type: File
    label: SQL query to run
    
baseCommand: iseq

stdin: $(inputs.query.path)

arguments: [ $(inputs.tag), $(inputs.workspace), $(inputs.project) ]

stdout: results.tsv

outputs:
  results:
    type: File
    streamable: True
    format: iana:text/tab-separated-values
    outputBinding:
      glob: results.tsv

$namespaces: { iana: https://www.iana.org/assignments/media-types/ }
