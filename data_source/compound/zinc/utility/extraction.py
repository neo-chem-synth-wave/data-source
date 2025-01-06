""" The ``data_source.compound.zinc.utility`` package ``extraction`` module. """

from os import PathLike
from pathlib import Path
from shutil import copyfileobj
from typing import Union

from gzip import GzipFile


class ZINCCompoundDatabaseExtractionUtility:
    """ The `ZINC <https://zinc20.docking.org>`_ chemical compound database extraction utility class. """

    @staticmethod
    def extract_v_building_blocks(
            version: str,
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Extract the data from a `v_building_blocks_*` version of the database.

        :parameter version: The version of the database.
        :parameter input_directory_path: The path to the input directory where the data is downloaded.
        :parameter output_directory_path: The path to the output directory where the data should be extracted.
        """

        input_file_name = "{input_file_name_prefix:s}.smi.gz".format(
            input_file_name_prefix=version.split(
                sep="_",
                maxsplit=3
            )[-1]
        )

        output_file_name = input_file_name[:-3]

        with GzipFile(
            filename=Path(input_directory_path, input_file_name)
        ) as gzip_archive_file_handle:
            with open(
                file=Path(output_directory_path, output_file_name),
                mode="wb"
            ) as destination_file_handle:
                # noinspection PyTypeChecker
                copyfileobj(
                    fsrc=gzip_archive_file_handle,
                    fdst=destination_file_handle
                )
