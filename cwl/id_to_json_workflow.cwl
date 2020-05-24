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
  mapping:
    type: File
  tags:
    type: File

steps:
  download_adaptive_study:
    run: downloader.cwl
    in:
      credentials: credentials
      tag: tag
      workspace: workspace
      project: project
      query: query
    out: [ results ]
  map_adaptive_to_AIRR:
    run: mapping.cwl
    in:
      tsv: download_adaptive_study/results
      mapping: mapping
      tags: tags
      study_id: project
    out: [ results ]
  convert_to_AIRR_Repertoire_JSON:
    run: tsv_to_json.cwl
    in:
      tsv: map_adaptive_to_AIRR/results
    out: [ json ]

outputs:
  results:
    type: File
    format: iana:application/json
    outputSource: convert_to_AIRR_Repertoire_JSON/json
 
$namespaces:
  iana: https://www.iana.org/assignments/media-types/
  cwltool: http://commonwl.org/cwltool#
