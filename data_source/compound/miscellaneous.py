""" The ``data_source.compound`` package ``miscellaneous`` module. """

from datetime import datetime
from logging import Logger
from os import PathLike
from pathlib import Path
from typing import Dict, Optional, Union

from pandas.io.parsers.readers import read_csv

from data_source.abstract_base.abstract_base import AbstractBaseDataSource


class MiscellaneousCompoundDataSource(AbstractBaseDataSource):
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

    @property
    def available_versions(
            self
    ) -> Dict[str, str]:
        """
        Get the available versions of the chemical compound data source.

        :returns: The available versions of the chemical compound data source.
        """

        return {
            "v_20201218_polykovskiy_d_et_al": "https://doi.org/10.3389/fphar.2020.565644",
        }

    def _download_v_20201218_polykovskiy_d_et_al(
            self,
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Download the data from the `v_20201218_polykovskiy_d_et_al` version of the chemical compound data source.

        :parameter output_directory_path: The path to the output directory where the data should be downloaded.
        """

        self._download_file(
            file_url="https://media.githubusercontent.com/media/molecularsets/moses/master/data/dataset_v1.csv",
            file_name="dataset_v1.csv",
            output_directory_path=output_directory_path
        )

    def download(
            self,
            version: str,
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Download the data from the chemical compound data source.

        :parameter version: The version of the chemical compound data source.
        :parameter output_directory_path: The path to the output directory where the data should be downloaded.
        """

        try:
            if version in self.available_versions.keys():
                if self.logger is not None:
                    self.logger.info(
                        msg="The download of the data from the {data_source:s} has been started.".format(
                            data_source="miscellaneous chemical compound data source ({version:s})".format(
                                version=version
                            )
                        )
                    )

                if version == "v_20201218_polykovskiy_d_et_al":
                    self._download_v_20201218_polykovskiy_d_et_al(
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
                        data_source="miscellaneous chemical compound data source ({version:s})".format(
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
        Extract the data from the chemical compound data source.

        :parameter version: The version of the chemical compound data source.
        :parameter input_directory_path: The path to the input directory where the data is downloaded.
        :parameter output_directory_path: The path to the output directory where the data should be extracted.
        """

        try:
            if version in self.available_versions.keys():
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
                        data_source="miscellaneous chemical compound data source ({version:s})".format(
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

    @staticmethod
    def _format_v_20201218_polykovskiy_d_et_al(
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Format the data from the `v_20201218_polykovskiy_d_et_al` version of the chemical compound data source.

        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        read_csv(
            filepath_or_buffer=Path(input_directory_path, "dataset_v1.csv"),
            header=0
        ).to_csv(
            path_or_buf=Path(
                output_directory_path,
                "{timestamp:s}_miscellaneous_v_20201218_polykovskiy_d_et_al.csv".format(
                    timestamp=datetime.now().strftime(
                        format="%Y%m%d%H%M%S"
                    )
                )
            ),
            index=False
        )

    def format(
            self,
            version: str,
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Format the data from the chemical compound data source.

        :parameter version: The version of the chemical compound data source.
        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        try:
            if version in self.available_versions.keys():
                if self.logger is not None:
                    self.logger.info(
                        msg="The formatting of the data from the {data_source:s} has been started.".format(
                            data_source="miscellaneous chemical compound data source ({version:s})".format(
                                version=version
                            )
                        )
                    )

                if version == "v_20201218_polykovskiy_d_et_al":
                    self._format_v_20201218_polykovskiy_d_et_al(
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
                        data_source="miscellaneous chemical compound data source ({version:s})".format(
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
