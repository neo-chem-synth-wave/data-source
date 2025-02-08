""" The ``data_source.reaction.rhea.utility`` package ``extraction`` module. """

from os import PathLike
from pathlib import Path
from shutil import copyfileobj
from typing import Union

from tarfile import TarFile


class RheaReactionDatabaseExtractionUtility:
    """ The `Rhea <https://www.rhea-db.org>`_ chemical reaction database extraction utility class. """

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

        input_file_name = "{release_number:s}.tar.bz2".format(
            release_number=version.split(
                sep="_"
            )[-1]
        )

        output_file_name = "rhea-reaction-smiles.tsv"

        with TarFile.open(
            name=Path(input_directory_path, input_file_name),
            mode="r:bz2"
        ) as tar_archive_file_handle:
            with tar_archive_file_handle.extractfile(
                member="{release_number:s}/tsv/{output_file_name:s}".format(
                    release_number=version.split(
                        sep="_"
                    )[-1],
                    output_file_name=output_file_name
                )
            ) as source_file_handle:
                with open(
                    file=Path(output_directory_path, output_file_name),
                    mode="wb"
                ) as destination_file_handle:
                    copyfileobj(
                        fsrc=source_file_handle,
                        fdst=destination_file_handle
                    )
