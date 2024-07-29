""" The ``data_source.reaction`` package ``uspto`` module. """

from datetime import datetime
from logging import Logger
from os import PathLike
from pathlib import Path
from shutil import copyfileobj
from typing import Dict, Optional, Union

from gzip import open as open_gzip_archive_file

from pandas.core.reshape.concat import concat
from pandas.io.parsers.readers import read_csv

from py7zr.py7zr import SevenZipFile

from zipfile import ZipFile

from data_source.abstract_base.abstract_base import AbstractBaseDataSource


class USPTOReactionDataset(AbstractBaseDataSource):
    """
    The `United States Patent and Trademark Office (USPTO) <https://doi.org/10.17863/CAM.16293>`_ chemical reaction
    dataset class.
    """

    def __init__(
            self,
            logger: Optional[Logger] = None
    ) -> None:
        """
        The constructor method of the class.

        :parameter logger: The logger. The value `None` indicates that the logger should not be utilized.
        """

        super().__init__(
            logger=logger
        )

    @property
    def available_versions(
            self
    ) -> Dict[str, str]:
        """
        Get the available versions of the chemical reaction dataset.

        :returns: The available versions of the chemical reaction dataset.
        """

        return {
            "v_1976_to_2013_by_20121009_lowe_d_m": "https://doi.org/10.6084/m9.figshare.12084729.v1",
            "v_50k_by_20161122_schneider_n_et_al": "https://doi.org/10.1021/acs.jcim.6b00564",
            "v_15k_by_20170418_coley_c_w_et_al": "https://doi.org/10.1021/acscentsci.7b00064",
            "v_1976_to_2016_by_20121009_lowe_d_m": "https://doi.org/10.6084/m9.figshare.5104873.v1",
            "v_50k_by_20171116_coley_c_w_et_al": "https://doi.org/10.1021/acscentsci.7b00355",
            "v_480k_or_mit_by_20171204_jin_w_et_al": "https://doi.org/10.48550/arXiv.1709.04555",
            "v_480k_or_mit_by_20180622_schwaller_p_et_al": "https://doi.org/10.1039/C8SC02339E",
            "v_stereo_by_20180622_schwaller_p_et_al": "https://doi.org/10.1039/C8SC02339E",
            "v_1k_tpl_by_20210128_schwaller_p_et_al": "https://doi.org/10.1038/s42256-020-00284-w",
            "v_1976_to_2016_by_20210407_schwaller_p_et_al": "https://doi.org/10.1126/sciadv.abe4166",
            "v_1976_to_2016_by_20240313_chen_s_et_al": "https://doi.org/10.6084/m9.figshare.25046471.v1",
            "v_50k_by_20240313_chen_s_et_al": "https://doi.org/10.6084/m9.figshare.25046471.v1",
        }

    # ------------------------------------------------------------------------------------------------------------------
    #  Version: v_1976_to_2013_by_20121009_lowe_d_m
    # ------------------------------------------------------------------------------------------------------------------

    @staticmethod
    def _download_v_1976_to_2013_by_20121009_lowe_d_m(
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Download the data from the `v_1976_to_2013_by_20121009_lowe_d_m` version of the chemical reaction dataset.

        :parameter output_directory_path: The path to the output directory where the data should be downloaded.
        """

        AbstractBaseDataSource._download_file(
            file_url="https://figshare.com/ndownloader/articles/12084729/versions/1",
            file_name="12084729.zip",
            output_directory_path=output_directory_path
        )

    @staticmethod
    def _extract_v_1976_to_2013_by_20121009_lowe_d_m(
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Extract the data from the `v_1976_to_2013_by_20121009_lowe_d_m` version of the chemical reaction dataset.

        :parameter input_directory_path: The path to the input directory where the data is downloaded.
        :parameter output_directory_path: The path to the output directory where the data should be extracted.
        """

        with ZipFile(
            file=Path(input_directory_path, "12084729.zip")
        ) as zip_archive_file_handle:
            for seven_zip_archive_file_name in [
                "1976-2013_USPTOgrants_reactionSmiles_feb2014filters.7z",
                "2001-2013_USPTOapplications_reactionSmiles_feb2014filters.7z",
            ]:
                with zip_archive_file_handle.open(
                    name=seven_zip_archive_file_name
                ) as seven_zip_archive_file_handle:
                    with open(
                        file=Path(output_directory_path, seven_zip_archive_file_name),
                        mode="wb"
                    ) as destination_file_handle:
                        copyfileobj(
                            fsrc=seven_zip_archive_file_handle,
                            fdst=destination_file_handle
                        )

                with SevenZipFile(
                    file=Path(input_directory_path, seven_zip_archive_file_name)
                ) as seven_zip_archive_file_handle:
                    seven_zip_archive_file_handle.extractall(
                        path=output_directory_path
                    )

    @staticmethod
    def _format_v_1976_to_2013_by_20121009_lowe_d_m(
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Format the data from the `v_1976_to_2013_by_20121009_lowe_d_m` version of the chemical reaction dataset.

        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        dataframes = list()

        for file_name in [
            "1976-2013_USPTOgrants_reactionSmiles_feb2014filters.rsmi",
            "2001-2013_USPTOapplications_reactionSmiles_feb2014filters.rsmi",
        ]:
            dataframe = read_csv(
                filepath_or_buffer=Path(input_directory_path, file_name),
                sep="\t",
                header=None,
                low_memory=False
            )

            dataframe["FileName"] = file_name

            dataframes.append(
                dataframe
            )

        concat(
            objs=dataframes
        ).rename(
            columns={
                0: "ReactionSmiles",
                1: "PatentNumber",
                2: "ParagraphNum",
            }
        ).to_csv(
            path_or_buf=Path(
                output_directory_path,
                "{timestamp:s}_uspto_v_1976_to_2013_by_20121009_lowe_d_m.csv".format(
                    timestamp=datetime.now().strftime(
                        format="%Y%m%d%H%M%S"
                    )
                )
            ),
            index=False
        )

    # ------------------------------------------------------------------------------------------------------------------
    #  Version: v_50k_by_20161122_schneider_n_et_al
    # ------------------------------------------------------------------------------------------------------------------

    @staticmethod
    def _download_v_50k_by_20161122_schneider_n_et_al(
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Download the data from the `v_50k_by_20161122_schneider_n_et_al` version of the chemical reaction dataset.

        :parameter output_directory_path: The path to the output directory where the data should be downloaded.
        """

        AbstractBaseDataSource._download_file(
            file_url="https://ndownloader.figstatic.com/files/7005749",
            file_name="ci6b00564_si_002.zip",
            output_directory_path=output_directory_path
        )

    @staticmethod
    def _extract_v_50k_by_20161122_schneider_n_et_al(
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Extract the data from the `v_50k_by_20161122_schneider_n_et_al` version of the chemical reaction dataset.

        :parameter input_directory_path: The path to the input directory where the data is downloaded.
        :parameter output_directory_path: The path to the output directory where the data should be extracted.
        """

        with ZipFile(
            file=Path(input_directory_path, "ci6b00564_si_002.zip")
        ) as zip_archive_file_handle:
            for file_name in [
                "dataSetA.csv",
                "dataSetB.csv",
            ]:
                with zip_archive_file_handle.open(
                    name="data/{file_name:s}".format(
                        file_name=file_name
                    )
                ) as source_file_handle:
                    with open(
                        file=Path(output_directory_path, file_name),
                        mode="wb"
                    ) as destination_file_handle:
                        copyfileobj(
                            fsrc=source_file_handle,
                            fdst=destination_file_handle
                        )

    @staticmethod
    def _format_v_50k_by_20161122_schneider_n_et_al(
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Format the data from the `v_50k_by_20161122_schneider_n_et_al` version of the chemical reaction dataset.

        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        dataframes = list()

        for file_name in [
            "dataSetA.csv",
            "dataSetB.csv",
        ]:
            dataframe = read_csv(
                filepath_or_buffer=Path(input_directory_path, file_name),
                sep=",",
                header=0
            )

            dataframe["file_Name"] = file_name

            dataframes.append(
                dataframe
            )

        concat(
            objs=dataframes
        ).to_csv(
            path_or_buf=Path(
                output_directory_path,
                "{timestamp:s}_uspto_v_50k_by_20161122_schneider_n_et_al.csv".format(
                    timestamp=datetime.now().strftime(
                        format="%Y%m%d%H%M%S"
                    )
                )
            ),
            index=False
        )

    # ------------------------------------------------------------------------------------------------------------------
    #  Version: v_15k_by_20170418_coley_c_w_et_al
    # ------------------------------------------------------------------------------------------------------------------

    @staticmethod
    def _download_v_15k_by_20170418_coley_c_w_et_al(
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Download the data from the `v_15k_by_20170418_coley_c_w_et_al` version of the chemical reaction dataset.

        :parameter output_directory_path: The path to the output directory where the data should be downloaded.
        """

        AbstractBaseDataSource._download_file(
            file_url="https://raw.githubusercontent.com/wengong-jin/nips17-rexgen/master/USPTO-15K/data.zip",
            file_name="data.zip",
            output_directory_path=output_directory_path
        )

    @staticmethod
    def _extract_v_15k_by_20170418_coley_c_w_et_al(
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Extract the data from the `v_15k_by_20170418_coley_c_w_et_al` version of the chemical reaction dataset.

        :parameter input_directory_path: The path to the input directory where the data is downloaded.
        :parameter output_directory_path: The path to the output directory where the data should be extracted.
        """

        with ZipFile(
            file=Path(input_directory_path, "data.zip")
        ) as zip_archive_file_handle:
            for file_name in [
                "train.txt",
                "valid.txt",
                "test.txt",
            ]:
                with zip_archive_file_handle.open(
                    name="data/{file_name:s}".format(
                        file_name=file_name
                    )
                ) as source_file_handle:
                    with open(
                        file=Path(output_directory_path, file_name),
                        mode="wb"
                    ) as destination_file_handle:
                        copyfileobj(
                            fsrc=source_file_handle,
                            fdst=destination_file_handle
                        )

    @staticmethod
    def _format_v_15k_by_20170418_coley_c_w_et_al(
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Format the data from the `v_15k_by_20170418_coley_c_w_et_al` version of the chemical reaction dataset.

        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        dataframes = list()

        for file_name in [
            "train.txt",
            "valid.txt",
            "test.txt",
        ]:
            dataframe = read_csv(
                filepath_or_buffer=Path(input_directory_path, file_name),
                sep="\t",
                header=None
            )

            dataframe["file_name"] = file_name

            dataframes.append(
                dataframe
            )

        concat(
            objs=dataframes
        ).rename(
            columns={
                0: "reaction_smiles",
            }
        ).to_csv(
            path_or_buf=Path(
                output_directory_path,
                "{timestamp:s}_uspto_v_15k_by_20170418_coley_c_w_et_al.csv".format(
                    timestamp=datetime.now().strftime(
                        format="%Y%m%d%H%M%S"
                    )
                )
            ),
            index=False
        )

    # ------------------------------------------------------------------------------------------------------------------
    #  Version: v_1976_to_2016_by_20121009_lowe_d_m
    # ------------------------------------------------------------------------------------------------------------------

    @staticmethod
    def _download_v_1976_to_2016_by_20121009_lowe_d_m(
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Download the data from the `v_1976_to_2016_by_20121009_lowe_d_m` version of the chemical reaction dataset.

        :parameter output_directory_path: The path to the output directory where the data should be downloaded.
        """

        AbstractBaseDataSource._download_file(
            file_url="https://figshare.com/ndownloader/articles/5104873/versions/1",
            file_name="5104873.zip",
            output_directory_path=output_directory_path
        )

    @staticmethod
    def _extract_v_1976_to_2016_by_20121009_lowe_d_m(
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Extract the data from the `v_1976_to_2016_by_20121009_lowe_d_m` version of the chemical reaction dataset.

        :parameter input_directory_path: The path to the input directory where the data is downloaded.
        :parameter output_directory_path: The path to the output directory where the data should be extracted.
        """

        with ZipFile(
            file=Path(input_directory_path, "5104873.zip")
        ) as zip_archive_file_handle:
            for seven_zip_archive_file_name in [
                "1976_Sep2016_USPTOgrants_smiles.7z",
                "2001_Sep2016_USPTOapplications_smiles.7z",
            ]:
                with zip_archive_file_handle.open(
                    name=seven_zip_archive_file_name
                ) as seven_zip_archive_file_handle:
                    with open(
                        file=Path(output_directory_path, seven_zip_archive_file_name),
                        mode="wb"
                    ) as destination_file_handle:
                        copyfileobj(
                            fsrc=seven_zip_archive_file_handle,
                            fdst=destination_file_handle
                        )

                with SevenZipFile(
                    file=Path(input_directory_path, seven_zip_archive_file_name)
                ) as seven_zip_archive_file_handle:
                    seven_zip_archive_file_handle.extractall(
                        path=output_directory_path
                    )

    @staticmethod
    def _format_v_1976_to_2016_by_20121009_lowe_d_m(
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Format the data from the `v_1976_to_2016_by_20121009_lowe_d_m` version of the chemical reaction dataset.

        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        dataframes = list()

        for file_name in [
            "1976_Sep2016_USPTOgrants_smiles.rsmi",
            "2001_Sep2016_USPTOapplications_smiles.rsmi",
        ]:
            dataframe = read_csv(
                filepath_or_buffer=Path(input_directory_path, file_name),
                sep="\t",
                header=0,
                low_memory=False
            )

            dataframe["FileName"] = file_name

            dataframes.append(
                dataframe
            )

        concat(
            objs=dataframes
        ).to_csv(
            path_or_buf=Path(
                output_directory_path,
                "{timestamp:s}_uspto_v_1976_to_2016_by_20121009_lowe_d_m.csv".format(
                    timestamp=datetime.now().strftime(
                        format="%Y%m%d%H%M%S"
                    )
                )
            ),
            index=False
        )

    # ------------------------------------------------------------------------------------------------------------------
    #  Version: v_50k_by_20171116_coley_c_w_et_al
    # ------------------------------------------------------------------------------------------------------------------

    @staticmethod
    def _download_v_50k_by_20171116_coley_c_w_et_al(
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Download the data from the `v_50k_by_20171116_coley_c_w_et_al` version of the chemical reaction dataset.

        :parameter output_directory_path: The path to the output directory where the data should be downloaded.
        """

        AbstractBaseDataSource._download_file(
            file_url="https://raw.githubusercontent.com/connorcoley/retrosim/master/{file_url_suffix:s}".format(
                file_url_suffix="retrosim/data/data_processed.csv"
            ),
            file_name="data_processed.csv",
            output_directory_path=output_directory_path
        )

    @staticmethod
    def _format_v_50k_by_20171116_coley_c_w_et_al(
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Format the data from the `v_50k_by_20171116_coley_c_w_et_al` version of the chemical reaction dataset.

        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        read_csv(
            filepath_or_buffer=Path(input_directory_path, "data_processed.csv"),
            header=0,
            index_col=0
        ).to_csv(
            path_or_buf=Path(
                output_directory_path,
                "{timestamp:s}_uspto_v_50k_by_20171116_coley_c_w_et_al.csv".format(
                    timestamp=datetime.now().strftime(
                        format="%Y%m%d%H%M%S"
                    )
                )
            ),
            index=False
        )

    # ------------------------------------------------------------------------------------------------------------------
    #  Version: v_480k_or_mit_by_20171204_jin_w_et_al
    # ------------------------------------------------------------------------------------------------------------------

    @staticmethod
    def _download_v_480k_or_mit_by_20171204_jin_w_et_al(
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Download the data from the `v_480k_or_mit_by_20171204_jin_w_et_al` version of the chemical reaction dataset.

        :parameter output_directory_path: The path to the output directory where the data should be downloaded.
        """

        AbstractBaseDataSource._download_file(
            file_url="https://raw.githubusercontent.com/wengong-jin/nips17-rexgen/master/USPTO/data.zip",
            file_name="data.zip",
            output_directory_path=output_directory_path
        )

    @staticmethod
    def _extract_v_480k_or_mit_by_20171204_jin_w_et_al(
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Extract the data from the `v_480k_or_mit_by_20171204_jin_w_et_al` version of the chemical reaction dataset.

        :parameter input_directory_path: The path to the input directory where the data is downloaded.
        :parameter output_directory_path: The path to the output directory where the data should be extracted.
        """

        with ZipFile(
            file=Path(input_directory_path, "data.zip")
        ) as zip_archive_file_handle:
            for file_name in [
                "train.txt",
                "valid.txt",
                "test.txt",
            ]:
                with zip_archive_file_handle.open(
                    name="data/{file_name:s}".format(
                        file_name=file_name
                    )
                ) as source_file_handle:
                    with open(
                        file=Path(output_directory_path, file_name),
                        mode="wb"
                    ) as destination_file_handle:
                        copyfileobj(
                            fsrc=source_file_handle,
                            fdst=destination_file_handle
                        )

    @staticmethod
    def _format_v_480k_or_mit_by_20171204_jin_w_et_al(
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Format the data from the `v_480k_or_mit_by_20171204_jin_w_et_al` version of the chemical reaction dataset.

        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        dataframes = list()

        for file_name in [
            "train.txt",
            "valid.txt",
            "test.txt",
        ]:
            dataframe = read_csv(
                filepath_or_buffer=Path(input_directory_path, file_name),
                sep="\t",
                header=None
            )

            dataframe["file_name"] = file_name

            dataframes.append(
                dataframe
            )

        concat(
            objs=dataframes
        ).rename(
            columns={
                0: "reaction_smiles",
            }
        ).to_csv(
            path_or_buf=Path(
                output_directory_path,
                "{timestamp:s}_uspto_v_480k_or_mit_by_20171229_jin_w_et_al.csv".format(
                    timestamp=datetime.now().strftime(
                        format="%Y%m%d%H%M%S"
                    )
                )
            ),
            index=False
        )

    # ------------------------------------------------------------------------------------------------------------------
    #  Version: v_480k_or_mit_by_20180622_schwaller_p_et_al
    # ------------------------------------------------------------------------------------------------------------------

    @staticmethod
    def _download_v_480k_or_mit_by_20180622_schwaller_p_et_al(
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Download the data from the `v_480k_or_mit_by_20180622_schwaller_p_et_al` version of the chemical reaction
        dataset.

        :parameter output_directory_path: The path to the output directory where the data should be downloaded.
        """

        AbstractBaseDataSource._download_file(
            file_url=AbstractBaseDataSource._send_http_get_request(
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
    def _extract_v_480k_or_mit_by_20180622_schwaller_p_et_al(
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Extract the data from the `v_480k_or_mit_by_20180622_schwaller_p_et_al` version of the chemical reaction
        dataset.

        :parameter input_directory_path: The path to the input directory where the data is downloaded.
        :parameter output_directory_path: The path to the output directory where the data should be extracted.
        """

        with ZipFile(
            file=Path(input_directory_path, "ReactionSeq2Seq_Dataset.zip")
        ) as zip_archive_file_handle:
            for file_name in [
                "Jin_USPTO_1product_train.txt",
                "Jin_USPTO_1product_valid.txt",
                "Jin_USPTO_1product_test.txt",
            ]:
                with zip_archive_file_handle.open(
                    name="ReactionSeq2Seq_Dataset/{file_name:s}".format(
                        file_name=file_name
                    )
                ) as source_file_handle:
                    with open(
                        file=Path(output_directory_path, file_name),
                        mode="wb"
                    ) as destination_file_handle:
                        copyfileobj(
                            fsrc=source_file_handle,
                            fdst=destination_file_handle
                        )

    @staticmethod
    def _format_v_480k_or_mit_by_20180622_schwaller_p_et_al(
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Format the data from the `v_480k_or_mit_by_20180622_schwaller_p_et_al` version of the chemical reaction dataset.

        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        dataframes = list()

        for file_name in [
            "Jin_USPTO_1product_train.txt",
            "Jin_USPTO_1product_valid.txt",
            "Jin_USPTO_1product_test.txt",
        ]:
            dataframe = read_csv(
                filepath_or_buffer=Path(input_directory_path, file_name),
                sep="\t",
                header=None,
                skiprows=[0, ]
            )

            dataframe["file_name"] = file_name

            dataframes.append(
                dataframe
            )

        concat(
            objs=dataframes
        ).rename(
            columns={
                0: "reaction_smiles",
            }
        ).to_csv(
            path_or_buf=Path(
                output_directory_path,
                "{timestamp:s}_uspto_v_480k_or_mit_by_20180622_schwaller_p_et_al.csv".format(
                    timestamp=datetime.now().strftime(
                        format="%Y%m%d%H%M%S"
                    )
                )
            ),
            index=False
        )

    # ------------------------------------------------------------------------------------------------------------------
    #  Version: v_stereo_by_20180622_schwaller_p_et_al
    # ------------------------------------------------------------------------------------------------------------------

    @staticmethod
    def _download_v_stereo_by_20180622_schwaller_p_et_al(
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Download the data from the `v_stereo_by_20180622_schwaller_p_et_al` version of the chemical reaction dataset.

        :parameter output_directory_path: The path to the output directory where the data should be downloaded.
        """

        AbstractBaseDataSource._download_file(
            file_url=AbstractBaseDataSource._send_http_get_request(
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
    def _extract_v_stereo_by_20180622_schwaller_p_et_al(
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Extract the data from the `v_stereo_by_20180622_schwaller_p_et_al` version of the chemical reaction dataset.

        :parameter input_directory_path: The path to the input directory where the data is downloaded.
        :parameter output_directory_path: The path to the output directory where the data should be extracted.
        """

        with ZipFile(
            file=Path(input_directory_path, "ReactionSeq2Seq_Dataset.zip")
        ) as zip_archive_file_handle:
            for file_name in [
                "US_patents_1976-Sep2016_1product_reactions_train.csv",
                "US_patents_1976-Sep2016_1product_reactions_valid.csv",
                "US_patents_1976-Sep2016_1product_reactions_test.csv",
            ]:
                with zip_archive_file_handle.open(
                    name="ReactionSeq2Seq_Dataset/{file_name:s}".format(
                        file_name=file_name
                    )
                ) as source_file_handle:
                    with open(
                        file=Path(output_directory_path, file_name),
                        mode="wb"
                    ) as destination_file_handle:
                        copyfileobj(
                            fsrc=source_file_handle,
                            fdst=destination_file_handle
                        )

    @staticmethod
    def _format_v_stereo_by_20180622_schwaller_p_et_al(
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Format the data from the `v_stereo_by_20180622_schwaller_p_et_al` version of the chemical reaction dataset.

        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        dataframes = list()

        for file_name in [
            "US_patents_1976-Sep2016_1product_reactions_train.csv",
            "US_patents_1976-Sep2016_1product_reactions_valid.csv",
            "US_patents_1976-Sep2016_1product_reactions_test.csv",
        ]:
            dataframe = read_csv(
                filepath_or_buffer=Path(input_directory_path, file_name),
                sep="\t",
                header=2,
                low_memory=False
            )

            dataframe["FileName"] = file_name

            dataframes.append(
                dataframe
            )

        concat(
            objs=dataframes
        ).rename(
            columns={
                0: "reaction_smiles",
            }
        ).to_csv(
            path_or_buf=Path(
                output_directory_path,
                "{timestamp:s}_uspto_v_stereo_by_20180622_schwaller_p_et_al.csv".format(
                    timestamp=datetime.now().strftime(
                        format="%Y%m%d%H%M%S"
                    )
                )
            ),
            index=False
        )

    # ------------------------------------------------------------------------------------------------------------------
    #  Version: v_1k_tpl_by_20210128_schwaller_p_et_al
    # ------------------------------------------------------------------------------------------------------------------

    @staticmethod
    def _download_v_1k_tpl_by_20210128_schwaller_p_et_al(
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Download the data from the `v_1k_tpl_by_20210128_schwaller_p_et_al` version of the chemical reaction dataset.

        :parameter output_directory_path: The path to the output directory where the data should be downloaded.
        """

        AbstractBaseDataSource._download_file(
            file_url=AbstractBaseDataSource._send_http_get_request(
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
    def _extract_v_1k_tpl_by_20210128_schwaller_p_et_al(
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Extract the data from the `v_1k_tpl_by_20210128_schwaller_p_et_al` version of the chemical reaction dataset.

        :parameter input_directory_path: The path to the input directory where the data is downloaded.
        :parameter output_directory_path: The path to the output directory where the data should be extracted.
        """

        with ZipFile(
            file=Path(input_directory_path, "MappingChemicalReactions.zip")
        ) as zip_archive_file_handle:
            for file_name in [
                "uspto_1k_TPL_test.tsv.gzip",
                "uspto_1k_TPL_train_valid.tsv.gzip",
            ]:
                with zip_archive_file_handle.open(
                    name="data_set/{file_name:s}".format(
                        file_name=file_name
                    )
                ) as source_file_handle:
                    with open(
                        file=Path(output_directory_path, file_name),
                        mode="wb"
                    ) as destination_file_handle:
                        copyfileobj(
                            fsrc=source_file_handle,
                            fdst=destination_file_handle
                        )

                with open_gzip_archive_file(
                    filename=Path(input_directory_path, file_name)
                ) as gzip_archive_file_handle:
                    with open(
                        file=Path(output_directory_path, file_name[:-5]),
                        mode="wb"
                    ) as file_handle:
                        copyfileobj(
                            fsrc=gzip_archive_file_handle,
                            fdst=file_handle
                        )

    @staticmethod
    def _format_v_1k_tpl_by_20210128_schwaller_p_et_al(
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Format the data from the `v_1k_tpl_by_20210128_schwaller_p_et_al` version of the chemical reaction dataset.

        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        dataframes = list()

        for file_name in [
            "uspto_1k_TPL_test.tsv",
            "uspto_1k_TPL_train_valid.tsv",
        ]:
            dataframe = read_csv(
                filepath_or_buffer=Path(input_directory_path, file_name),
                sep="\t",
                header=0,
                index_col=0
            )

            dataframe["file_name"] = file_name

            dataframes.append(
                dataframe
            )

        concat(
            objs=dataframes
        ).to_csv(
            path_or_buf=Path(
                output_directory_path,
                "{timestamp:s}_uspto_v_1k_tpl_by_20210705_schwaller_p_et_al.csv".format(
                    timestamp=datetime.now().strftime(
                        format="%Y%m%d%H%M%S"
                    )
                )
            ),
            index=False
        )

    # ------------------------------------------------------------------------------------------------------------------
    #  Version: v_1k_tpl_by_20210128_schwaller_p_et_al
    # ------------------------------------------------------------------------------------------------------------------

    @staticmethod
    def _download_v_1976_to_2016_by_20210407_schwaller_p_et_al(
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Download the data from the `v_1976_to_2016_by_20210407_schwaller_p_et_al` version of the chemical reaction
        dataset.

        :parameter output_directory_path: The path to the output directory where the data should be downloaded.
        """

        AbstractBaseDataSource._download_file(
            file_url=AbstractBaseDataSource._send_http_get_request(
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
    def _extract_v_1976_to_2016_by_20210407_schwaller_p_et_al(
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Extract the data from the `v_1976_to_2016_by_20210407_schwaller_p_et_al` version of the chemical reaction
        dataset.

        :parameter input_directory_path: The path to the input directory where the data is downloaded.
        :parameter output_directory_path: The path to the output directory where the data should be extracted.
        """

        with ZipFile(
            file=Path(input_directory_path, "USPTO_remapped.zip")
        ) as zip_archive_file_handle:
            for file_name in [
                "1976_Sep2016_USPTOgrants_smiles_mapped.tsv",
                "2001_Sep2016_USPTOapplications_smiles_mapped.tsv",
            ]:
                with zip_archive_file_handle.open(
                    name="USPTO_remapped/{file_name:s}".format(
                        file_name=file_name
                    )
                ) as source_file_handle:
                    with open(
                        file=Path(output_directory_path, file_name),
                        mode="wb"
                    ) as destination_file_handle:
                        copyfileobj(
                            fsrc=source_file_handle,
                            fdst=destination_file_handle
                        )

    @staticmethod
    def _format_v_1976_to_2016_by_20210407_schwaller_p_et_al(
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Format the data from the `v_1976_to_2016_by_20210407_schwaller_p_et_al` version of the chemical reaction
        dataset.

        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        dataframes = list()

        for file_name in [
            "1976_Sep2016_USPTOgrants_smiles_mapped.tsv",
            "2001_Sep2016_USPTOapplications_smiles_mapped.tsv",
        ]:
            dataframe = read_csv(
                filepath_or_buffer=Path(input_directory_path, file_name),
                sep="\t",
                header=0,
                index_col=0
            )

            dataframe["file_name"] = file_name

            dataframes.append(
                dataframe
            )

        concat(
            objs=dataframes
        ).to_csv(
            path_or_buf=Path(
                output_directory_path,
                "{timestamp:s}_uspto_v_1976_to_2016_by_20210407_schwaller_p_et_al.csv".format(
                    timestamp=datetime.now().strftime(
                        format="%Y%m%d%H%M%S"
                    )
                )
            ),
            index=False
        )

    # ------------------------------------------------------------------------------------------------------------------
    #  Version: v_1976_to_2016_by_20240313_chen_s_et_al
    # ------------------------------------------------------------------------------------------------------------------

    @staticmethod
    def _download_v_1976_to_2016_by_20240313_chen_s_et_al(
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Download the data from the `v_1976_to_2016_by_20240313_chen_s_et_al` version of the chemical reaction dataset.

        :parameter output_directory_path: The path to the output directory where the data should be downloaded.
        """

        AbstractBaseDataSource._download_file(
            file_url="https://figshare.com/ndownloader/files/44192531",
            file_name="remapped_USPTO_FULL.csv",
            output_directory_path=output_directory_path
        )

    @staticmethod
    def _format_v_1976_to_2016_by_20240313_chen_s_et_al(
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Format the data from the `v_1976_to_2016_by_20240313_chen_s_et_al` version of the chemical reaction dataset.

        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        read_csv(
            filepath_or_buffer=Path(input_directory_path, "remapped_USPTO_FULL.csv"),
            header=0
        ).to_csv(
            path_or_buf=Path(
                output_directory_path,
                "{timestamp:s}_uspto_v_1976_to_2016_by_20240313_chen_s_et_al.csv".format(
                    timestamp=datetime.now().strftime(
                        format="%Y%m%d%H%M%S"
                    )
                )
            ),
            index=False
        )

    # ------------------------------------------------------------------------------------------------------------------
    #  Version: v_50k_by_20240313_chen_s_et_al
    # ------------------------------------------------------------------------------------------------------------------

    @staticmethod
    def _download_v_50k_by_20240313_chen_s_et_al(
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Download the data from the `v_50k_by_20240313_chen_s_et_al` version of the chemical reaction dataset.

        :parameter output_directory_path: The path to the output directory where the data should be downloaded.
        """

        AbstractBaseDataSource._download_file(
            file_url="https://figshare.com/ndownloader/files/44192528",
            file_name="remapped_USPTO_50K.csv",
            output_directory_path=output_directory_path
        )

    @staticmethod
    def _format_v_50k_by_20240313_chen_s_et_al(
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Format the data from the `v_50k_by_20240313_chen_s_et_al` version of the chemical reaction dataset.

        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        read_csv(
            filepath_or_buffer=Path(input_directory_path, "remapped_USPTO_50K.csv"),
            header=0
        ).to_csv(
            path_or_buf=Path(
                output_directory_path,
                "{timestamp:s}_uspto_v_50k_by_20240313_chen_s_et_al.csv".format(
                    timestamp=datetime.now().strftime(
                        format="%Y%m%d%H%M%S"
                    )
                )
            ),
            index=False
        )

    # ------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------

    def download(
            self,
            version: str,
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Download the data from the chemical reaction dataset.

        :parameter version: The version of the chemical reaction dataset.
        :parameter output_directory_path: The path to the output directory where the data should be downloaded.
        """

        try:
            if version in self.available_versions.keys():
                if self.logger is not None:
                    self.logger.info(
                        msg="The download of the data from the {data_source:s} has been started.".format(
                            data_source="USPTO chemical reaction dataset ({version:s})".format(
                                version=version
                            )
                        )
                    )

                if version == "v_1976_to_2013_by_20121009_lowe_d_m":
                    self._download_v_1976_to_2013_by_20121009_lowe_d_m(
                        output_directory_path=output_directory_path
                    )

                if version == "v_50k_by_20161122_schneider_n_et_al":
                    self._download_v_50k_by_20161122_schneider_n_et_al(
                        output_directory_path=output_directory_path
                    )

                if version == "v_15k_by_20170418_coley_c_w_et_al":
                    self._download_v_15k_by_20170418_coley_c_w_et_al(
                        output_directory_path=output_directory_path
                    )

                if version == "v_1976_to_2016_by_20121009_lowe_d_m":
                    self._download_v_1976_to_2016_by_20121009_lowe_d_m(
                        output_directory_path=output_directory_path
                    )

                if version == "v_50k_by_20171116_coley_c_w_et_al":
                    self._download_v_50k_by_20171116_coley_c_w_et_al(
                        output_directory_path=output_directory_path
                    )

                if version == "v_480k_or_mit_by_20171204_jin_w_et_al":
                    self._download_v_480k_or_mit_by_20171204_jin_w_et_al(
                        output_directory_path=output_directory_path
                    )

                if version == "v_480k_or_mit_by_20180622_schwaller_p_et_al":
                    self._download_v_480k_or_mit_by_20180622_schwaller_p_et_al(
                        output_directory_path=output_directory_path
                    )

                if version == "v_stereo_by_20180622_schwaller_p_et_al":
                    self._download_v_stereo_by_20180622_schwaller_p_et_al(
                        output_directory_path=output_directory_path
                    )

                if version == "v_1k_tpl_by_20210128_schwaller_p_et_al":
                    self._download_v_1k_tpl_by_20210128_schwaller_p_et_al(
                        output_directory_path=output_directory_path
                    )

                if version == "v_1976_to_2016_by_20210407_schwaller_p_et_al":
                    self._download_v_1976_to_2016_by_20210407_schwaller_p_et_al(
                        output_directory_path=output_directory_path
                    )

                if version == "v_1976_to_2016_by_20240313_chen_s_et_al":
                    self._download_v_1976_to_2016_by_20240313_chen_s_et_al(
                        output_directory_path=output_directory_path
                    )

                if version == "v_50k_by_20240313_chen_s_et_al":
                    self._download_v_50k_by_20240313_chen_s_et_al(
                        output_directory_path=output_directory_path
                    )

                if self.logger is not None:
                    self.logger.info(
                        msg="The download of the data from the {data_source:s} has been completed.".format(
                            data_source="USPTO chemical reaction dataset ({version:s})".format(
                                version=version
                            )
                        )
                    )

            else:
                raise ValueError(
                    "The {data_source:s} is not supported.".format(
                        data_source="USPTO chemical reaction dataset ({version:s})".format(
                            version=version
                        )
                    )
                )

        except Exception as exception_handle:
            if self.logger is not None:
                self.logger.error(
                    msg=exception_handle
                )

    def extract(
            self,
            version: str,
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Extract the data from the chemical reaction dataset.

        :parameter version: The version of the chemical reaction dataset.
        :parameter input_directory_path: The path to the input directory where the data is downloaded.
        :parameter output_directory_path: The path to the output directory where the data should be extracted.
        """

        try:
            if version in self.available_versions.keys():
                if self.logger is not None:
                    self.logger.info(
                        msg="The extraction of the data from the {data_source:s} has been started.".format(
                            data_source="USPTO chemical reaction dataset ({version:s})".format(
                                version=version
                            )
                        )
                    )

                if version == "v_1976_to_2013_by_20121009_lowe_d_m":
                    self._extract_v_1976_to_2013_by_20121009_lowe_d_m(
                        input_directory_path=input_directory_path,
                        output_directory_path=output_directory_path
                    )

                if version == "v_50k_by_20161122_schneider_n_et_al":
                    self._extract_v_50k_by_20161122_schneider_n_et_al(
                        input_directory_path=input_directory_path,
                        output_directory_path=output_directory_path
                    )

                if version == "v_15k_by_20170418_coley_c_w_et_al":
                    self._extract_v_15k_by_20170418_coley_c_w_et_al(
                        input_directory_path=input_directory_path,
                        output_directory_path=output_directory_path
                    )

                if version == "v_1976_to_2016_by_20121009_lowe_d_m":
                    self._extract_v_1976_to_2016_by_20121009_lowe_d_m(
                        input_directory_path=input_directory_path,
                        output_directory_path=output_directory_path
                    )

                if version == "v_480k_or_mit_by_20171204_jin_w_et_al":
                    self._extract_v_480k_or_mit_by_20171204_jin_w_et_al(
                        input_directory_path=input_directory_path,
                        output_directory_path=output_directory_path
                    )

                if version == "v_480k_or_mit_by_20180622_schwaller_p_et_al":
                    self._extract_v_480k_or_mit_by_20180622_schwaller_p_et_al(
                        input_directory_path=input_directory_path,
                        output_directory_path=output_directory_path
                    )

                if version == "v_stereo_by_20180622_schwaller_p_et_al":
                    self._extract_v_stereo_by_20180622_schwaller_p_et_al(
                        input_directory_path=input_directory_path,
                        output_directory_path=output_directory_path
                    )

                if version == "v_1k_tpl_by_20210128_schwaller_p_et_al":
                    self._extract_v_1k_tpl_by_20210128_schwaller_p_et_al(
                        input_directory_path=input_directory_path,
                        output_directory_path=output_directory_path
                    )

                if version == "v_1976_to_2016_by_20210407_schwaller_p_et_al":
                    self._extract_v_1976_to_2016_by_20210407_schwaller_p_et_al(
                        input_directory_path=input_directory_path,
                        output_directory_path=output_directory_path
                    )

                if self.logger is not None:
                    self.logger.info(
                        msg="The extraction of the data from the {data_source:s} has been completed.".format(
                            data_source="USPTO chemical reaction dataset ({version:s})".format(
                                version=version
                            )
                        )
                    )

            else:
                raise ValueError(
                    "The {data_source:s} is not supported.".format(
                        data_source="USPTO chemical reaction dataset ({version:s})".format(
                            version=version
                        )
                    )
                )

        except Exception as exception_handle:
            if self.logger is not None:
                self.logger.error(
                    msg=exception_handle
                )

            raise

    def format(
            self,
            version: str,
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Format the data.

        :parameter version: The version of the chemical reaction dataset.
        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        try:
            if version in self.available_versions.keys():
                if self.logger is not None:
                    self.logger.info(
                        msg="The formatting of the data from the {data_source:s} has been started.".format(
                            data_source="USPTO chemical reaction dataset ({version:s})".format(
                                version=version
                            )
                        )
                    )

                if version == "v_1976_to_2013_by_20121009_lowe_d_m":
                    self._format_v_1976_to_2013_by_20121009_lowe_d_m(
                        input_directory_path=input_directory_path,
                        output_directory_path=output_directory_path
                    )

                if version == "v_50k_by_20161122_schneider_n_et_al":
                    self._format_v_50k_by_20161122_schneider_n_et_al(
                        input_directory_path=input_directory_path,
                        output_directory_path=output_directory_path
                    )

                if version == "v_15k_by_20170418_coley_c_w_et_al":
                    self._format_v_15k_by_20170418_coley_c_w_et_al(
                        input_directory_path=input_directory_path,
                        output_directory_path=output_directory_path
                    )

                if version == "v_1976_to_2016_by_20121009_lowe_d_m":
                    self._format_v_1976_to_2016_by_20121009_lowe_d_m(
                        input_directory_path=input_directory_path,
                        output_directory_path=output_directory_path
                    )

                if version == "v_50k_by_20171116_coley_c_w_et_al":
                    self._format_v_50k_by_20171116_coley_c_w_et_al(
                        input_directory_path=input_directory_path,
                        output_directory_path=output_directory_path
                    )

                if version == "v_480k_or_mit_by_20171204_jin_w_et_al":
                    self._format_v_480k_or_mit_by_20171204_jin_w_et_al(
                        input_directory_path=input_directory_path,
                        output_directory_path=output_directory_path
                    )

                if version == "v_480k_or_mit_by_20180622_schwaller_p_et_al":
                    self._format_v_480k_or_mit_by_20180622_schwaller_p_et_al(
                        input_directory_path=input_directory_path,
                        output_directory_path=output_directory_path
                    )

                if version == "v_stereo_by_20180622_schwaller_p_et_al":
                    self._format_v_stereo_by_20180622_schwaller_p_et_al(
                        input_directory_path=input_directory_path,
                        output_directory_path=output_directory_path
                    )

                if version == "v_1k_tpl_by_20210128_schwaller_p_et_al":
                    self._format_v_1k_tpl_by_20210128_schwaller_p_et_al(
                        input_directory_path=input_directory_path,
                        output_directory_path=output_directory_path
                    )

                if version == "v_1976_to_2016_by_20210407_schwaller_p_et_al":
                    self._format_v_1976_to_2016_by_20210407_schwaller_p_et_al(
                        input_directory_path=input_directory_path,
                        output_directory_path=output_directory_path
                    )

                if version == "v_1976_to_2016_by_20240313_chen_s_et_al":
                    self._format_v_1976_to_2016_by_20240313_chen_s_et_al(
                        input_directory_path=input_directory_path,
                        output_directory_path=output_directory_path
                    )

                if version == "v_50k_by_20240313_chen_s_et_al":
                    self._format_v_50k_by_20240313_chen_s_et_al(
                        input_directory_path=input_directory_path,
                        output_directory_path=output_directory_path
                    )

                if self.logger is not None:
                    self.logger.info(
                        msg="The formatting of the data from the {data_source:s} has been completed.".format(
                            data_source="USPTO chemical reaction dataset ({version:s})".format(
                                version=version
                            )
                        )
                    )

            else:
                raise ValueError(
                    "The {data_source:s} is not supported.".format(
                        data_source="USPTO chemical reaction dataset ({version:s})".format(
                            version=version
                        )
                    )
                )

        except Exception as exception_handle:
            if self.logger is not None:
                self.logger.error(
                    msg=exception_handle
                )

            raise
