""" The ``data_source.reaction_pattern.miscellaneous.utility`` package ``extraction`` module. """

from os import PathLike
from pathlib import Path
from typing import Union

from zipfile import ZipFile


class MiscellaneousReactionPatternDataSourceExtractionUtility:
    """ The miscellaneous chemical reaction pattern data source extraction utility class. """

    @staticmethod
    def extract_v_auto_template_by_20240627_chen_l_and_li_y(
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Extract the data from the `v_auto_template_by_20240627_chen_l_and_li_y` version of the data source.

        :parameter input_directory_path: The path to the input directory where the data is downloaded.
        :parameter output_directory_path: The path to the output directory where the data should be extracted.
        """

        input_file_name = "AutoTemplate-main.zip"

        with ZipFile(
            file=Path(input_directory_path, input_file_name)
        ) as zip_archive_file_handle:
            zip_archive_file_handle.extractall(
                path=output_directory_path
            )
