""" The ``data_source.compound`` package ``chembl`` module. """

from datetime import datetime
from logging import Logger
from os import PathLike
from pathlib import Path
from re import search
from shutil import copyfileobj
from typing import Dict, Optional, Union

from gzip import open as open_gzip_archive_file

from pandas.io.parsers.readers import read_csv

from data_source.abstract_base.abstract_base import AbstractBaseDataSource


class ChEMBLCompoundDatabase(AbstractBaseDataSource):
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

    @property
    def available_versions(
            self
    ) -> Dict[str, str]:
        """
        Get the available versions of the chemical compound database.

        :returns: The available versions of the chemical compound database.
        """

        http_get_request_response = self._send_http_get_request(
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

    # ------------------------------------------------------------------------------------------------------------------
    #  Version(s): v_release_*
    # ------------------------------------------------------------------------------------------------------------------

    @staticmethod
    def _download_v_release(
            version: str,
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Download the data from a `v_release_*` version of the chemical compound database.

        :parameter version: The version of the chemical compound database.
        :parameter output_directory_path: The path to the output directory where the data should be downloaded.
        """

        AbstractBaseDataSource._download_file(
            file_url="https://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/{file_url_suffix:s}".format(
                file_url_suffix="chembl_{release_number:s}/chembl_{release_number:s}_chemreps.txt.gz".format(
                    release_number=version.split(
                        sep="_"
                    )[-1]
                )
            ),
            file_name="chembl_{release_number:s}_chemreps.txt.gz".format(
                release_number=version.split(
                    sep="_"
                )[-1]
            ),
            output_directory_path=output_directory_path
        )

    @staticmethod
    def _extract_v_release(
            version: str,
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Extract the data from a `v_release_*` version of the chemical compound database.

        :parameter version: The version of the chemical compound database.
        :parameter input_directory_path: The path to the input directory where the data is downloaded.
        :parameter output_directory_path: The path to the output directory where the data should be extracted.
        """

        with open_gzip_archive_file(
            filename=Path(
                input_directory_path,
                "chembl_{release_number:s}_chemreps.txt.gz".format(
                    release_number=version.split(
                        sep="_"
                    )[-1]
                )
            )
        ) as gzip_archive_file_handle:
            with open(
                file=Path(
                    output_directory_path,
                    "chembl_{release_number:s}_chemreps.txt".format(
                        release_number=version.split(
                            sep="_"
                        )[-1]
                    )
                ),
                mode="wb"
            ) as file_handle:
                copyfileobj(
                    fsrc=gzip_archive_file_handle,
                    fdst=file_handle
                )

    @staticmethod
    def _format_v_release(
            version: str,
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Format the data from a `v_release_*` version of the chemical compound database.

        :parameter version: The version of the chemical compound database.
        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        read_csv(
            filepath_or_buffer=Path(
                input_directory_path,
                "chembl_{release_number:s}_chemreps.txt".format(
                    release_number=version.split(
                        sep="_"
                    )[-1]
                )
            ),
            sep="\t",
            header=0
        ).to_csv(
            path_or_buf=Path(
                output_directory_path,
                "{timestamp:s}_chembl_{version:s}.csv".format(
                    timestamp=datetime.now().strftime(
                        format="%Y%m%d%H%M%S"
                    ),
                    version=version
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
        Download the data from the chemical compound database.

        :parameter version: The version of the chemical compound database.
        :parameter output_directory_path: The path to the output directory where the data should be downloaded.
        """

        try:
            if version in self.available_versions.keys():
                if self.logger is not None:
                    self.logger.info(
                        msg="The download of the data from the {data_source:s} has been started.".format(
                            data_source="ChEMBL chemical compound database ({version:s})".format(
                                version=version
                            )
                        )
                    )

                if version.startswith("v_release"):
                    self._download_v_release(
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
                        data_source="ChEMBL chemical compound database ({version:s})".format(
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
            if version in self.available_versions.keys():
                if self.logger is not None:
                    self.logger.info(
                        msg="The extraction of the data from the {data_source:s} has been started.".format(
                            data_source="ChEMBL chemical compound database ({version:s})".format(
                                version=version
                            )
                        )
                    )

                if version.startswith("v_release"):
                    self._extract_v_release(
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
                        data_source="ChEMBL chemical compound database ({version:s})".format(
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
            if version in self.available_versions.keys():
                if self.logger is not None:
                    self.logger.info(
                        msg="The formatting of the data from the {data_source:s} has been started.".format(
                            data_source="ChEMBL chemical compound database ({version:s})".format(
                                version=version
                            )
                        )
                    )

                if version.startswith("v_release"):
                    self._format_v_release(
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
                        data_source="ChEMBL chemical compound database ({version:s})".format(
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
