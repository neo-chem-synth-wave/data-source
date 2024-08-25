""" The ``data_source.compound.chembl`` package ``chembl`` module. """

from logging import Logger
from os import PathLike
from re import search
from typing import Dict, Optional, Union

from data_source.base.base import BaseDataSource
from data_source.base.utility.download import BaseDataSourceDownloadUtility

from data_source.compound.chembl.utility.download import ChEMBLCompoundDatabaseDownloadUtility
from data_source.compound.chembl.utility.extraction import ChEMBLCompoundDatabaseExtractionUtility
from data_source.compound.chembl.utility.formatting import ChEMBLCompoundDatabaseFormattingUtility


class ChEMBLCompoundDatabase(BaseDataSource):
    """ The `ChEMBL <https://www.ebi.ac.uk/chembl>`_ chemical compound database class. """

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
        Get the supported versions of the chemical compound database.

        :returns: The supported versions of the chemical compound database.
        """

        try:
            http_get_request_response = BaseDataSourceDownloadUtility.send_http_get_request(
                http_get_request_url="https://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/latest/README"
            )

            latest_release_number = int(
                search(
                    pattern=r"Release:\s*chembl_(\d+)",
                    string=str(http_get_request_response.content)
                ).group(1)
            )

            return {
                "v_release_{release_number:d}".format(
                    release_number=release_number
                ): "https://doi.org/10.6019/CHEMBL.database.{release_number:d}".format(
                    release_number=release_number
                ) for release_number in range(25, latest_release_number + 1)
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
        Download the data from the chemical compound database.

        :parameter version: The version of the chemical compound database.
        :parameter output_directory_path: The path to the output directory where the data should be downloaded.
        """

        try:
            if version in self.get_supported_versions().keys():
                if self.logger is not None:
                    self.logger.info(
                        msg="The download of the data from the {data_source:s} has been started.".format(
                            data_source="ChEMBL chemical compound database ({version:s})".format(
                                version=version
                            )
                        )
                    )

                if version.startswith("v_release"):
                    ChEMBLCompoundDatabaseDownloadUtility.download_v_release(
                        version=version,
                        output_directory_path=output_directory_path
                    )

                if self.logger is not None:
                    self.logger.info(
                        msg="The download of the data from the {data_source:s} has been completed.".format(
                            data_source="ChEMBL chemical compound database ({version:s})".format(
                                version=version
                            )
                        )
                    )

            else:
                raise ValueError(
                    "The {data_source:s} is not supported.".format(
                        data_source="ChEMBL chemical compound database version '{version:s}'".format(
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
        Extract the data from the chemical compound database.

        :parameter version: The version of the chemical compound database.
        :parameter input_directory_path: The path to the input directory where the data is downloaded.
        :parameter output_directory_path: The path to the output directory where the data should be extracted.
        """

        try:
            if version in self.get_supported_versions().keys():
                if self.logger is not None:
                    self.logger.info(
                        msg="The extraction of the data from the {data_source:s} has been started.".format(
                            data_source="ChEMBL chemical compound database ({version:s})".format(
                                version=version
                            )
                        )
                    )

                if version.startswith("v_release"):
                    ChEMBLCompoundDatabaseExtractionUtility.extract_v_release(
                        version=version,
                        input_directory_path=input_directory_path,
                        output_directory_path=output_directory_path
                    )

                if self.logger is not None:
                    self.logger.info(
                        msg="The extraction of the data from the {data_source:s} has been completed.".format(
                            data_source="ChEMBL chemical compound database ({version:s})".format(
                                version=version
                            )
                        )
                    )

            else:
                raise ValueError(
                    "The {data_source:s} is not supported.".format(
                        data_source="ChEMBL chemical compound database version '{version:s}'".format(
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
        Format the data from the chemical compound database.

        :parameter version: The version of the chemical compound database.
        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        try:
            if version in self.get_supported_versions().keys():
                if self.logger is not None:
                    self.logger.info(
                        msg="The formatting of the data from the {data_source:s} has been started.".format(
                            data_source="ChEMBL chemical compound database ({version:s})".format(
                                version=version
                            )
                        )
                    )

                if version.startswith("v_release"):
                    ChEMBLCompoundDatabaseFormattingUtility.format_v_release(
                        version=version,
                        input_directory_path=input_directory_path,
                        output_directory_path=output_directory_path
                    )

                if self.logger is not None:
                    self.logger.info(
                        msg="The formatting of the data from the {data_source:s} has been completed.".format(
                            data_source="ChEMBL chemical compound database ({version:s})".format(
                                version=version
                            )
                        )
                    )

            else:
                raise ValueError(
                    "The {data_source:s} is not supported.".format(
                        data_source="ChEMBL chemical compound database version '{version:s}'".format(
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
