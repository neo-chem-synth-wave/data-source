""" The ``data_source.reaction.crd.utility`` package ``formatting`` module. """

from datetime import datetime
from os import PathLike
from pathlib import Path
from typing import Union

from pandas.io.parsers.readers import read_csv


class ChemicalReactionDatabaseFormattingUtility:
    """ The `Chemical Reaction Database (CRD) <https://kmt.vander-lingen.nl>`_ formatting utility class. """

    @staticmethod
    def format_v_reaction_smiles(
            version: str,
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Format the data from a `v_reaction_smiles_*` version of the database.

        :parameter version: The version of the database.
        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        if version == "v_reaction_smiles_2001_to_2021":
            input_file_name = "reactionSmilesFigShare.txt"

        elif version == "v_reaction_smiles_2001_to_2023":
            input_file_name = "reactionSmilesFigShare2023.txt"

        else:
            input_file_name = "reactionSmilesFigShareUSPTO2023.txt"

        output_file_name = "{timestamp:s}_crd_{version:s}.csv".format(
            timestamp=datetime.now().strftime(
                format="%Y%m%d%H%M%S"
            ),
            version=version
        )

        dataframe = read_csv(
            filepath_or_buffer=Path(input_directory_path, input_file_name),
            header=None
        ).rename(
            columns={
                0: "reaction_smiles",
            }
        )

        dataframe["file_name"] = input_file_name

        dataframe.to_csv(
            path_or_buf=Path(output_directory_path, output_file_name),
            index=False
        )
