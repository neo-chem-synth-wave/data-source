""" The ``data_source.reaction.uspto.utility`` package ``download`` module. """

from os import PathLike
from typing import Union

from data_source.base.utility.download import BaseDataSourceDownloadUtility


class USPTOReactionDatasetDownloadUtility:
    """
    The `United States Patent and Trademark Office (USPTO) <https://www.repository.cam.ac.uk/handle/1810/244727>`_
    chemical reaction dataset download utility class.
    """

    @staticmethod
    def download_v_1976_to_2013_by_20121009_lowe_d_m(
            version: str,
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Download the data from a `v_1976_to_2013_*_by_20121009_lowe_d_m` version of the chemical reaction dataset.

        :parameter version: The version of the chemical reaction dataset.
        :parameter output_directory_path: The path to the output directory where the data should be downloaded.
        """

        if version == "v_1976_to_2013_by_20121009_lowe_d_m":
            file_url_suffixes_and_names = [
                ("files/22217844", "1976-2013_USPTOgrants_CML.7z", ),
                ("files/22217838", "2001-2013_USPTOapplications_CML.7z", ),
            ]

        elif version == "v_1976_to_2013_cml_by_20121009_lowe_d_m":
            file_url_suffixes_and_names = [
                ("files/22217829", "1976-2013_USPTOgrants_reactionSmiles_feb2014filters.7z", ),
                ("files/22217826", "2001-2013_USPTOapplications_reactionSmiles_feb2014filters.7z", ),
            ]

        else:
            file_url_suffixes_and_names = [
                ("articles/12084729/versions/1", "12084729.zip", ),
            ]

        for file_url_suffix, file_name in file_url_suffixes_and_names:
            BaseDataSourceDownloadUtility.download_file(
                file_url="https://figshare.com/ndownloader/{file_url_suffix:s}".format(
                    file_url_suffix=file_url_suffix
                ),
                file_name=file_name,
                output_directory_path=output_directory_path
            )

    @staticmethod
    def download_v_50k_by_20141226_schneider_n_et_al(
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Download the data from the `v_50k_by_20141226_schneider_n_et_al` version of the chemical reaction dataset.

        :parameter output_directory_path: The path to the output directory where the data should be downloaded.
        """

        BaseDataSourceDownloadUtility.download_file(
            file_url="https://ndownloader.figstatic.com/files/3848755",
            file_name="ci5006614_si_002.zip",
            output_directory_path=output_directory_path
        )

    @staticmethod
    def download_v_50k_by_20161122_schneider_n_et_al(
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Download the data from the `v_50k_by_20161122_schneider_n_et_al` version of the chemical reaction dataset.

        :parameter output_directory_path: The path to the output directory where the data should be downloaded.
        """

        BaseDataSourceDownloadUtility.download_file(
            file_url="https://ndownloader.figstatic.com/files/7005749",
            file_name="ci6b00564_si_002.zip",
            output_directory_path=output_directory_path
        )

    @staticmethod
    def download_v_15k_by_20170418_coley_c_w_et_al(
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Download the data from the `v_15k_by_20170418_coley_c_w_et_al` version of the chemical reaction dataset.

        :parameter output_directory_path: The path to the output directory where the data should be downloaded.
        """

        BaseDataSourceDownloadUtility.download_file(
            file_url="https://raw.githubusercontent.com/wengong-jin/nips17-rexgen/master/USPTO-15K/data.zip",
            file_name="data.zip",
            output_directory_path=output_directory_path
        )

    @staticmethod
    def download_v_1976_to_2016_by_20121009_lowe_d_m(
            version: str,
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Download the data from a `v_1976_to_2016_*_by_20121009_lowe_d_m` version of the chemical reaction dataset.

        :parameter version: The version of the chemical reaction dataset.
        :parameter output_directory_path: The path to the output directory where the data should be downloaded.
        """

        if version == "v_1976_to_2016_cml_by_20121009_lowe_d_m":
            file_url_suffixes_and_names = [
                ("files/8664364", "1976_Sep2016_USPTOgrants_cml.7z", ),
                ("files/8664367", "2001_Sep2016_USPTOapplications_cml.7z", ),
            ]

        elif version == "v_1976_to_2016_rsmi_by_20121009_lowe_d_m":
            file_url_suffixes_and_names = [
                ("files/8664379", "1976_Sep2016_USPTOgrants_smiles.7z", ),
                ("files/8664370", "2001_Sep2016_USPTOapplications_smiles.7z", ),
            ]

        else:
            file_url_suffixes_and_names = [
                ("articles/5104873/versions/1", "5104873.zip", ),
            ]

        for file_url_suffix, file_name in file_url_suffixes_and_names:
            BaseDataSourceDownloadUtility.download_file(
                file_url="https://figshare.com/ndownloader/{file_url_suffix:s}".format(
                    file_url_suffix=file_url_suffix
                ),
                file_name=file_name,
                output_directory_path=output_directory_path
            )

    @staticmethod
    def download_v_50k_by_20170905_liu_b_et_al(
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Download the data from the `v_50k_by_20170905_liu_b_et_al` version of the chemical reaction dataset.

        :parameter output_directory_path: The path to the output directory where the data should be downloaded.
        """

        for file_name in [
            "train_targets",
            "train_sources",
            "valid_targets",
            "valid_sources",
            "test_targets",
            "test_sources",
        ]:
            BaseDataSourceDownloadUtility.download_file(
                file_url="https://raw.githubusercontent.com/pandegroup/{file_url_suffix:s}".format(
                    file_url_suffix="reaction_prediction_seq2seq/master/processed_data/{file_name:s}".format(
                        file_name=file_name
                    )
                ),
                file_name=file_name,
                output_directory_path=output_directory_path
            )

    @staticmethod
    def download_v_50k_by_20171116_coley_c_w_et_al(
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Download the data from the `v_50k_by_20171116_coley_c_w_et_al` version of the chemical reaction dataset.

        :parameter output_directory_path: The path to the output directory where the data should be downloaded.
        """

        BaseDataSourceDownloadUtility.download_file(
            file_url="https://raw.githubusercontent.com/connorcoley/retrosim/master/{file_url_suffix:s}".format(
                file_url_suffix="retrosim/data/data_processed.csv"
            ),
            file_name="data_processed.csv",
            output_directory_path=output_directory_path
        )

    @staticmethod
    def download_v_480k_or_mit_by_20171204_jin_w_et_al(
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Download the data from the `v_480k_or_mit_by_20171204_jin_w_et_al` version of the chemical reaction dataset.

        :parameter output_directory_path: The path to the output directory where the data should be downloaded.
        """

        BaseDataSourceDownloadUtility.download_file(
            file_url="https://raw.githubusercontent.com/wengong-jin/nips17-rexgen/master/USPTO/data.zip",
            file_name="data.zip",
            output_directory_path=output_directory_path
        )

    @staticmethod
    def download_v_20180622_schwaller_p_et_al(
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Download the data from a `v_*_20180622_schwaller_p_et_al` version of the chemical reaction dataset.

        :parameter output_directory_path: The path to the output directory where the data should be downloaded.
        """

        BaseDataSourceDownloadUtility.download_file(
            file_url=BaseDataSourceDownloadUtility.send_http_get_request(
                http_get_request_url="{url:s}?{folder_id:s}&{vanity_name:s}&{rm:s}".format(
                    url="https://ibm.ent.box.com/index.php",
                    folder_id="folder_id=40552708120",
                    vanity_name="q[shared_item][vanity_name]=ReactionSeq2SeqDataset",
                    rm="rm=box_v2_zip_shared_folder"
                )
            ).json()["download_url"],
            file_name="ReactionSeq2Seq_Dataset.zip",
            output_directory_path=output_directory_path
        )

    @staticmethod
    def download_v_lef_by_20181221_bradshaw_j_et_al(
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Download the data from the `v_lef_by_20181221_bradshaw_j_et_al` version of the chemical reaction dataset.

        :parameter output_directory_path: The path to the output directory where the data should be downloaded.
        """

        BaseDataSourceDownloadUtility.download_file(
            file_url="https://raw.githubusercontent.com/john-bradshaw/electro/master/lef_uspto.zip",
            file_name="lef_uspto.zip",
            output_directory_path=output_directory_path
        )

    @staticmethod
    def download_v_1k_tpl_by_20210128_schwaller_p_et_al(
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Download the data from the `v_1k_tpl_by_20210128_schwaller_p_et_al` version of the chemical reaction dataset.

        :parameter output_directory_path: The path to the output directory where the data should be downloaded.
        """

        BaseDataSourceDownloadUtility.download_file(
            file_url=BaseDataSourceDownloadUtility.send_http_get_request(
                http_get_request_url="{url:s}?{folder_id:s}&{vanity_name:s}&{rm:s}".format(
                    url="https://ibm.ent.box.com/index.php",
                    folder_id="folder_id=124192222443",
                    vanity_name="q[shared_item][vanity_name]=MappingChemicalReactions",
                    rm="rm=box_v2_zip_shared_folder"
                )
            ).json()["download_url"],
            file_name="MappingChemicalReactions.zip",
            output_directory_path=output_directory_path
        )

    @staticmethod
    def download_v_1976_to_2016_by_20210407_schwaller_p_et_al(
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Download the data from the `v_1976_to_2016_by_20210407_schwaller_p_et_al` version of the chemical reaction
        dataset.

        :parameter output_directory_path: The path to the output directory where the data should be downloaded.
        """

        BaseDataSourceDownloadUtility.download_file(
            file_url=BaseDataSourceDownloadUtility.send_http_get_request(
                http_get_request_url="{url:s}?{folder_id:s}&{vanity_name:s}&{rm:s}".format(
                    url="https://ibm.ent.box.com/index.php",
                    folder_id="folder_id=112951098080",
                    vanity_name="q[shared_item][vanity_name]=RXNMapperData",
                    rm="rm=box_v2_zip_shared_folder"
                )
            ).json()["download_url"],
            file_name="USPTO_remapped.zip",
            output_directory_path=output_directory_path
        )

    @staticmethod
    def download_v_chen_s_et_al(
            version: str,
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Download the data from a `v_*_chen_s_et_al` version of the chemical reaction dataset.

        :parameter version: The version of the chemical reaction dataset.
        :parameter output_directory_path: The path to the output directory where the data should be downloaded.
        """

        if version == "v_1976_to_2016_by_20240313_chen_s_et_al":
            file_url_suffix = "44192531"
            file_name = "remapped_USPTO_FULL.csv"

        elif version == "v_50k_by_20240313_chen_s_et_al":
            file_url_suffix = "44192528"
            file_name = "remapped_USPTO_50K.csv"

        else:
            file_url_suffix = "44708185"
            file_name = "mech-USPTO-31k.csv"

        BaseDataSourceDownloadUtility.download_file(
            file_url="https://figshare.com/ndownloader/files/{file_url_suffix:s}".format(
                file_url_suffix=file_url_suffix
            ),
            file_name=file_name,
            output_directory_path=output_directory_path
        )
