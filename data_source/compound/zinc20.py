""" The ``data_source.compound`` package ``zinc20`` module. """

from datetime import datetime
from logging import Logger
from os import PathLike
from pathlib import Path
from re import findall
from shutil import copyfileobj
from typing import Dict, Optional, Union

from gzip import open as open_gzip_archive_file

from pandas.io.parsers.readers import read_csv

from data_source.abstract_base.abstract_base import AbstractBaseDataSource


class ZINC20CompoundDatabase(AbstractBaseDataSource):
    """ The `ZINC20 <https://zinc20.docking.org>`_ chemical compound database class. """

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

        available_versions = dict()

        for file_name in findall(
            pattern=r"href=\"([^\.]+)\.smi\.gz",
            string=self._send_http_get_request(
                http_get_request_url="https://files.docking.org/bb/current"
            ).text
        ):
            available_versions[
                "v_building_blocks_{file_name:s}".format(
                    file_name=file_name
                )
            ] = "https://doi.org/10.1021/acs.jcim.0c00675"

        for file_name in findall(
            pattern=r"href=\"([^\.]+)\.src\.txt",
            string=self._send_http_get_request(
                http_get_request_url="https://files.docking.org/catalogs/source"
            ).text
        ):
            available_versions[
                "v_catalog_{file_name:s}".format(
                    file_name=file_name
                )
            ] = "https://doi.org/10.1021/acs.jcim.0c00675"

        return available_versions

    # ------------------------------------------------------------------------------------------------------------------
    #  Version(s): v_building_blocks_*
    # ------------------------------------------------------------------------------------------------------------------

    @staticmethod
    def _download_v_building_blocks(
            version: str,
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Download the data from a `v_building_blocks_*` version of the chemical compound database.

        :parameter version: The version of the chemical compound database.
        :parameter output_directory_path: The path to the output directory where the data should be downloaded.
        """

        AbstractBaseDataSource._download_file(
            file_url="https://files.docking.org/bb/current/{file_name:s}.smi.gz".format(
                file_name=version.split(
                    sep="_",
                    maxsplit=3
                )[-1]
            ),
            file_name="{file_name:s}.smi.gz".format(
                file_name=version.split(
                    sep="_",
                    maxsplit=3
                )[-1]
            ),
            output_directory_path=output_directory_path
        )

    @staticmethod
    def _extract_v_building_blocks(
            version: str,
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Extract the data from a `v_building_blocks_*` version of the chemical compound database.

        :parameter version: The version of the chemical compound database.
        :parameter input_directory_path: The path to the input directory where the data is downloaded.
        :parameter output_directory_path: The path to the output directory where the data should be extracted.
        """

        with open_gzip_archive_file(
            filename=Path(
                input_directory_path,
                "{file_name:s}.smi.gz".format(
                    file_name=version.split(
                        sep="_",
                        maxsplit=3
                    )[-1]
                )
            )
        ) as gz_archive_file_handle:
            with open(
                file=Path(
                    output_directory_path,
                    "{file_name:s}.smi".format(
                        file_name=version.split(
                            sep="_",
                            maxsplit=3
                        )[-1]
                    )
                ),
                mode="wb"
            ) as file_handle:
                copyfileobj(
                    fsrc=gz_archive_file_handle,
                    fdst=file_handle
                )

    @staticmethod
    def _format_v_building_blocks(
            version: str,
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Format the data from a `v_building_blocks_*` version of the chemical compound database.

        :parameter version: The version of the chemical compound database.
        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        read_csv(
            filepath_or_buffer=Path(
                input_directory_path,
                "{file_name:s}.smi".format(
                    file_name=version.split(
                        sep="_",
                        maxsplit=3
                    )[-1]
                )
            ),
            sep=r"\s+",
            header=None
        ).rename(
            columns={
                0: "smiles",
                1: "id",
            }
        ).to_csv(
            path_or_buf=Path(
                output_directory_path,
                "{timestamp:s}_zinc20_{version:s}.csv".format(
                    timestamp=datetime.now().strftime(
                        format="%Y%m%d%H%M%S"
                    ),
                    version=version.replace("-", "_")
                )
            ),
            index=False
        )

    # ------------------------------------------------------------------------------------------------------------------
    #  Version(s): v_catalog_*
    # ------------------------------------------------------------------------------------------------------------------

    @staticmethod
    def _download_v_catalog(
            version: str,
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Download the data from a `v_catalog_*` version of the chemical compound database.

        :parameter version: The version of the chemical compound database.
        :parameter output_directory_path: The path to the output directory where the data should be downloaded.
        """

        AbstractBaseDataSource._download_file(
            file_url="https://files.docking.org/catalogs/source/{file_name:s}.src.txt".format(
                file_name=version.split(
                    sep="_",
                    maxsplit=2
                )[-1]
            ),
            file_name="{file_name:s}.src.txt".format(
                file_name=version.split(
                    sep="_",
                    maxsplit=2
                )[-1]
            ),
            output_directory_path=output_directory_path
        )

    @staticmethod
    def _format_v_catalog(
            version: str,
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Format the data from a `v_catalog_*` version of the chemical compound database.

        :parameter version: The version of the chemical compound database.
        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        read_csv(
            filepath_or_buffer=Path(
                input_directory_path,
                "{file_name:s}.src.txt".format(
                    file_name=version.split(
                        sep="_",
                        maxsplit=2
                    )[-1]
                )
            ),
            sep=r"\s+",
            header=None
        ).rename(
            columns={
                0: "smiles",
                1: "id",
            }
        ).to_csv(
            path_or_buf=Path(
                output_directory_path,
                "{timestamp:s}_zinc20_{version:s}.csv".format(
                    timestamp=datetime.now().strftime(
                        format="%Y%m%d%H%M%S"
                    ),
                    version=version.replace("-", "_")
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
                            data_source="ZINC20 chemical compound database ({version:s})".format(
                                version=version
                            )
                        )
                    )

                if version.startswith("v_building_blocks"):
                    self._download_v_building_blocks(
                        version=version,
                        output_directory_path=output_directory_path
                    )

                if version.startswith("v_catalog"):
                    self._download_v_catalog(
                        version=version,
                        output_directory_path=output_directory_path
                    )

                if self.logger is not None:
                    self.logger.info(
                        msg="The download of the data from the {data_source:s} has been completed.".format(
                            data_source="ZINC20 chemical compound database ({version:s})".format(
                                version=version
                            )
                        )
                    )

            else:
                raise ValueError(
                    "The {data_source:s} is not supported.".format(
                        data_source="ZINC20 chemical compound database ({version:s})".format(
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
                            data_source="ZINC20 chemical compound database ({version:s})".format(
                                version=version
                            )
                        )
                    )

                if version.startswith("v_building_blocks"):
                    self._extract_v_building_blocks(
                        version=version,
                        input_directory_path=input_directory_path,
                        output_directory_path=output_directory_path
                    )

                if self.logger is not None:
                    self.logger.info(
                        msg="The extraction of the data from the {data_source:s} has been completed.".format(
                            data_source="ZINC20 chemical compound database ({version:s})".format(
                                version=version
                            )
                        )
                    )

            else:
                raise ValueError(
                    "The {data_source:s} is not supported.".format(
                        data_source="ZINC20 chemical compound database ({version:s})".format(
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
                            data_source="ZINC20 chemical compound database ({version:s})".format(
                                version=version
                            )
                        )
                    )

                if version.startswith("v_building_blocks"):
                    self._format_v_building_blocks(
                        version=version,
                        input_directory_path=input_directory_path,
                        output_directory_path=output_directory_path
                    )

                if version.startswith("v_catalog"):
                    self._format_v_catalog(
                        version=version,
                        input_directory_path=input_directory_path,
                        output_directory_path=output_directory_path
                    )

                if self.logger is not None:
                    self.logger.info(
                        msg="The formatting of the data from the {data_source:s} has been completed.".format(
                            data_source="ZINC20 chemical compound database ({version:s})".format(
                                version=version
                            )
                        )
                    )

            else:
                raise ValueError(
                    "The {data_source:s} is not supported.".format(
                        data_source="ZINC20 chemical compound database ({version:s})".format(
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
