# Overview
**Title:** ORDerly: Data Sets and Benchmarks for Chemical Reaction Data<br>
**Authors:** Daniel S. Wigh, Joe Arrowsmith, Alexander Pomberger, Kobi C. Felton, Alexei A. Lapkin<br>
**Publication Date:** 2024/04/22<br>
**Publication Link:** [ACS JCIM](https://pubs.acs.org/doi/full/10.1021/acs.jcim.4c00292)<br>
**Alternative Publication Links:** [ChemRxiv](https://chemrxiv.org/engage/chemrxiv/article-details/64ca5d3e4a3f7d0c0d78ca42)
| [PubMed Central](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11094788) |
[ResearchGate](https://www.researchgate.net/publication/372903934_ORDerly_Datasets_and_benchmarks_for_chemical_reaction_data)


# Abstract
Machine learning has the potential to provide tremendous value to life sciences by providing models that aid in the
discovery of new molecules and reduce the time for new products to come to market. Chemical reactions play a significant
role in these fields, but there is a lack of high-quality open-source chemical reaction data sets for training machine
learning models. Herein, we present ORDerly, an open-source Python package for the customizable and reproducible
preparation of reaction data stored in accordance with the increasingly popular Open Reaction Database (ORD) schema. We
use ORDerly to clean United States patent data stored in ORD and generate data sets for forward prediction,
retrosynthesis, as well as the first benchmark for reaction condition prediction. We train neural networks on data sets
generated with ORDerly for condition prediction and show that data sets missing key cleaning steps can lead to silently
overinflated performance metrics. Additionally, we train transformers for forward and retrosynthesis prediction and
demonstrate how non-patent data can be used to evaluate model generalization. By providing a customizable open-source
solution for cleaning and preparing large chemical reaction data, ORDerly is poised to push forward the boundaries of
machine learning applications in chemistry.
