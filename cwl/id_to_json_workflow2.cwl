#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: Workflow

hints:
  cwltool:Secrets:  # this extension to CWL v1.0 was incorporated in CWL v1.1
    secrets: [password]
    # hint: pass --enable-ext to the CWL reference runner (cwltool) to accept this
    # or if your production system understands CWL v1.1, use the "cwl-upgrader" tool to
    # upgrade this to the v1.1 syntax
      
inputs:
  username: string
  password: string
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
    run: downloader2.cwl
    in:
      username: username
      password: password
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
