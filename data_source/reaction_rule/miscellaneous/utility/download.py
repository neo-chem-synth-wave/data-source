""" The ``data_source.reaction_rule.miscellaneous.utility`` package ``download`` module. """

from os import PathLike
from typing import Union

from data_source.base.utility.download import BaseDataSourceDownloadUtility


class MiscellaneousReactionRuleDataSourceDownloadUtility:
    """ The miscellaneous chemical reaction rule data source download utility class. """

    @staticmethod
    def download_v_retro_transform_db_by_20180421_avramova_s_et_al(
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Download the data from the `v_retro_transform_db_by_20180421_avramova_s_et_al` version of the data source.

        :parameter output_directory_path: The path to the output directory where the data should be downloaded.
        """

        file_name = "RetroTransformDB-v-1-0.txt"

        file_url = "https://zenodo.org/records/1209313/files/{file_name:s}".format(
            file_name=file_name
        )

        BaseDataSourceDownloadUtility.download_file(
            file_url=file_url,
            file_name=file_name,
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

        file_name = "rxn_set.txt"

        file_url = "https://raw.githubusercontent.com/neo-chem-synth-wave/data-source/main/data/{file_url_suffix:s}".format(
            file_url_suffix="reaction_rule/miscellaneous_v_dingos_by_20190701_button_a_et_al/{file_name:s}".format(
                file_name=file_name
            )
        )

        BaseDataSourceDownloadUtility.download_file(
            file_url=file_url,
            file_name=file_name,
            output_directory_path=output_directory_path
        )
