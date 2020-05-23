1. Install the Common Workflow Language ( https://www.commonwl.org ) reference runner, cwltool. Preferably inside a fresh Python 3.5+ virtualenv.

```
python3 -m venv env3
. env3/bin/activate
pip install cwltool
```

2. Build the Docker container by running the following within the top directory of this repository

```
docker build -t airr-seqaa . 
```

3. Run the downloader
  1. Using and existing credentials file (a.k.a. ".iseq"):
     ```
     cwltool cwl/downloader.cwl --credentials path-to-my-credentials-file \
       --tag analyzer --workspace VUAmsterdam-Crusoe \
       --project 5eaca36e-c0b9-4be5-aeaa-bc1d230af791 \
       --query adaptive/iseq/export_all_samples.sql
     ```
     See `cwltool cwl/downloader.cwl --help` for more information.
  2. Without having to create a credentials file:
     ```
     cwltool --enable-ext cwl/downloader2.cwl --username m.r.crusoe@vu.nl \
       --password NOTMYREALPASSWORD --workspace VUAmsterdam-Crusoe \
       --project 5eaca36e-c0b9-4be5-aeaa-bc1d230af791 \
       --query adaptive/iseq/export_all_samples.sql
     ```

4. In either case, `cwltool` will produce a description of the results in JSON format over the standard out stream. By default the results from the downloader are written to the current working directory as "results.tsv". You can add `--outdir path_to_desired_output_directory` just after `cwltool` to choose the output location

5. To convert the TSV to JSON format (not to be confused with the summary of running a CWL tool/workflow as mention above), I (M. Crusoe) simplified `scripts/tsv_to_json.py` into `cwl/tsv_to_json.cwl` ; an example of running that by itself is `cwltool cwl/tsv_to_json.cwl cwl/tsv_to_json-job.yaml` ; Here `cwl/tsv_to_json-job.yaml` takes the place of the options we used above as we need to indicate that the tsv is really of format TSV and that is not yet supported at cwltool command line. Inside a full CWL workflow this isn't a problem as shown in 6:

6. To go from project ID to JSON results, try the two step worklow: `cwl/id_to_json_workflow.cwl` (".iseq" credentials style) or `cwl/id_to_json_workflow2.cwl` (username & password style). Example:

```
cwltool --enable-ext cwl/id_to_json_workflow2.cwl --username m.r.crusoe@vu.nl \
  --password NOTMYREALPASSWORD --workspace VUAmsterdam-Crusoe \
  --project 5eaca36e-c0b9-4be5-aeaa-bc1d230af791 \
  --query adaptive/iseq/export_all_samples.sql
```
