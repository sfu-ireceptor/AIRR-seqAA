import json
import sys
import argparse


def extract_tags(adaptv2airrMap=map, jsonSample=json):
    keys = jsonSample[0].keys()


def map_species(kvpair):
    # Would be great to have a reliable mapping betwen a common name to the taxonomic identifiers
    # Doing just human for now.

    species = str.upper(kvpair[1])

    taxonomicIds = {
          "HUMAN"    : ("Homo Sapiens", 9606),
          "MOUSE"    : ("Mus musacris", 10090),
          "ZEBRAFISH": ("Danio rerio", 7955),
          "E. COLI"  : ("Escherichia coli", 562),
          "FRUITFLY" : ("Drosophilia melanogaster", 7227),
        # ...        : ...
    }

    return [
        {
            "species.id"    : taxonomicIds[species][1]
        },
        {
            "species.label" : taxonomicIds[species][0]
        }
    ]


def map_total_t_cells(kvpair):
    celln = kvpair[1]
    return [{"cell_number": celln}]


def map_test_name(kvpair):
    seqplatform = kvpair[1]
    return [{"sequencing_platform": seqplatform}]


def map_locus(kvpair):
    pcr_target_locus = kvpair[1]
    return [{"pcr_target_locus": pcr_target_locus}]


def map_sample_name(kvpair):
    name = kvpair[1]
    return [{"sample_id": name}]


adaptive_to_airr = {
    "sample_name"  : map_sample_name,
    "locus"        : map_locus,
    "test_name"    : map_test_name,
    "total_t_cells": map_total_t_cells,
    "species"      : map_species,
    # add transforms to expand known mappings
}
