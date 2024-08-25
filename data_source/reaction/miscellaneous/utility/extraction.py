""" The ``data_source.reaction.miscellaneous.utility`` package ``extraction`` module. """

from os import PathLike
from pathlib import Path
from typing import Union

from zipfile import ZipFile


class MiscellaneousReactionDataSourceExtractionUtility:
    """ The miscellaneous chemical reaction data source extraction utility class. """

    @staticmethod
    def extract_v_20131008_kraut_h_et_al(
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Extract the data from the `v_20131008_kraut_h_et_al` version of the chemical reaction data source.

        :parameter input_directory_path: The path to the input directory where the data is downloaded.
        :parameter output_directory_path: The path to the output directory where the data should be extracted.
        """

        with ZipFile(
            file=Path(input_directory_path, "ci400442f_si_002.zip")
        ) as zip_archive_file_handle:
            zip_archive_file_handle.extractall(
                path=output_directory_path
            )

    @staticmethod
    def extract_v_golden_dataset_by_20211103_lin_a_et_al(
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Extract the data from the `v_golden_dataset_by_20211103_lin_a_et_al` version of the chemical reaction data
        source.

        :parameter input_directory_path: The path to the input directory where the data is downloaded.
        :parameter output_directory_path: The path to the output directory where the data should be extracted.
        """

        with ZipFile(
            file=Path(input_directory_path, "golden_dataset.zip")
        ) as zip_archive_file_handle:
            zip_archive_file_handle.extractall(
                path=output_directory_path
            )
