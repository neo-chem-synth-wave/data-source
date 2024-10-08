# Overview
**Title:** A Generative Model for Electron Paths<br>
**Authors:** John Bradshaw, Matt J. Kusner, Brooks Paige, Marwin H.S. Segler, José M. Hernández-Lobato<br>
**Publication Date:** 2018/12/21<br>
**Publication Link:** [OpenReview](https://openreview.net/forum?id=r1x4BnCqKX)<br>
**Alternative Publication Links:** [arXiv](https://arxiv.org/abs/1805.10970) |
[Apollo - University of Cambridge Repository](https://www.repository.cam.ac.uk/items/c0d8b48a-5e44-43e5-9a03-487fcadea456)


# Abstract
Chemical reactions can be described as the stepwise redistribution of electrons in molecules. As such, reactions are
often depicted using "arrow-pushing" diagrams which show this movement as a sequence of arrows. We propose an electron
path prediction model (ELECTRO) to learn these sequences directly from raw reaction data. Instead of predicting product
molecules directly from reactant molecules in one shot, learning a model of electron movement has the benefits of (a)
being easy for chemists to interpret, (b) incorporating constraints of chemistry, such as balanced atom counts before
and after the reaction, and (c) naturally encoding the sparsity of chemical reactions, which usually involve changes in
only a small number of atoms in the reactants. We design a method to extract approximate reaction paths from any dataset
of atom-mapped reaction SMILES strings. Our model achieves excellent performance on an important subset of the USPTO
reaction dataset, comparing favorably to the strongest baselines. Furthermore, we show that our model recovers a basic
knowledge of chemistry without being explicitly trained to do so.
