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

    if str.upper(species) in taxonomicIds.keys():
        return [
            {
                "species.id": taxonomicIds[species][1]
            },
            {
                "species.label": taxonomicIds[species][0]
            }
        ]
    else:
        print(
            "Species [ {} ] does not have a defined mapping to id/tax.".format(species))
        return 1


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


def map_counting_method(kvpair):
    cnt_method = kvpair[1]

    try:
        cnt_method = str(cnt_method)
        return [{"software_versions": str(kvpair[1])}]
    except:
        print("Could not transform {} to string.".format(cnt_method))
        # Frankly can't think of a case what they could put in the field for it to fail
        return 1


def map_product_subtype(kvpair):
    try:
        kitinfo = str(kvpair[1])
        return [{"sequencing_kit": kitinfo}]
    except:
        print("Could not transform [{}] to string.".format(kitinfo))
        return 1


def map_kit_id(kvpair):
    if kvpair[1] in [None, False, 0, ""]:
        return [{"library_generation_kit_info": "N/A"}]
    try:
        kit_id = str(kvpair[1])
        return [{"library_generation_kit_info": kit_id}]
    except:
        return [{"library_generation_kit_info": "N/A"}]


adaptive_to_airr = {
    "sample_name"    : map_sample_name,
    "locus"          : map_locus,
    "test_name"      : map_test_name,
    "total_t_cells"  : map_total_t_cells,
    "species"        : map_species,
    "counting_method": map_counting_method,
    "product_subtype": map_product_subtype,
    "kit_id"         : map_kit_id
    # add transforms to expand known mappings
}
