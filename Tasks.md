# AIRR Adaptive Adapter Tasks

Below is an example of the workflow we would hope to be able to perform at the end of the hackathon. Recall that the goal is to be able to process a large number of datasets from Adaptive's ImmunoSeq repository, in particular the COVID-19 data from the Adaptive/Microsoft project, with the workflow below performed for each dataset. 

An ideal outcome for the end of the hackathon would be able to have a pipeline of simple commands to perform the following workflow.

- Find an interesting study
    - Log in to Adaptives ImmunoSeq web portal
    - Identify an interesting study/data set (`study_id` = "COVID-19 study")
    - Log out
- Download all data related to `study_id` from ImmunoSeq using ImmunoSeq API
    - Download Repertoire metadata (AIRR term) for each sample (Adaptive term) in `study_id` using ImmunoSeq API
        - This would typically be a single TSV file with one line per repertoire/sample
    - Download Sequence Rearrangement data for each sample in `study_id` using ImmunoSeq API
        - This would typically be a single TSV for EACH repertoire/sample, with each TSV file potentially having a very large number of lines (up to millions of lines per repertoire/sample.
- Convert Adaptive sample data to an AIRR Repertoire JSON file
    - This is the challenging part, we need to map a relatively loose key:value metadata dataset to the more structured AIRR Standard repertoire metadata
- Load data for `study_id` into an iReceptor repository
    - Load AIRR Repertoire JSON file converted above
    - Load each of the Adaptive Rearrangement TSV files, one file per repertoire/sample in the AIRR Repertoire JSON file

# The Tasks

The tasks that are anticipated for this hackathon, should you choose to accept them, are:

- Pick a representative study `study_id` from ImmunoSeq as an example
- Write some code/scripts that take a `study_id` as a parameters and downloads all of the data from ImmunoSeq for `study_id`
- Determine a mapping of ImmunoSeq sample metadata fields and metadata tags to AIRR fields
- Write some code/scripts that uses this mapping to converts ImmunoSeq sample metadata to AIRR Repertoire metadata
- Download and install an iReceptor Turnkey repository on our project VM
- Write some code/scripts that upload the convereted `study_id` data to the iReceptor Turnkey repository
