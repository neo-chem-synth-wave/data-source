""" The ``data_source.reaction.miscellaneous.utility`` package ``download`` module. """

from os import PathLike
from typing import Union

from data_source.base.utility.download import BaseDataSourceDownloadUtility


class MiscellaneousReactionDataSourceDownloadUtility:
    """ The miscellaneous chemical reaction data source download utility class. """

    @staticmethod
    def download_v_20131008_kraut_h_et_al(
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Download the data from the `v_20131008_kraut_h_et_al` version of the chemical reaction data source.

        :parameter output_directory_path: The path to the output directory where the data should be downloaded.
        """

        BaseDataSourceDownloadUtility.download_file(
            file_url="https://ndownloader.figstatic.com/files/3988891",
            file_name="ci400442f_si_002.zip",
            output_directory_path=output_directory_path
        )

    @staticmethod
    def download_v_20161014_wei_j_n_et_al(
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Download the data from the `v_20161014_wei_j_n_et_al` version of the chemical reaction data source.

        :parameter output_directory_path: The path to the output directory where the data should be downloaded.
        """

        for file_name in [
            "Wade8_47.ans_smi.txt",
            "Wade8_48.ans_smi.txt",
        ]:
            BaseDataSourceDownloadUtility.download_file(
                file_url="https://raw.githubusercontent.com/jnwei/{file_url_suffix:s}".format(
                    file_url_suffix="neural_reaction_fingerprint/master/data/test_questions/{file_name:s}".format(
                        file_name=file_name
                    )
                ),
                file_name=file_name,
                output_directory_path=output_directory_path
            )

    @staticmethod
    def download_v_20200508_grambow_c_et_al(
            version: str,
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Download the data from a `v_*_20200508_grambow_c_et_al` version of the chemical reaction data source.

        :parameter version: The version of the chemical reaction data source.
        :parameter output_directory_path: The path to the output directory where the data should be downloaded.
        """

        if version == "v_20200508_grambow_c_et_al":
            file_url_suffixes = [
                "3715478/files/b97d3.csv",
                "3715478/files/wb97xd3.csv",
            ]

        else:
            file_url_suffixes = [
                "3731554/files/b97d3_rad.csv",
                "3731554/files/wb97xd3_rad.csv",
            ]

        for file_url_suffix in file_url_suffixes:
            BaseDataSourceDownloadUtility.download_file(
                file_url="https://zenodo.org/records/{file_url_suffix:s}".format(
                    file_url_suffix=file_url_suffix
                ),
                file_name=file_url_suffix.split(
                    sep="/"
                )[-1],
                output_directory_path=output_directory_path
            )

    @staticmethod
    def download_v_golden_dataset_by_20211103_lin_a_et_al(
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Download the data from the `v_golden_dataset_by_20211103_lin_a_et_al` version of the chemical reaction data
        source.

        :parameter output_directory_path: The path to the output directory where the data should be downloaded.
        """

        BaseDataSourceDownloadUtility.download_file(
            file_url="https://github.com/Laboratoire-de-Chemoinformatique/{file_url_suffix:s}".format(
                file_url_suffix="Reaction_Data_Cleaning/raw/master/data/golden_dataset.zip"
            ),
            file_name="golden_dataset.zip",
            output_directory_path=output_directory_path
        )

    @staticmethod
    def download_v_rdb7_by_20220718_spiekermann_k_et_al(
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Download the data from the `v_rdb7_by_20220718_spiekermann_k_et_al` version of the chemical reaction data
        source.

        :parameter output_directory_path: The path to the output directory where the data should be downloaded.
        """

        for file_name in [
            "b97d3.csv",
            "wb97xd3.csv",
            "ccsdtf12_dz.csv",
            "ccsdtf12_tz.csv",
        ]:
            BaseDataSourceDownloadUtility.download_file(
                file_url="https://zenodo.org/records/6618262/files/{file_name:s}".format(
                    file_name=file_name
                ),
                file_name=file_name,
                output_directory_path=output_directory_path
            )
