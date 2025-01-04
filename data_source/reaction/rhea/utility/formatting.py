""" The ``data_source.reaction.rhea.utility`` package ``formatting`` module. """

from datetime import datetime
from os import PathLike
from pathlib import Path
from typing import Union

from pandas.io.parsers.readers import read_csv


class RheaReactionDatabaseFormattingUtility:
    """ The `Rhea <https://www.rhea-db.org>`_ chemical reaction database formatting utility class. """

    @staticmethod
    def format_v_release(
            version: str,
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Format the data from a `v_release_*` version of the chemical reaction database.

        :parameter version: The version of the chemical reaction database.
        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        input_file_name = "rhea-reaction-smiles.tsv"

        output_file_name = "{timestamp:s}_rhea_{version:s}.csv".format(
            timestamp=datetime.now().strftime(
                format="%Y%m%d%H%M%S"
            ),
            version=version
        )

        read_csv(
            filepath_or_buffer=Path(input_directory_path, input_file_name),
            sep="\t",
            header=None
        ).rename(
            columns={
                0: "id",
                1: "reaction_smiles",
            }
        ).to_csv(
            path_or_buf=Path(output_directory_path, output_file_name),
            index=False
        )
