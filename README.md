# The Data Source Project
![Static Badge](https://img.shields.io/badge/Elix%2C%20Inc.-%235EB6B3?style=flat)
![Static Badge](https://img.shields.io/badge/Institute%20of%20Science%20Tokyo-%231C3177?style=flat)

Over the last decade, computer-assisted chemical synthesis has re-emerged as a heavily researched subject in
Chemoinformatics. Even though the idea of utilizing computers to assist chemical synthesis has existed for nearly as
long as computers themselves, the expected blend of reliability and innovation has repeatedly been proven difficult to
achieve. Nevertheless, recent machine learning approaches have exhibited the potential to address these shortcomings.
The open-source data utilized by such approaches frequently lack quality and quantity, are stored in various formats, or
are published behind paywalls, all of which can represent significant barriers, especially for novice researchers. The
main objective of the Data Source project is to systematically curate and facilitate access to relevant
computer-assisted chemical synthesis data sources.


## Installation
A standalone environment can be created using the [git](https://git-scm.com) and [conda](https://conda.io) commands as
follows:

```shell
git clone https://github.com/neo-chem-synth-wave/data-source.git

cd data-source

conda env create -f environment.yaml

conda activate data-source-env
```

The [data_source](/data_source) package can be installed using the [pip](https://pip.pypa.io) command as follows:

```shell
pip install --no-build-isolation -e .
```


## Utilization
The purpose of the [scripts](/scripts) directory is to illustrate how to download, extract, and format the following
types of computer-assisted chemical synthesis data:

- [Chemical Compounds](#chemical-compounds)
- [Chemical Reactions](#chemical-reactions)
- [Chemical Reaction Rules](#chemical-reaction-rules)

The [download_extract_and_format_data](/scripts/download_extract_and_format_data.py) script can be utilized as follows:

```shell
# Example #1: Get the chemical reaction data source information.
python scripts/download_extract_and_format_data.py \
  --data_source_category "reaction" \
  --get_data_source_information

# Example #2: Get the ZINC20 chemical compound dataset version information.
python scripts/download_extract_and_format_data.py \
  --data_source_category "compound" \
  --data_source "zinc20" \
  --get_data_source_version_information

# Example #3: Download, extract, and format the data from the RetroRules chemical reaction rule database.
python scripts/download_extract_and_format_data.py \
  --data_source_category "reaction_rule" \
  --data_source "retro_rules" \
  --data_source_version "v_release_rr02_rp3_nohs" \
  --output_directory_path "path/to/the/output/directory"
```


### Chemical Compounds
The following chemical compound data sources are currently supported:

- [ChEMBL](#chembl)
- [ZINC20](#zinc20)
- [Miscellaneous Chemical Compound Data Sources](#miscellaneous-chemical-compound-data-sources)


#### ChEMBL
The following **ChEMBL** chemical compound database versions are currently supported:

| Version                                                                                                                                                              | DOI                                                        | Status                     |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------|----------------------------|
| v_release_[{release_number ≥ 25}](https://chembl.gitbook.io/chembl-interface-documentation/downloads#chembl-database-release-dois) <sup>[**[1]**](#references)</sup> | `https://doi.org/10.6019/CHEMBL.database.{release_number}` | :green_circle: Implemented |


#### ZINC20
The following **ZINC20** chemical compound database versions are currently supported:

| Version                                                                                                                   | DOI                                        | Status                     |
|---------------------------------------------------------------------------------------------------------------------------|--------------------------------------------|----------------------------|
| v_building_blocks_[{building_blocks_subset_name}](https://files.docking.org/bb/current) <sup>[**[2]**](#references)</sup> | `https://doi.org/10.1021/acs.jcim.0c00675` | :green_circle: Implemented |
| v_catalog_[{catalog_name}](https://files.docking.org/catalogs/source) <sup>[**[2]**](#references)</sup>                   | `https://doi.org/10.1021/acs.jcim.0c00675` | :green_circle: Implemented |


#### Miscellaneous Chemical Compound Data Sources
The following miscellaneous chemical compound data sources are currently supported:

| Version                                                          | DOI                                         | Status                     |
|------------------------------------------------------------------|---------------------------------------------|----------------------------|
| v_20190701_button_a_et_al <sup>[**[3]**](#references)</sup>      | `https://doi.org/10.24433/CO.6930970.v1`    | :green_circle: Implemented |
| v_20201218_polykovskiy_d_et_al <sup>[**[4]**](#references)</sup> | `https://doi.org/10.3389/fphar.2020.565644` | :green_circle: Implemented |


### Chemical Reactions
The following chemical reaction data sources are currently supported:

- [United States Patent and Trademark Office (USPTO) Dataset](#united-states-patent-and-trademark-office-uspto-dataset)
- [Open Reaction Database (ORD)](#open-reaction-database-ord)
- [Chemical Reaction Database (CRD)](#chemical-reaction-database-crd)
- [Rhea Database](#rhea-database)
- [Miscellaneous Chemical Reaction Data Sources](#miscellaneous-chemical-reaction-data-sources)

![chemical_reaction_data_sources.png](figures/chemical_reaction_data_sources.png)


#### United States Patent and Trademark Office (USPTO) Dataset
The following **United States Patent and Trademark Office (USPTO)** chemical reaction dataset versions are currently
supported:

| Version                                                                    | DOI                                               | Status                                |
|----------------------------------------------------------------------------|---------------------------------------------------|---------------------------------------|
| v_1976_to_2013_by_20121009_lowe_d_m <sup>[[5]](#references)</sup>          | `https://doi.org/10.6084/m9.figshare.12084729.v1` | :yellow_circle: Partially Implemented |
| v_50k_by_20161122_schneider_n_et_al <sup>[[6]](#references)</sup>          | `https://doi.org/10.1021/acs.jcim.6b00564`        | :green_circle: Implemented            |
| v_15k_by_20170418_coley_c_w_et_al <sup>[[7]](#references)</sup>            | `https://doi.org/10.1021/acscentsci.7b00064`      | :green_circle: Implemented            |
| v_1976_to_2016_by_20121009_lowe_d_m <sup>[[5]](#references)</sup>          | `https://doi.org/10.6084/m9.figshare.5104873.v1`  | :yellow_circle: Partially Implemented |
| v_50k_by_20171116_coley_c_w_et_al <sup>[[8]](#references)</sup>            | `https://doi.org/10.1021/acscentsci.7b00355`      | :green_circle: Implemented            |
| v_480k_or_mit_by_20171204_jin_w_et_al <sup>[[9]](#references)</sup>        | `https://doi.org/10.48550/arXiv.1709.04555`       | :green_circle: Implemented            |
| v_480k_or_mit_by_20180622_schwaller_p_et_al <sup>[[10]](#references)</sup> | `https://doi.org/10.1039/C8SC02339E`              | :green_circle: Implemented            |
| v_stereo_by_20180622_schwaller_p_et_al <sup>[[10]](#references)</sup>      | `https://doi.org/10.1039/C8SC02339E`              | :green_circle: Implemented            |
| v_1k_tpl_by_20210128_schwaller_p_et_al <sup>[[11]](#references)</sup>      | `https://doi.org/10.1038/s42256-020-00284-w`      | :green_circle: Implemented            |


### Chemical Reaction Rules
The following chemical reaction rule data sources are currently supported:

- [RetroRules Database](#retrorules-database)
- [Miscellaneous Chemical Reaction Rule Data Sources](#miscellaneous-chemical-reaction-rule-data-sources)


## License Information
The contents of this repository are published under the [MIT](/LICENSE) license. Please refer to individual references
for more details regarding the license information of external resources utilized within this repository.


## Contact
If you are interested in contributing to this repository by reporting bugs, suggesting improvements, or submitting
feedback, feel free to use [GitHub Issues](https://github.com/neo-chem-synth-wave/data-source/issues).

## References
