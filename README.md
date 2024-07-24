# The Computer-assisted Chemical Synthesis Data Source Project
![Static Badge](https://img.shields.io/badge/Elix%2C%20Inc.-%235EB6B3?style=flat)
![Static Badge](https://img.shields.io/badge/Institute%20of%20Science%20Tokyo-%231C3177?style=flat)

Over the last decade, computer-assisted chemical synthesis has re-emerged as a heavily researched subject in
Chemoinformatics. Even though the idea of utilizing computers to assist chemical synthesis has existed for nearly as
long as computers themselves, the expected blend of reliability and innovation has repeatedly been proven difficult to
achieve. Nevertheless, recent machine learning approaches have exhibited the potential to address these shortcomings.
The open-source data utilized by such approaches frequently lack quality and quantity, are stored in various formats, or
are published behind a paywall, all of which can represent significant barriers to entry for researchers.


## Installation
A minimal virtual environment can be created using the [git](https://git-scm.com) and [conda](https://conda.io) commands
as follows:

```shell
git clone https://github.com/neo-chem-synth-wave/data-source.git

cd data-source

conda env create -f environment.yaml

conda activate data-source-env
```

The [data_source](/data_source) package can be locally installed using the [pip](https://pip.pypa.io) command as
follows:

```shell
pip install --no-build-isolation -e .
```


## License Information
The contents of this repository are published under the [MIT](/LICENSE) license. Please refer to individual references
for more details regarding the license information of external resources utilized within this repository.


## Contact
If you are interested in contributing to this repository by reporting bugs, suggesting improvements, or submitting
feedback, feel free to use [GitHub Issues](https://github.com/neo-chem-synth-wave/data-source/issues).
