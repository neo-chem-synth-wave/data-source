""" The ``data_source.compound.chembl.utility`` package ``download`` module. """

from os import PathLike
from typing import Union

from data_source.base.utility.download import DataSourceDownloadUtility


class ChEMBLCompoundDatabaseDownloadUtility:
    """ The `ChEMBL <https://www.ebi.ac.uk/chembl>`_ chemical compound database download utility class. """

    @staticmethod
    def download_v_release(
            version: str,
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Download the data from a `v_release_*` version of the database.

        :parameter version: The version of the database.
        :parameter output_directory_path: The path to the output directory where the data should be downloaded.
        """

        release_number = version.split(
            sep="_"
        )[-1]

        file_name = "chembl_{release_number:s}_chemreps.txt.gz".format(
            release_number=release_number
        )

        file_url = "https://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_{release_number:s}/{file_name:s}".format(
            release_number=release_number,
            file_name=file_name
        )

        DataSourceDownloadUtility.download_file(
            file_url=file_url,
            file_name=file_name,
            output_directory_path=output_directory_path
        )
