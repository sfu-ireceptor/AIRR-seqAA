#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: CommandLineTool

doc: |
  This CWL description of the iseq downloader tool doesn't require the user to
  construct a ".iseq" credentials file; it assembles the credentials file for
  them.

requirements:
  InitialWorkDirRequirement:
    listing:
      - entryname: .iseq
        entry: |
          analyzer:$(inputs.username):$(inputs.password):$(inputs.url)

hints:
  cwltool:Secrets:  # this extension to CWL v1.0 was incorporated in CWL v1.1
    secrets: [password]
    # hint: pass --enable-ext to the CWL reference runner (cwltool) to accept this
    # or if your production system understands CWL v1.1, use the "cwl-upgrader" tool to
    # upgrade this to the v1.1 syntax
  DockerRequirement:
    dockerPull: airr-seqaa
      
inputs:
  username: string
  password: string
  url:
    type: string
    default: https://analyzer.adaptivebiotech.com
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

arguments: [ analyzer, $(inputs.workspace), $(inputs.project) ]

stdout: $(inputs.project).tsv

outputs:
  results:
    type: File
    streamable: True
    format: iana:text/tab-separated-values
    outputBinding:
      glob: $(inputs.project).tsv

$namespaces:
  iana: https://www.iana.org/assignments/media-types/
  cwltool: http://commonwl.org/cwltool#
