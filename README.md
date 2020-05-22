# Adaptive ImmunoSeq Repository

(a.k.a. AIRR-seq Adaptive Adapter) 

Team Lead: Brian Corrie

Project video below.

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/oJaGrAyqDMY/0.jpg)](https://www.youtube.com/watch?v=oJaGrAyqDMY)

## About the Project

Microsoft and Adaptive Biotechnologies are [exploring how the immune system responds to C0VID-19](https://www.cnbc.com/2020/03/20/microsoft-adaptive-studying-coronavirus-immune-system-reaction.html). As part of this project, they are gathering data from the Adaptive Immune Receptor Repertoire (AIRR-seq data) from COVID-19 patients. The AIRR-seq data from this study will be stored in Adaptive's publicly available [ImmunoSeq repository](https://clients.adaptivebiotech.com/login). In order to make this data more broadly accessible, there is a need to convert this data from the Adaptive metadata format to standard AIRR-seq data formats as created by the [AIRR Community](www.airr-community.org).

The goal of this project is to develop a tool (or set of tools) to query the Adaptive ImmunoSeq repository (using their Web APIs), download data, and convert it to the standard AIRR-seq data formats for [Repertoires](https://docs.airr-community.org/en/latest/datarep/metadata.html#file-format-specification). Once we have a converter for the Adaptive metadata, it will be possible to load the COVID-19 data produced by the Microsoft/Adaptive project and load that data into an AIRR Compliant repository such as the [iReceptor Turnkey repository](https://github.com/sfu-ireceptor/turnkey-service-php). The iReceptor project will be operating a [COVID-19 AIRR-seq repository](http://www.ireceptor.org/node/127), and will be working with Adaptive and Microsoft to curate this and other publicly available AIRR-seq data once it is made available. This effort is in collaboration with, and in response to, the [AIRR Community’s call for sharing COVID-19 AIRR-seq data](https://www.antibodysociety.org/airr-community/covid-19-demands-increased-public-sharing-of-biomedical-research-data/). 

Once curated, this data will be a part of the AIRR Data Commons, making it accessible to the international research community in the fight against COVID-19. Not only that, but because the data is part of the AIRR Data Commons, it will be possible for researchers to compare this data with other AIRR-seq data sets from both healthy subjects and data from subjects with other diseases through searching and federating that data using the iReceptor Scientific Gateway.  Sharing these data will be critical for developing diagnostics and therapeutics against cancer, infectious and autoimmune diseases.

