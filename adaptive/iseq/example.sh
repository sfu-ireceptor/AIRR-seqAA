#!/bin/bash

# This needs a few things to work.
# - It needs a ~/.iseq file, example of which is in this directory. This requires your username and password.
# - It us using my workspace - "SimonFraserUniversity-Corrie" you will need to change this.
# - It is using a project ID that I got from logging in to ImmunoSeq going to the page for the study, and grabbing the ID from the URL 8-)

./iseq analyzer SimonFraserUniversity-Corrie 5eaca36e-c0b9-4be5-aeaa-bc1d230af791 < export_all_samples.sql > 5eaca36e-c0b9-4be5-aeaa-bc1d230af791.samples.tsv
