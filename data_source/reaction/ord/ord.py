""" The ``data_source.reaction.ord`` package ``ord`` module. """

from logging import Logger
from os import PathLike
from typing import Dict, Optional, Union

from data_source.base.base import BaseDataSource

from data_source.reaction.ord.utility.download import OpenReactionDatabaseDownloadUtility
from data_source.reaction.ord.utility.extraction import OpenReactionDatabaseExtractionUtility
from data_source.reaction.ord.utility.formatting import OpenReactionDatabaseFormattingUtility


class OpenReactionDatabase(BaseDataSource):
    """ The `Open Reaction Database (ORD) <https://open-reaction-database.org>`_ class. """

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
        Get the supported versions of the chemical reaction database.

        :returns: The supported versions of the chemical reaction database.
        """

        try:
            return {
                "v_release_0_1_0": "https://doi.org/10.1021/jacs.1c09820",
                "v_release_main": "https://doi.org/10.1021/jacs.1c09820",
                "v_orderly_condition_by_20240422_wigh_d_s_et_al": "https://doi.org/10.6084/m9.figshare.23298467.v4",
                "v_orderly_forward_by_20240422_wigh_d_s_et_al": "https://doi.org/10.6084/m9.figshare.23298467.v4",
                "v_orderly_retro_by_20240422_wigh_d_s_et_al": "https://doi.org/10.6084/m9.figshare.23298467.v4",
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
        Download the data from the chemical reaction database.

        :parameter version: The version of the chemical reaction database.
        :parameter output_directory_path: The path to the output directory where the data should be downloaded.
        """

        try:
            if version in self.get_supported_versions().keys():
                if self.logger is not None:
                    self.logger.info(
                        msg="The download of the data from the {data_source:s} has been started.".format(
                            data_source="Open Reaction Database ({version:s})".format(
                                version=version
                            )
                        )
                    )

                if version.startswith("v_release"):
                    OpenReactionDatabaseDownloadUtility.download_v_release(
                        version=version,
                        output_directory_path=output_directory_path
                    )

                if version.startswith("v_orderly"):
                    OpenReactionDatabaseDownloadUtility.download_v_orderly(
                        version=version,
                        output_directory_path=output_directory_path
                    )

                if self.logger is not None:
                    self.logger.info(
                        msg="The download of the data from the {data_source:s} has been completed.".format(
                            data_source="Open Reaction Database ({version:s})".format(
                                version=version
                            )
                        )
                    )

            else:
                raise ValueError(
                    "The {data_source:s} is not supported.".format(
                        data_source="Open Reaction Database version '{version:s}'".format(
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
        Extract the data from the chemical reaction database.

        :parameter version: The version of the chemical reaction database.
        :parameter input_directory_path: The path to the input directory where the data is downloaded.
        :parameter output_directory_path: The path to the output directory where the data should be extracted.
        """

        try:
            if version in self.get_supported_versions().keys():
                if self.logger is not None:
                    self.logger.info(
                        msg="The extraction of the data from the {data_source:s} has been started.".format(
                            data_source="Open Reaction Database ({version:s})".format(
                                version=version
                            )
                        )
                    )

                if version.startswith("v_release"):
                    OpenReactionDatabaseExtractionUtility.extract_v_release(
                        version=version,
                        input_directory_path=input_directory_path,
                        output_directory_path=output_directory_path
                    )

                if self.logger is not None:
                    self.logger.info(
                        msg="The extraction of the data from the {data_source:s} has been completed.".format(
                            data_source="Open Reaction Database ({version:s})".format(
                                version=version
                            )
                        )
                    )

            else:
                raise ValueError(
                    "The {data_source:s} is not supported.".format(
                        data_source="Open Reaction Database version '{version:s}'".format(
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
            output_directory_path: Union[str, PathLike[str]],
            **kwargs
    ) -> None:
        """
        Format the data from the chemical reaction database.

        :parameter version: The version of the chemical reaction database.
        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        :parameter kwargs: The keyword arguments.
        """

        try:
            if version in self.get_supported_versions().keys():
                if self.logger is not None:
                    self.logger.info(
                        msg="The formatting of the data from the {data_source:s} has been started.".format(
                            data_source="Open Reaction Database ({version:s})".format(
                                version=version
                            )
                        )
                    )

                if version.startswith("v_release"):
                    OpenReactionDatabaseFormattingUtility.format_v_release(
                        version=version,
                        input_directory_path=input_directory_path,
                        output_directory_path=output_directory_path,
                        **kwargs
                    )

                if version.startswith("v_orderly"):
                    OpenReactionDatabaseFormattingUtility.format_v_orderly(
                        version=version,
                        input_directory_path=input_directory_path,
                        output_directory_path=output_directory_path
                    )

                if self.logger is not None:
                    self.logger.info(
                        msg="The formatting of the data from the {data_source:s} has been completed.".format(
                            data_source="Open Reaction Database ({version:s})".format(
                                version=version
                            )
                        )
                    )

            else:
                raise ValueError(
                    "The {data_source:s} is not supported.".format(
                        data_source="Open Reaction Database version '{version:s}'".format(
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
