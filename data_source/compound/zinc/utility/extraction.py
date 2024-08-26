""" The ``data_source.compound.zinc.utility`` package ``extraction`` module. """

from os import PathLike
from pathlib import Path
from shutil import copyfileobj
from typing import Union

from gzip import open as open_gzip_archive_file


class ZINCCompoundDatabaseExtractionUtility:
    """ The `ZINC <https://zinc20.docking.org>`_ chemical compound database extraction utility class. """

    @staticmethod
    def extract_v_building_blocks(
            version: str,
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Extract the data from a `v_building_blocks_*` version of the chemical compound database.

        :parameter version: The version of the chemical compound database.
        :parameter input_directory_path: The path to the input directory where the data is downloaded.
        :parameter output_directory_path: The path to the output directory where the data should be extracted.
        """

        with open_gzip_archive_file(
            filename=Path(
                input_directory_path,
                "{file_name:s}.smi.gz".format(
                    file_name=version.split(
                        sep="_",
                        maxsplit=3
                    )[-1]
                )
            )
        ) as gzip_archive_file_handle:
            with open(
                file=Path(
                    output_directory_path,
                    "{file_name:s}.smi".format(
                        file_name=version.split(
                            sep="_",
                            maxsplit=3
                        )[-1]
                    )
                ),
                mode="wb"
            ) as destination_file_handle:
                copyfileobj(
                    fsrc=gzip_archive_file_handle,
                    fdst=destination_file_handle
                )
