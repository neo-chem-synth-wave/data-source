""" The ``data_source.reaction.crd.utility`` package ``formatting`` module. """

from datetime import datetime
from os import PathLike
from pathlib import Path
from typing import Union

from pandas import read_csv


class ChemicalReactionDatabaseFormattingUtility:
    """ The `Chemical Reaction Database (CRD) <https://kmt.vander-lingen.nl>`_ formatting utility class. """

    @staticmethod
    def format_v_reaction_smiles(
            version: str,
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Format the data from a `v_reaction_smiles_*` version of the chemical reaction database.

        :parameter version: The version of the chemical reaction database.
        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        if version == "v_reaction_smiles_2001_to_2021":
            file_name = "reactionSmilesFigShare.txt"

        elif version == "v_reaction_smiles_2001_to_2023":
            file_name = "reactionSmilesFigShare2023.txt"

        else:
            file_name = "reactionSmilesFigShareUSPTO2023.txt"

        read_csv(
            filepath_or_buffer=Path(input_directory_path, file_name),
            header=None
        ).rename(
            columns={
                0: "reaction_smiles",
            }
        ).to_csv(
            path_or_buf=Path(
                output_directory_path,
                "{timestamp:s}_crd_{version:s}.csv".format(
                    timestamp=datetime.now().strftime(
                        format="%Y%m%d%H%M%S"
                    ),
                    version=version
                )
            ),
            index=False
        )
