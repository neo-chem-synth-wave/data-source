# Overview
**Title:** What's What: The (Nearly) Definitive Guide to Reaction Role Assignment<br>
**Authors:** Nadine Schneider, Nikolaus Stiefl, Gregory A. Landrum<br>
**Publication Date:** 2016/11/22<br>
**Publication Link:** [ACS JCIM](https://pubs.acs.org/doi/full/10.1021/acs.jcim.6b00564)


# Abstract
When analyzing chemical reactions it is essential to know which molecules are actively involved in the reaction and
which educts will form the product molecules. Assigning reaction roles, like reactant, reagent, or product, to the
molecules of a chemical reaction might be a trivial problem for hand-curated reaction schemes, but it is more difficult
to automate, an essential step when handling large amounts of reaction data. Here, we describe a new fingerprint-based
and data-driven approach to assign reaction roles which is also applicable to rather unbalanced and noisy reaction
schemes. Given a set of molecules involved and knowing the product(s) of a reaction we assign the most probable
reactants and sort out the remaining reagents. Our approach was validated using two different data sets: one
hand-curated data set comprising about 680 diverse reactions extracted from patents which span more than 200 different
reaction types and include up to 18 different reactants. A second set consists of 50,000 randomly picked reactions from
US patents. The results of the second data set were compared to results obtained using two different atom-to-atom
mapping algorithms. For both data sets our method assigns the reaction roles correctly for the vast majority of the
reactions, achieving an accuracy of 88% and 97% respectively. The median time needed, about 8 ms, indicates that the
algorithm is fast enough to be applied to large collections. The new method is available as part of the RDKit toolkit
and the data sets and Jupyter notebooks used for evaluation of the new method are available in the Supporting
Information of this publication.
