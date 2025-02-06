""" The ``data_source.compound.chembl.utility`` package ``extraction`` module. """

from os import PathLike
from pathlib import Path
from shutil import copyfileobj
from typing import Union

from gzip import GzipFile


class ChEMBLCompoundDatabaseExtractionUtility:
    """ The `ChEMBL <https://www.ebi.ac.uk/chembl>`_ chemical compound database extraction utility class. """

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

        input_file_name = "chembl_{release_number:s}_chemreps.txt.gz".format(
            release_number=version.split(
                sep="_"
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
                copyfileobj(
                    fsrc=gzip_archive_file_handle,
                    fdst=destination_file_handle
                )
