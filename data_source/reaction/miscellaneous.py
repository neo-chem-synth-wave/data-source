""" The ``data_source.reaction`` package ``miscellaneous`` module. """

from datetime import datetime
from logging import Logger
from os import PathLike
from pathlib import Path
from typing import Dict, Optional, Union

from pandas.core.frame import DataFrame
from pandas.core.reshape.concat import concat
from pandas.io.parquet import read_parquet
from pandas.io.parsers.readers import read_csv

from rdkit.Chem.rdChemReactions import ReactionFromRxnBlock, ReactionToSmiles

from zipfile import ZipFile

from data_source.abstract_base.abstract_base import AbstractBaseDataSource


class MiscellaneousReactionDataSource(AbstractBaseDataSource):
    """ The miscellaneous chemical reaction data source class. """

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
        Get the available versions of the chemical reaction data source.

        :returns: The available versions of the chemical reaction data source.
        """

        return {
            "v_20131008_kraut_h_et_al": "https://doi.org/10.1021/ci400442f",
            "v_20161014_wei_j_n_et_al": "https://doi.org/10.1021/acscentsci.6b00219",
            "v_20200508_grambow_c_et_al": "https://zenodo.org/doi/10.5281/zenodo.3581266",
            "v_20200508_grambow_c_et_al_add_on": "https://zenodo.org/doi/10.5281/zenodo.3731553",
            "v_20211103_lin_a_et_al": "https://doi.org/10.1002/minf.202100138",
            "v_20220718_spiekermann_k_et_al": "https://zenodo.org/doi/10.5281/zenodo.5652097",
            "v_20240422_wigh_d_s_et_al": "https://doi.org/10.6084/m9.figshare.23298467.v4"
        }

    # ------------------------------------------------------------------------------------------------------------------
    #  Version: v_20131008_kraut_h_et_al
    # ------------------------------------------------------------------------------------------------------------------

    @staticmethod
    def _download_v_20131008_kraut_h_et_al(
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Download the data from the `v_20131008_kraut_h_et_al` version of the chemical reaction data source.

        :parameter output_directory_path: The path to the output directory where the data should be downloaded.
        """

        AbstractBaseDataSource._download_file(
            file_url="https://ndownloader.figstatic.com/files/3988891",
            file_name="ci400442f_si_002.zip",
            output_directory_path=output_directory_path
        )

    @staticmethod
    def _extract_v_20131008_kraut_h_et_al(
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
    def _format_v_20131008_kraut_h_et_al(
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Format the data from the `v_20131008_kraut_h_et_al` version of the chemical reaction data source.

        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        dataframe_rows = list()

        for file_name in [
            "MapTestExamplesV1.0.rdf",
            "MapTestExamplesV1_ICMapRctCpy.rdf",
            "MapTestExamplesV1_ICMap.rdf",
        ]:
            with open(
                file=Path(input_directory_path, file_name)
            ) as file_handle:
                for reaction_rxn_block_without_identifier in file_handle.read().split(
                    sep="$RXN"
                )[1:]:
                    reaction_rxn = ReactionFromRxnBlock(
                        rxnblock="$RXN{reaction_rxn_block_without_identifier:s}".format(
                            reaction_rxn_block_without_identifier=reaction_rxn_block_without_identifier
                        )
                    )

                    if reaction_rxn is not None:
                        reaction_smiles = ReactionToSmiles(
                            reaction=reaction_rxn
                        )

                        if reaction_smiles is not None:
                            dataframe_rows.append((
                                reaction_smiles,
                                file_name,
                            ))

        DataFrame(
            data=dataframe_rows,
            columns=[
                "reaction_smiles",
                "file_name",
            ]
        ).to_csv(
            path_or_buf=Path(
                output_directory_path,
                "{timestamp:s}_v_20131008_kraut_h_et_al.csv".format(
                    timestamp=datetime.now().strftime(
                        format="%Y%m%d%H%M%S"
                    )
                )
            ),
            index=False
        )

    # ------------------------------------------------------------------------------------------------------------------
    #  Version: v_20161014_wei_j_n_et_al
    # ------------------------------------------------------------------------------------------------------------------

    @staticmethod
    def _download_v_20161014_wei_j_n_et_al(
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
            AbstractBaseDataSource._download_file(
                file_url="https://raw.githubusercontent.com/jnwei/{file_url_suffix:s}".format(
                    file_url_suffix="neural_reaction_fingerprint/master/data/test_questions/{file_name:s}".format(
                        file_name=file_name
                    )
                ),
                file_name=file_name,
                output_directory_path=output_directory_path
            )

    @staticmethod
    def _format_v_20161014_wei_j_n_et_al(
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Format the data from the `v_20161014_wei_j_n_et_al` version of the chemical reaction data source.

        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        dataframes = list()

        for file_name in [
            "Wade8_47.ans_smi.txt",
            "Wade8_48.ans_smi.txt",
        ]:
            dataframe = read_csv(
                filepath_or_buffer=Path(input_directory_path, file_name),
                header=None
            ).rename(
                columns={
                    0: "reaction_smiles",
                }
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
                "{timestamp:s}_v_20161014_wei_j_n_et_al.csv".format(
                    timestamp=datetime.now().strftime(
                        format="%Y%m%d%H%M%S"
                    )
                )
            ),
            index=False
        )

    # ------------------------------------------------------------------------------------------------------------------
    #  Version: v_20200508_grambow_c_et_al
    # ------------------------------------------------------------------------------------------------------------------

    @staticmethod
    def _download_v_20200508_grambow_c_et_al(
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Download the data from the `v_20200508_grambow_c_et_al` version of the chemical reaction data source.

        :parameter output_directory_path: The path to the output directory where the data should be downloaded.
        """

        for file_name in [
            "b97d3.csv",
            "wb97xd3.csv",
        ]:
            AbstractBaseDataSource._download_file(
                file_url="https://zenodo.org/records/3715478/files/{file_name:s}".format(
                    file_name=file_name
                ),
                file_name=file_name,
                output_directory_path=output_directory_path
            )

    @staticmethod
    def _format_v_20200508_grambow_c_et_al(
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Format the data from the `v_20200508_grambow_c_et_al` version of the chemical reaction data source.

        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        dataframes = list()

        for file_name in [
            "b97d3.csv",
            "wb97xd3.csv",
        ]:
            dataframe = read_csv(
                filepath_or_buffer=Path(input_directory_path, file_name),
                header=0
            )

            dataframe["reaction_smiles"] = dataframe["rsmi"] + ">>" + dataframe["psmi"]
            dataframe["file_name"] = file_name

            dataframes.append(
                dataframe
            )

        concat(
            objs=dataframes
        ).to_csv(
            path_or_buf=Path(
                output_directory_path,
                "{timestamp:s}_miscellaneous_v_20200508_grambow_c_et_al.csv".format(
                    timestamp=datetime.now().strftime(
                        format="%Y%m%d%H%M%S"
                    )
                )
            ),
            index=False
        )

    # ------------------------------------------------------------------------------------------------------------------
    #  Version: v_20200508_grambow_c_et_al_add_on
    # ------------------------------------------------------------------------------------------------------------------

    @staticmethod
    def _download_v_20200508_grambow_c_et_al_add_on(
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Download the data from the `v_20200508_grambow_c_et_al_add_on` version of the chemical reaction data source.

        :parameter output_directory_path: The path to the output directory where the data should be downloaded.
        """

        for file_name in [
            "b97d3_rad.csv",
            "wb97xd3_rad.csv",
        ]:
            AbstractBaseDataSource._download_file(
                file_url="https://zenodo.org/records/3731554/files/{file_name:s}".format(
                    file_name=file_name
                ),
                file_name=file_name,
                output_directory_path=output_directory_path
            )

    @staticmethod
    def _format_v_20200508_grambow_c_et_al_add_on(
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Format the data from the `v_20200508_grambow_c_et_al_add_on` version of the chemical reaction data source.

        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        dataframes = list()

        for file_name in [
            "b97d3_rad.csv",
            "wb97xd3_rad.csv",
        ]:
            dataframe = read_csv(
                filepath_or_buffer=Path(input_directory_path, file_name),
                header=0
            )

            dataframe["reaction_smiles"] = dataframe["rsmi"] + ">>" + dataframe["psmi"]
            dataframe["file_name"] = file_name

            dataframes.append(
                dataframe
            )

        concat(
            objs=dataframes
        ).to_csv(
            path_or_buf=Path(
                output_directory_path,
                "{timestamp:s}_v_20200508_grambow_c_et_al_add_on.csv".format(
                    timestamp=datetime.now().strftime(
                        format="%Y%m%d%H%M%S"
                    )
                )
            ),
            index=False
        )

    # ------------------------------------------------------------------------------------------------------------------
    #  Version: v_20211103_lin_a_et_al
    # ------------------------------------------------------------------------------------------------------------------

    @staticmethod
    def _download_v_20211103_lin_a_et_al(
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Download the data from the `v_20211103_lin_a_et_al` version of the chemical reaction data source.

        :parameter output_directory_path: The path to the output directory where the data should be downloaded.
        """

        AbstractBaseDataSource._download_file(
            file_url="https://github.com/Laboratoire-de-Chemoinformatique/{file_url_suffix:s}".format(
                file_url_suffix="Reaction_Data_Cleaning/raw/master/data/golden_dataset.zip"
            ),
            file_name="golden_dataset.zip",
            output_directory_path=output_directory_path
        )

    @staticmethod
    def _extract_v_20211103_lin_a_et_al(
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Extract the data from the `v_20211103_lin_a_et_al` version of the chemical reaction data source.

        :parameter input_directory_path: The path to the input directory where the data is downloaded.
        :parameter output_directory_path: The path to the output directory where the data should be extracted.
        """

        with ZipFile(
            file=Path(input_directory_path, "golden_dataset.zip")
        ) as zip_archive_file_handle:
            zip_archive_file_handle.extractall(
                path=output_directory_path
            )

    @staticmethod
    def _format_v_20211103_lin_a_et_al(
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Format the data from the `v_20211103_lin_a_et_al` version of the chemical reaction data source.

        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        dataframe_rows = list()

        with open(
            file=Path(input_directory_path, "golden_dataset.rdf")
        ) as file_handle:
            for reaction_rxn_block_without_identifier in file_handle.read().split(
                sep="$RXN"
            )[1:]:
                reaction_rxn = ReactionFromRxnBlock(
                    rxnblock="$RXN{reaction_rxn_block_without_identifier:s}".format(
                        reaction_rxn_block_without_identifier=reaction_rxn_block_without_identifier
                    )
                )

                if reaction_rxn is not None:
                    reaction_smiles = ReactionToSmiles(
                        reaction=reaction_rxn
                    )

                    if reaction_smiles is not None:
                        dataframe_rows.append(
                            reaction_smiles
                        )

        DataFrame(
            data=dataframe_rows,
            columns=[
                "reaction_smiles",
            ]
        ).to_csv(
            path_or_buf=Path(
                output_directory_path,
                "{timestamp:s}_v_20211103_lin_a_et_al.csv".format(
                    timestamp=datetime.now().strftime(
                        format="%Y%m%d%H%M%S"
                    )
                )
            ),
            index=False
        )

    # ------------------------------------------------------------------------------------------------------------------
    #  Version: v_20220718_spiekermann_k_et_al
    # ------------------------------------------------------------------------------------------------------------------

    @staticmethod
    def _download_v_20220718_spiekermann_k_et_al(
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Download the data from the `v_20220718_spiekermann_k_et_al` version of the chemical reaction data source.

        :parameter output_directory_path: The path to the output directory where the data should be downloaded.
        """

        for file_name in [
            "b97d3.csv",
            "wb97xd3.csv",
            "ccsdtf12_dz.csv",
            "ccsdtf12_tz.csv",
        ]:
            AbstractBaseDataSource._download_file(
                file_url="https://zenodo.org/records/6618262/files/{file_name:s}".format(
                    file_name=file_name
                ),
                file_name=file_name,
                output_directory_path=output_directory_path
            )

    @staticmethod
    def _format_v_20220718_spiekermann_k_et_al(
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Format the data from the `v_20220718_spiekermann_k_et_al` version of the chemical reaction data source.

        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        dataframes = list()

        for file_name in [
            "b97d3.csv",
            "wb97xd3.csv",
            "ccsdtf12_dz.csv",
            "ccsdtf12_tz.csv",
        ]:
            dataframe = read_csv(
                filepath_or_buffer=Path(input_directory_path, file_name),
                header=0
            )

            dataframe["reaction_smiles"] = dataframe["rsmi"] + ">>" + dataframe["psmi"]
            dataframe["file_name"] = file_name

            dataframes.append(
                dataframe
            )

        concat(
            objs=dataframes
        ).to_csv(
            path_or_buf=Path(
                output_directory_path,
                "{timestamp:s}_v_20220718_spiekermann_k_et_al.csv".format(
                    timestamp=datetime.now().strftime(
                        format="%Y%m%d%H%M%S"
                    )
                )
            ),
            index=False
        )

    # ------------------------------------------------------------------------------------------------------------------
    #  Version: v_20240422_wigh_d_s_et_al
    # ------------------------------------------------------------------------------------------------------------------

    @staticmethod
    def _download_v_20240422_wigh_d_s_et_al(
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Download the data from the `v_20240422_wigh_d_s_et_al` version of the chemical reaction data source.

        :parameter output_directory_path: The path to the output directory where the data should be downloaded.
        """

        for file_url, file_name in [
            ("https://figshare.com/ndownloader/files/44413040", "orderly_condition_test.parquet"),
            ("https://figshare.com/ndownloader/files/44413052", "orderly_condition_train.parquet"),
            ("https://figshare.com/ndownloader/files/44413043", "orderly_condition_with_rare_test.parquet"),
            ("https://figshare.com/ndownloader/files/44413055", "orderly_condition_with_rare_train.parquet"),
            ("https://figshare.com/ndownloader/files/44413046", "orderly_forward_test.parquet"),
            ("https://figshare.com/ndownloader/files/44413058", "orderly_forward_train.parquet"),
            ("https://figshare.com/ndownloader/files/44413049", "orderly_retro_test.parquet"),
            ("https://figshare.com/ndownloader/files/44413061", "orderly_retro_train.parquet"),
        ]:
            AbstractBaseDataSource._download_file(
                file_url=file_url,
                file_name=file_name,
                output_directory_path=output_directory_path
            )

    @staticmethod
    def _format_v_20240422_wigh_d_s_et_al(
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Format the data from the `v_20240422_wigh_d_s_et_al` version of the chemical reaction data source.

        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        dataframes = list()

        for file_name in [
            "orderly_condition_test.parquet",
            "orderly_condition_train.parquet",
            "orderly_condition_with_rare_test.parquet",
            "orderly_condition_with_rare_train.parquet",
            "orderly_forward_test.parquet",
            "orderly_forward_train.parquet",
            "orderly_retro_test.parquet",
            "orderly_retro_train.parquet",
        ]:
            dataframe = read_parquet(
                path=Path(input_directory_path, file_name)
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
                "{timestamp:s}_v_20240422_wigh_d_s_et_al.csv".format(
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
        Download the data from the chemical reaction data source.

        :parameter version: The version of the chemical reaction data source.
        :parameter output_directory_path: The path to the output directory where the data should be downloaded.
        """

        try:
            if version in self.available_versions.keys():
                if self.logger is not None:
                    self.logger.info(
                        msg="The download of the data from the {data_source:s} has been started.".format(
                            data_source="miscellaneous chemical reaction data source ({version:s})".format(
                                version=version
                            )
                        )
                    )

                if version == "v_20131008_kraut_h_et_al":
                    self._download_v_20131008_kraut_h_et_al(
                        output_directory_path=output_directory_path
                    )

                if version == "v_20161014_wei_j_n_et_al":
                    self._download_v_20161014_wei_j_n_et_al(
                        output_directory_path=output_directory_path
                    )

                if version == "v_20200508_grambow_c_et_al":
                    self._download_v_20200508_grambow_c_et_al(
                        output_directory_path=output_directory_path
                    )

                if version == "v_20200508_grambow_c_et_al_add_on":
                    self._download_v_20200508_grambow_c_et_al_add_on(
                        output_directory_path=output_directory_path
                    )

                if version == "v_20211103_lin_a_et_al":
                    self._download_v_20211103_lin_a_et_al(
                        output_directory_path=output_directory_path
                    )

                if version == "v_20220718_spiekermann_k_et_al":
                    self._download_v_20220718_spiekermann_k_et_al(
                        output_directory_path=output_directory_path
                    )

                if version == "v_20240422_wigh_d_s_et_al":
                    self._download_v_20240422_wigh_d_s_et_al(
                        output_directory_path=output_directory_path
                    )

                if self.logger is not None:
                    self.logger.info(
                        msg="The download of the data from the {data_source:s} has been completed.".format(
                            data_source="miscellaneous chemical reaction data source ({version:s})".format(
                                version=version
                            )
                        )
                    )

            else:
                raise ValueError(
                    "The {data_source:s} is not supported.".format(
                        data_source="miscellaneous chemical reaction data source ({version:s})".format(
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

    def extract(
            self,
            version: str,
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Extract the data from the chemical reaction data source.

        :parameter version: The version of the chemical reaction data source.
        :parameter input_directory_path: The path to the input directory where the data is downloaded.
        :parameter output_directory_path: The path to the output directory where the data should be extracted.
        """

        try:
            if version in self.available_versions.keys():
                if self.logger is not None:
                    self.logger.info(
                        msg="The extraction of the data from the {data_source:s} has been started.".format(
                            data_source="miscellaneous chemical reaction data source ({version:s})".format(
                                version=version
                            )
                        )
                    )

                if version == "v_20131008_kraut_h_et_al":
                    self._extract_v_20131008_kraut_h_et_al(
                        input_directory_path=input_directory_path,
                        output_directory_path=output_directory_path
                    )

                if version == "v_20211103_lin_a_et_al":
                    self._extract_v_20211103_lin_a_et_al(
                        input_directory_path=input_directory_path,
                        output_directory_path=output_directory_path
                    )

                if self.logger is not None:
                    self.logger.info(
                        msg="The extraction of the data from the {data_source:s} has been completed.".format(
                            data_source="miscellaneous chemical reaction data source ({version:s})".format(
                                version=version
                            )
                        )
                    )

            else:
                raise ValueError(
                    "The {data_source:s} is not supported.".format(
                        data_source="miscellaneous chemical reaction data source ({version:s})".format(
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
        Format the data from the chemical reaction data source.

        :parameter version: The version of the chemical reaction data source.
        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        try:
            if version in self.available_versions.keys():
                if self.logger is not None:
                    self.logger.info(
                        msg="The formatting of the data from the {data_source:s} has been started.".format(
                            data_source="miscellaneous chemical reaction data source ({version:s})".format(
                                version=version
                            )
                        )
                    )

                if version == "v_20131008_kraut_h_et_al":
                    self._format_v_20131008_kraut_h_et_al(
                        input_directory_path=input_directory_path,
                        output_directory_path=output_directory_path
                    )

                if version == "v_20161014_wei_j_n_et_al":
                    self._format_v_20161014_wei_j_n_et_al(
                        input_directory_path=input_directory_path,
                        output_directory_path=output_directory_path
                    )

                if version == "v_20200508_grambow_c_et_al":
                    self._format_v_20200508_grambow_c_et_al(
                        input_directory_path=input_directory_path,
                        output_directory_path=output_directory_path
                    )

                if version == "v_20200508_grambow_c_et_al_add_on":
                    self._format_v_20200508_grambow_c_et_al_add_on(
                        input_directory_path=input_directory_path,
                        output_directory_path=output_directory_path
                    )

                if version == "v_20211103_lin_a_et_al":
                    self._format_v_20211103_lin_a_et_al(
                        input_directory_path=input_directory_path,
                        output_directory_path=output_directory_path
                    )

                if version == "v_20220718_spiekermann_k_et_al":
                    self._format_v_20220718_spiekermann_k_et_al(
                        input_directory_path=input_directory_path,
                        output_directory_path=output_directory_path
                    )

                if version == "v_20240422_wigh_d_s_et_al":
                    self._format_v_20240422_wigh_d_s_et_al(
                        input_directory_path=input_directory_path,
                        output_directory_path=output_directory_path
                    )

                if self.logger is not None:
                    self.logger.info(
                        msg="The formatting of the data from the {data_source:s} has been completed.".format(
                            data_source="miscellaneous chemical reaction data source ({version:s})".format(
                                version=version
                            )
                        )
                    )

            else:
                raise ValueError(
                    "The {data_source:s} is not supported.".format(
                        data_source="miscellaneous chemical reaction data source ({version:s})".format(
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
