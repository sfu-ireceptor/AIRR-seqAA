#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: Workflow

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

steps:
  download_project:
    run: downloader.cwl
    in:
      credentials: credentials
      tag: tag
      workspace: workspace
      project: project
      query: query
    out: [ results ]
  convert_to_JSON:
    run: tsv_to_json.cwl
    in:
      tsv: download_project/results
    out: [ json ]

outputs:
  results:
    type: File
    outputSource: convert_to_JSON/json
 
