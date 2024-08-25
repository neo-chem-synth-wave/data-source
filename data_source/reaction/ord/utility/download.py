""" The ``data_source.reaction.ord.utility`` package ``download`` module. """

from os import PathLike
from typing import Union

from data_source.base.utility.download import BaseDataSourceDownloadUtility


class OpenReactionDatabaseDownloadUtility:
    """ The `Open Reaction Database (ORD) <https://open-reaction-database.org>`_ download utility class. """

    @staticmethod
    def download_v_release(
            version: str,
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Download the data from a `v_release_*` version of the chemical reaction database.

        :parameter version: The version of the chemical reaction database.
        :parameter output_directory_path: The path to the output directory where the data should be downloaded.
        """

        if version == "v_release_0_1_0":
            file_url = "https://github.com/open-reaction-database/ord-data/archive/refs/tags/v0.1.0.zip"
            file_name = "ord-data-0.1.0.zip"

        else:
            file_url = "https://github.com/open-reaction-database/ord-data/archive/refs/heads/main.zip"
            file_name = "ord-data-main.zip"

        BaseDataSourceDownloadUtility.download_file(
            file_url=file_url,
            file_name=file_name,
            output_directory_path=output_directory_path
        )

    @staticmethod
    def download_v_orderly(
            version: str,
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Download the data from a `v_orderly_*` version of the chemical reaction database.

        :parameter version: The version of the chemical reaction database.
        :parameter output_directory_path: The path to the output directory where the data should be downloaded.
        """

        if version == "v_orderly_condition_by_20240422_wigh_d_s_et_al":
            file_url_suffixes_and_names = [
                ("44413052", "orderly_condition_train.parquet", ),
                ("44413040", "orderly_condition_test.parquet", ),
                ("44413055", "orderly_condition_with_rare_train.parquet", ),
                ("44413043", "orderly_condition_with_rare_test.parquet", ),
            ]

        elif version == "v_orderly_forward_by_20240422_wigh_d_s_et_al":
            file_url_suffixes_and_names = [
                ("44413058", "orderly_forward_train.parquet", ),
                ("44413046", "orderly_forward_test.parquet", ),
            ]

        else:
            file_url_suffixes_and_names = [
                ("44413061", "orderly_retro_train.parquet", ),
                ("44413049", "orderly_retro_test.parquet", ),
            ]

        for file_url_suffix, file_name in file_url_suffixes_and_names:
            BaseDataSourceDownloadUtility.download_file(
                file_url="https://figshare.com/ndownloader/files/{file_url_suffix:s}".format(
                    file_url_suffix=file_url_suffix
                ),
                file_name=file_name,
                output_directory_path=output_directory_path
            )
