""" The ``data_source.reaction.ord.utility`` package ``extraction`` module. """

from os import PathLike
from pathlib import Path
from typing import Union

from zipfile import ZipFile


class OpenReactionDatabaseExtractionUtility:
    """ The `Open Reaction Database (ORD) <https://open-reaction-database.org>`_ extraction utility class. """

    @staticmethod
    def extract_v_release(
            version: str,
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Extract the data from a `v_release_*` version of the database.

        :parameter version: The version of the database.
        :parameter input_directory_path: The path to the input directory where the data is downloaded.
        :parameter output_directory_path: The path to the output directory where the data should be extracted.
        """

        if version == "v_release_0_1_0":
            input_file_name = "ord-data-0.1.0.zip"

        else:
            input_file_name = "ord-data-main.zip"

        with ZipFile(
            file=Path(input_directory_path, input_file_name)
        ) as zip_archive_file_handle:
            zip_archive_file_handle.extractall(
                path=output_directory_path
            )
