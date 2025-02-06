""" The ``data_source.reaction.rhea.utility`` package ``download`` module. """

from os import PathLike
from typing import Union

from data_source.base.utility.download import DataSourceDownloadUtility


class RheaReactionDatabaseDownloadUtility:
    """ The `Rhea <https://www.rhea-db.org>`_ chemical reaction database download utility class. """

    @staticmethod
    def download_v_release(
            version: str,
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Download the data from a `v_release_*` version of the chemical reaction database.

        :parameter version: The version of the chemical reaction database.
        :parameter output_directory_path: The path to the output directory where the data should be downloaded.
        """

        file_url = "https://ftp.expasy.org/databases/rhea/old_releases/{release_number:s}.tar.bz2".format(
            release_number=version.split(
                sep="_"
            )[-1]
        )

        DataSourceDownloadUtility.download_file(
            url=file_url,
            name=file_url.split(
                sep="/"
            )[-1],
            output_directory_path=output_directory_path
        )
