""" The ``data_source.reaction_pattern.miscellaneous.utility`` package ``download`` module. """

from os import PathLike
from typing import Union

from data_source.base.utility.download import DataSourceDownloadUtility


class MiscellaneousReactionPatternDataSourceDownloadUtility:
    """ The miscellaneous chemical reaction pattern data source download utility class. """

    @staticmethod
    def download_v_retro_transform_db_by_20180421_avramova_s_et_al(
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Download the data from the `v_retro_transform_db_by_20180421_avramova_s_et_al` version of the data source.

        :parameter output_directory_path: The path to the output directory where the data should be downloaded.
        """

        file_url = "https://zenodo.org/records/1209313/files/RetroTransformDB-v-1-0.txt"

        DataSourceDownloadUtility.download_file(
            url=file_url,
            name=file_url.split(
                sep="/"
            )[-1],
            output_directory_path=output_directory_path
        )

    @staticmethod
    def download_v_dingos_by_20190701_button_a_et_al(
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Download the data from the `v_dingos_by_20190701_button_a_et_al` version of the data source.

        :parameter output_directory_path: The path to the output directory where the data should be downloaded.
        """

        file_url = (
            "https://raw.githubusercontent.com/neo-chem-synth-wave/data-source/refs/heads/main/"
            "data/reaction/miscellaneous_v_dingos_by_20190701_button_a_et_al/rxn_set.txt"
        )

        DataSourceDownloadUtility.download_file(
            url=file_url,
            name=file_url.split(
                sep="/"
            )[-1],
            output_directory_path=output_directory_path
        )

    @staticmethod
    def download_v_auto_template_by_20240627_chen_l_and_li_y(
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Download the data from the `v_auto_template_by_20240627_chen_l_and_li_y` version of the data source.

        :parameter output_directory_path: The path to the output directory where the data should be downloaded.
        """

        file_url = "https://github.com/Lung-Yi/AutoTemplate/archive/refs/heads/main.zip"
        file_name = "AutoTemplate-main.zip"

        DataSourceDownloadUtility.download_file(
            url=file_url,
            name=file_name,
            output_directory_path=output_directory_path
        )
