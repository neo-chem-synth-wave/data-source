""" The ``data_source.reaction.crd.utility`` package ``extraction`` module. """

from os import PathLike
from pathlib import Path
from typing import Union

from zipfile import ZipFile


class ChemicalReactionDatabaseExtractionUtility:
    """ The `Chemical Reaction Database (CRD) <https://kmt.vander-lingen.nl>`_ extraction utility class. """

    @staticmethod
    def extract_v_reaction_smiles(
            version: str,
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Extract the data from a `v_reaction_smiles_*` version of the database.

        :parameter version: The version of the database.
        :parameter input_directory_path: The path to the input directory where the data is downloaded.
        :parameter output_directory_path: The path to the output directory where the data should be extracted.
        """

        if version == "v_reaction_smiles_1976_to_2024":
            input_file_name = "reactionSmilesFigShare2024.txt.zip"

        else:
            raise ValueError(
                "The extraction of the data from the {data_source:s} is not supported.".format(
                    data_source="Chemical Reaction Database ({version:s})".format(
                        version=version
                    )
                )
            )

        with ZipFile(
            file=Path(input_directory_path, input_file_name)
        ) as zip_archive_file_handle:
            zip_archive_file_handle.extractall(
                path=output_directory_path
            )
