""" The ``data_source.reaction.miscellaneous`` package ``miscellaneous`` module. """

from logging import Logger
from os import PathLike
from typing import Dict, Optional, Union

from data_source.base.base import BaseDataSource

from data_source.reaction.miscellaneous.utility.download import MiscellaneousReactionDataSourceDownloadUtility
from data_source.reaction.miscellaneous.utility.extraction import MiscellaneousReactionDataSourceExtractionUtility
from data_source.reaction.miscellaneous.utility.formatting import MiscellaneousReactionDataSourceFormattingUtility


class MiscellaneousReactionDataSource(BaseDataSource):
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

    def get_supported_versions(
            self
    ) -> Dict[str, str]:
        """
        Get the supported versions of the chemical reaction data source.

        :returns: The supported versions of the chemical reaction data source.
        """

        try:
            return {
                "v_20131008_kraut_h_et_al": "https://doi.org/10.1021/ci400442f",
                "v_20161014_wei_j_n_et_al": "https://doi.org/10.1021/acscentsci.6b00219",
                "v_20200508_grambow_c_et_al": "https://zenodo.org/doi/10.5281/zenodo.3581266",
                "v_add_on_by_20200508_grambow_c_et_al": "https://zenodo.org/doi/10.5281/zenodo.3731553",
                "v_golden_dataset_by_20211103_lin_a_et_al": "https://doi.org/10.1002/minf.202100138",
                "v_rdb7_by_20220718_spiekermann_k_et_al": "https://zenodo.org/doi/10.5281/zenodo.5652097",
            }

        except Exception as exception_handle:
            if self.logger is not None:
                self.logger.error(
                    msg=exception_handle
                )

            raise

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
            if version in self.get_supported_versions().keys():
                if self.logger is not None:
                    self.logger.info(
                        msg="The download of the data from the {data_source:s} has been started.".format(
                            data_source="miscellaneous chemical reaction data source ({version:s})".format(
                                version=version
                            )
                        )
                    )

                if version == "v_20131008_kraut_h_et_al":
                    MiscellaneousReactionDataSourceDownloadUtility.download_v_20131008_kraut_h_et_al(
                        output_directory_path=output_directory_path
                    )

                if version == "v_20161014_wei_j_n_et_al":
                    MiscellaneousReactionDataSourceDownloadUtility.download_v_20161014_wei_j_n_et_al(
                        output_directory_path=output_directory_path
                    )

                if version == "v_20200508_grambow_c_et_al":
                    MiscellaneousReactionDataSourceDownloadUtility.download_v_20200508_grambow_c_et_al(
                        output_directory_path=output_directory_path
                    )

                if version == "v_add_on_by_20200508_grambow_c_et_al":
                    MiscellaneousReactionDataSourceDownloadUtility.download_v_add_on_by_20200508_grambow_c_et_al(
                        output_directory_path=output_directory_path
                    )

                if version == "v_golden_dataset_by_20211103_lin_a_et_al":
                    MiscellaneousReactionDataSourceDownloadUtility.download_v_golden_dataset_by_20211103_lin_a_et_al(
                        output_directory_path=output_directory_path
                    )

                if version == "v_rdb7_by_20220718_spiekermann_k_et_al":
                    MiscellaneousReactionDataSourceDownloadUtility.download_v_rdb7_by_20220718_spiekermann_k_et_al(
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
                        data_source="miscellaneous chemical reaction data source version '{version:s}'".format(
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
            if version in self.get_supported_versions().keys():
                if self.logger is not None:
                    self.logger.info(
                        msg="The extraction of the data from the {data_source:s} has been started.".format(
                            data_source="miscellaneous chemical reaction data source ({version:s})".format(
                                version=version
                            )
                        )
                    )

                if version == "v_20131008_kraut_h_et_al":
                    MiscellaneousReactionDataSourceExtractionUtility.extract_v_20131008_kraut_h_et_al(
                        input_directory_path=input_directory_path,
                        output_directory_path=output_directory_path
                    )

                if version == "v_golden_dataset_by_20211103_lin_a_et_al":
                    MiscellaneousReactionDataSourceExtractionUtility.extract_v_golden_dataset_by_20211103_lin_a_et_al(
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
                        data_source="miscellaneous chemical reaction data source version '{version:s}'".format(
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
            if version in self.get_supported_versions().keys():
                if self.logger is not None:
                    self.logger.info(
                        msg="The formatting of the data from the {data_source:s} has been started.".format(
                            data_source="miscellaneous chemical reaction data source ({version:s})".format(
                                version=version
                            )
                        )
                    )

                if version == "v_20131008_kraut_h_et_al":
                    MiscellaneousReactionDataSourceFormattingUtility.format_v_20131008_kraut_h_et_al(
                        input_directory_path=input_directory_path,
                        output_directory_path=output_directory_path
                    )

                if version == "v_20161014_wei_j_n_et_al":
                    MiscellaneousReactionDataSourceFormattingUtility.format_v_20161014_wei_j_n_et_al(
                        input_directory_path=input_directory_path,
                        output_directory_path=output_directory_path
                    )

                if version == "v_20200508_grambow_c_et_al":
                    MiscellaneousReactionDataSourceFormattingUtility.format_v_20200508_grambow_c_et_al(
                        input_directory_path=input_directory_path,
                        output_directory_path=output_directory_path
                    )

                if version == "v_add_on_by_20200508_grambow_c_et_al":
                    MiscellaneousReactionDataSourceFormattingUtility.format_v_add_on_by_20200508_grambow_c_et_al(
                        input_directory_path=input_directory_path,
                        output_directory_path=output_directory_path
                    )

                if version == "v_golden_dataset_by_20211103_lin_a_et_al":
                    MiscellaneousReactionDataSourceFormattingUtility.format_v_golden_dataset_by_20211103_lin_a_et_al(
                        input_directory_path=input_directory_path,
                        output_directory_path=output_directory_path
                    )

                if version == "v_rdb7_by_20220718_spiekermann_k_et_al":
                    MiscellaneousReactionDataSourceFormattingUtility.format_v_rdb7_by_20220718_spiekermann_k_et_al(
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
                        data_source="miscellaneous chemical reaction data source version '{version:s}'".format(
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
