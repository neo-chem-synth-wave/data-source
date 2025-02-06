""" The ``data_source.compound.zinc.utility`` package ``download`` module. """

from os import PathLike
from typing import Union

from data_source.base.utility.download import DataSourceDownloadUtility


class ZINCCompoundDatabaseDownloadUtility:
    """ The `ZINC <https://zinc.docking.org>`_ chemical compound database download utility class. """

    @staticmethod
    def download_v_building_blocks(
            version: str,
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Download the data from a `v_building_blocks_*` version of the database.

        :parameter version: The version of the database.
        :parameter output_directory_path: The path to the output directory where the data should be downloaded.
        """

        file_name = "{file_name_prefix:s}.smi.gz".format(
            file_name_prefix=version.split(
                sep="_",
                maxsplit=3
            )[-1]
        )

        file_url = "https://files.docking.org/bb/current/{file_name:s}".format(
            file_name=file_name
        )

        DataSourceDownloadUtility.download_file(
            url=file_url,
            name=file_name,
            output_directory_path=output_directory_path
        )

    @staticmethod
    def download_v_catalog(
            version: str,
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Download the data from a `v_catalog_*` version of the database.

        :parameter version: The version of the database.
        :parameter output_directory_path: The path to the output directory where the data should be downloaded.
        """

        file_name = "{file_name_prefix:s}.src.txt".format(
            file_name_prefix=version.split(
                sep="_",
                maxsplit=2
            )[-1]
        )

        file_url = "https://files.docking.org/catalogs/source/{file_name:s}".format(
            file_name=file_name
        )

        DataSourceDownloadUtility.download_file(
            url=file_url,
            name=file_name,
            output_directory_path=output_directory_path
        )
