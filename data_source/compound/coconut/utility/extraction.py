""" The ``data_source.compound.coconut.utility`` package ``extraction`` module. """

from os import PathLike
from pathlib import Path
from shutil import copyfileobj
from typing import Union

from zipfile import ZipFile


class COCONUTCompoundDatabaseExtractionUtility:
    """ The `COCONUT <https://coconut.naturalproducts.net>`_ chemical compound database extraction utility class. """

    @staticmethod
    def extract_v_2_0_by_20241126_chandrasekhar_v_et_al(
            version: str,
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Extract the data from a `v_2_0_*_by_20241126_chandrasekhar_v_et_al` version of the database.

        :parameter version: The version of the database.
        :parameter input_directory_path: The path to the input directory where the data is downloaded.
        :parameter output_directory_path: The path to the output directory where the data should be extracted.
        """

        if version == "v_2_0_by_20241126_chandrasekhar_v_et_al":
            input_file_name = "coconut-10-2024.csv.zip"

        elif version == "v_2_0_complete_by_20241126_chandrasekhar_v_et_al":
            input_file_name = "coconut_complete-10-2024.csv.zip"

        else:
            raise ValueError(
                "The extraction of the data from the {data_source:s} is not supported.".format(
                    data_source="COCONUT chemical compound database ({version:s})".format(
                        version=version
                    )
                )
            )

        output_file_name = input_file_name[:-4]

        with ZipFile(
            file=Path(input_directory_path, input_file_name)
        ) as zip_archive_file_handle:
            with zip_archive_file_handle.open(
                name=output_file_name
            ) as source_file_handle:
                with open(
                    file=Path(output_directory_path, output_file_name),
                    mode="wb"
                ) as destination_file_handle:
                    copyfileobj(
                        fsrc=source_file_handle,
                        fdst=destination_file_handle
                    )
