""" The ``data_source.reaction.miscellaneous.utility`` package ``download`` module. """

from os import PathLike
from typing import Union

from data_source.base.utility.download import DataSourceDownloadUtility


class MiscellaneousReactionDataSourceDownloadUtility:
    """ The miscellaneous chemical reaction data source download utility class. """

    @staticmethod
    def download_v_20131008_kraut_h_et_al(
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Download the data from the `v_20131008_kraut_h_et_al` version of the data source.

        :parameter output_directory_path: The path to the output directory where the data should be downloaded.
        """

        file_url = "https://ndownloader.figstatic.com/files/3988891"
        file_name = "ci400442f_si_002.zip"

        DataSourceDownloadUtility.download_file(
            url=file_url,
            name=file_name,
            output_directory_path=output_directory_path
        )

    @staticmethod
    def download_v_20161014_wei_j_n_et_al(
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Download the data from the `v_20161014_wei_j_n_et_al` version of the data source.

        :parameter output_directory_path: The path to the output directory where the data should be downloaded.
        """

        file_urls = [
            "https://raw.githubusercontent.com/jnwei/neural_reaction_fingerprint/master/data/test_questions/Wade8_47.ans_smi.txt",
            "https://raw.githubusercontent.com/jnwei/neural_reaction_fingerprint/master/data/test_questions/Wade8_48.ans_smi.txt",
        ]

        for file_url in file_urls:
            DataSourceDownloadUtility.download_file(
                url=file_url,
                name=file_url.split(
                    sep="/"
                )[-1],
                output_directory_path=output_directory_path
            )

    @staticmethod
    def download_v_20200508_grambow_c_et_al(
            version: str,
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Download the data from a `v_*_20200508_grambow_c_et_al` version of the data source.

        :parameter version: The version of the data source.
        :parameter output_directory_path: The path to the output directory where the data should be downloaded.
        """

        if version == "v_20200508_grambow_c_et_al":
            file_urls = [
                "https://zenodo.org/records/3715478/files/b97d3.csv",
                "https://zenodo.org/records/3715478/files/wb97xd3.csv",
            ]

        elif version == "v_add_on_by_20200508_grambow_c_et_al":
            file_urls = [
                "https://zenodo.org/records/3731554/files/b97d3_rad.csv",
                "https://zenodo.org/records/3731554/files/wb97xd3_rad.csv",
            ]

        else:
            raise ValueError(
                "The download of the data from the {data_source:s} is not supported.".format(
                    data_source="miscellaneous chemical reaction data source ({version:s})".format(
                        version=version
                    )
                )
            )

        for file_url in file_urls:
            DataSourceDownloadUtility.download_file(
                url=file_url,
                name=file_url.split(
                    sep="/"
                )[-1],
                output_directory_path=output_directory_path
            )

    @staticmethod
    def download_v_golden_dataset_by_20211102_lin_a_et_al(
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Download the data from the `v_golden_dataset_by_20211102_lin_a_et_al` version of the data source.

        :parameter output_directory_path: The path to the output directory where the data should be downloaded.
        """

        file_url = (
            "https://github.com/Laboratoire-de-Chemoinformatique/Reaction_Data_Cleaning/raw/master/data/"
            "golden_dataset.zip"
        )

        DataSourceDownloadUtility.download_file(
            url=file_url,
            name=file_url.split(
                sep="/"
            )[-1],
            output_directory_path=output_directory_path
        )

    @staticmethod
    def download_v_rdb7_by_20220718_spiekermann_k_et_al(
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Download the data from the `v_rdb7_by_20220718_spiekermann_k_et_al` version of the data source.

        :parameter output_directory_path: The path to the output directory where the data should be downloaded.
        """

        file_urls = [
            "https://zenodo.org/records/6618262/files/b97d3.csv",
            "https://zenodo.org/records/6618262/files/wb97xd3.csv",
            "https://zenodo.org/records/6618262/files/ccsdtf12_dz.csv",
            "https://zenodo.org/records/6618262/files/ccsdtf12_tz.csv",
        ]

        for file_url in file_urls:
            DataSourceDownloadUtility.download_file(
                url=file_url,
                name=file_url.split(
                    sep="/"
                )[-1],
                output_directory_path=output_directory_path
            )

    @staticmethod
    def download_v_orderly(
            version: str,
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Download the data from a `v_orderly_*` version of the database.

        :parameter version: The version of the database.
        :parameter output_directory_path: The path to the output directory where the data should be downloaded.
        """

        if version == "v_orderly_condition_by_20240422_wigh_d_s_et_al":
            file_urls_and_names = [
                (
                    "https://figshare.com/ndownloader/files/44413052",
                    "orderly_condition_train.parquet",
                ),
                (
                    "https://figshare.com/ndownloader/files/44413040",
                    "orderly_condition_test.parquet",
                ),
                (
                    "https://figshare.com/ndownloader/files/44413055",
                    "orderly_condition_with_rare_train.parquet",
                ),
                (
                    "https://figshare.com/ndownloader/files/44413043",
                    "orderly_condition_with_rare_test.parquet",
                ),
            ]

        elif version == "v_orderly_forward_by_20240422_wigh_d_s_et_al":
            file_urls_and_names = [
                (
                    "https://figshare.com/ndownloader/files/44413058",
                    "orderly_forward_train.parquet",
                ),
                (
                    "https://figshare.com/ndownloader/files/44413046",
                    "orderly_forward_test.parquet",
                ),
            ]

        elif version == "v_orderly_retro_by_20240422_wigh_d_s_et_al":
            file_urls_and_names = [
                (
                    "https://figshare.com/ndownloader/files/44413061",
                    "orderly_retro_train.parquet",
                ),
                (
                    "https://figshare.com/ndownloader/files/44413049",
                    "orderly_retro_test.parquet",
                ),
            ]

        else:
            raise ValueError(
                "The download of the data from the {data_source:s} is not supported.".format(
                    data_source="miscellaneous chemical reaction data source ({version:s})".format(
                        version=version
                    )
                )
            )

        for file_url, file_name in file_urls_and_names:
            DataSourceDownloadUtility.download_file(
                url=file_url,
                name=file_name,
                output_directory_path=output_directory_path
            )
