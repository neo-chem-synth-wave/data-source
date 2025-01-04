""" The ``data_source.reaction.crd.utility`` package ``download`` module. """

from os import PathLike
from typing import Union

from data_source.base.utility.download import BaseDataSourceDownloadUtility


class ChemicalReactionDatabaseDownloadUtility:
    """ The `Chemical Reaction Database (CRD) <https://kmt.vander-lingen.nl>`_ download utility class. """

    @staticmethod
    def download_v_reaction_smiles(
            version: str,
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Download the data from a `v_reaction_smiles_*` version of the database.

        :parameter version: The version of the database.
        :parameter output_directory_path: The path to the output directory where the data should be downloaded.
        """

        if version == "v_reaction_smiles_2001_to_2021":
            file_url = "https://figshare.com/ndownloader/files/36222051"

            file_name = "reactionSmilesFigShare.txt"

        elif version == "v_reaction_smiles_2001_to_2023":
            file_url = "https://figshare.com/ndownloader/files/39944236"

            file_name = "reactionSmilesFigShare2023.txt"

        else:
            file_url = "https://figshare.com/ndownloader/files/43858050"

            file_name = "reactionSmilesFigShareUSPTO2023.txt"

        BaseDataSourceDownloadUtility.download_file(
            file_url=file_url,
            file_name=file_name,
            output_directory_path=output_directory_path
        )
