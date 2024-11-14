""" The ``data_source.compound.miscellaneous`` package ``miscellaneous`` module. """

from logging import Logger
from os import PathLike
from typing import Dict, Optional, Union

from data_source.base.base import BaseDataSource

from data_source.compound.miscellaneous.utility.download import MiscellaneousCompoundDataSourceDownloadUtility
from data_source.compound.miscellaneous.utility.formatting import MiscellaneousCompoundDataSourceFormattingUtility


class MiscellaneousCompoundDataSource(BaseDataSource):
    """ The miscellaneous chemical compound data source class. """

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

    @staticmethod
    def get_supported_versions() -> Dict[str, str]:
        """
        Get the supported versions of the data source.

        :returns: The supported versions of the data source.
        """

        return {
            "v_moses_by_20201218_polykovskiy_d_et_al": "https://doi.org/10.3389/fphar.2020.565644",
        }

    def download(
            self,
            version: str,
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Download the data from the data source.

        :parameter version: The version of the data source.
        :parameter output_directory_path: The path to the output directory where the data should be downloaded.
        """

        try:
            if version in self.get_supported_versions().keys():
                if self.logger is not None:
                    self.logger.info(
                        msg="The download of the data from the {data_source:s} has been started.".format(
                            data_source="miscellaneous chemical compound data source ({version:s})".format(
                                version=version
                            )
                        )
                    )

                if version == "v_moses_by_20201218_polykovskiy_d_et_al":
                    MiscellaneousCompoundDataSourceDownloadUtility.download_v_moses_by_20201218_polykovskiy_d_et_al(
                        output_directory_path=output_directory_path
                    )

                if self.logger is not None:
                    self.logger.info(
                        msg="The download of the data from the {data_source:s} has been completed.".format(
                            data_source="miscellaneous chemical compound data source ({version:s})".format(
                                version=version
                            )
                        )
                    )

            else:
                raise ValueError(
                    "The {data_source:s} is not supported.".format(
                        data_source="miscellaneous chemical compound data source version '{version:s}'".format(
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
        Extract the data from the data source.

        :parameter version: The version of the data source.
        :parameter input_directory_path: The path to the input directory where the data is downloaded.
        :parameter output_directory_path: The path to the output directory where the data should be extracted.
        """

        try:
            if version in self.get_supported_versions().keys():
                if self.logger is not None:
                    self.logger.info(
                        msg="The extraction of the data from the {data_source:s} has been started.".format(
                            data_source="miscellaneous chemical compound data source ({version:s})".format(
                                version=version
                            )
                        )
                    )

                if self.logger is not None:
                    self.logger.info(
                        msg="The extraction of the data from the {data_source:s} has been completed.".format(
                            data_source="miscellaneous chemical compound data source ({version:s})".format(
                                version=version
                            )
                        )
                    )

            else:
                raise ValueError(
                    "The {data_source:s} is not supported.".format(
                        data_source="miscellaneous chemical compound data source version '{version:s}'".format(
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
        Format the data from the data source.

        :parameter version: The version of the data source.
        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        try:
            if version in self.get_supported_versions().keys():
                if self.logger is not None:
                    self.logger.info(
                        msg="The formatting of the data from the {data_source:s} has been started.".format(
                            data_source="miscellaneous chemical compound data source ({version:s})".format(
                                version=version
                            )
                        )
                    )

                if version == "v_moses_by_20201218_polykovskiy_d_et_al":
                    MiscellaneousCompoundDataSourceFormattingUtility.format_v_moses_by_20201218_polykovskiy_d_et_al(
                        input_directory_path=input_directory_path,
                        output_directory_path=output_directory_path
                    )

                if self.logger is not None:
                    self.logger.info(
                        msg="The formatting of the data from the {data_source:s} has been completed.".format(
                            data_source="miscellaneous chemical compound data source ({version:s})".format(
                                version=version
                            )
                        )
                    )

            else:
                raise ValueError(
                    "The {data_source:s} is not supported.".format(
                        data_source="miscellaneous chemical compound data source version '{version:s}'".format(
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
