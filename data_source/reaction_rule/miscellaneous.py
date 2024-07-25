""" The ``data_source.reaction_rule`` package ``miscellaneous`` module. """

from datetime import datetime
from logging import Logger
from os import PathLike
from pathlib import Path
from typing import Dict, Optional, Union

from pandas.io.parsers.readers import read_csv

from data_source.abstract_base.abstract_base import AbstractBaseDataSource


class MiscellaneousReactionRuleDataSource(AbstractBaseDataSource):
    """ The miscellaneous chemical reaction rule data source class. """

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
        Get the available versions of the chemical reaction rule data source.

        :returns: The available versions of the chemical reaction rule data source.
        """

        return {
            "v_20180421_avramova_s_et_al_1_0": "https://doi.org/10.5281/zenodo.1209313",
            "v_20190701_button_a_et_al": "https://doi.org/10.24433/CO.6930970.v1",
        }

    # ------------------------------------------------------------------------------------------------------------------
    #  Version: v_20180421_avramova_s_et_al_1_0
    # ------------------------------------------------------------------------------------------------------------------

    @staticmethod
    def _download_v_20180421_avramova_s_et_al_1_0(
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Download the data from the `v_20180421_avramova_s_et_al_1_0` version of the chemical reaction rule data source.

        :parameter output_directory_path: The path to the output directory where the data should be downloaded.
        """

        AbstractBaseDataSource._download_file(
            file_url="https://zenodo.org/records/1209313/files/RetroTransformDB-v-1-0.txt",
            file_name="RetroTransformDB-v-1-0.txt",
            output_directory_path=output_directory_path
        )

    @staticmethod
    def _format_v_20180421_avramova_s_et_al_1_0(
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Format the data from the `v_20180421_avramova_s_et_al_1_0` version of the chemical reaction rule data source.

        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        read_csv(
            filepath_or_buffer=Path(input_directory_path, "RetroTransformDB-v-1-0.txt"),
            sep="\t",
            header=0
        ).dropna(
            how="all"
        ).astype(
            dtype={
                "ID": int,
            }
        ).to_csv(
            path_or_buf=Path(
                output_directory_path,
                "{timestamp:s}_v_20180421_avramova_s_et_al_1_0.csv".format(
                    timestamp=datetime.now().strftime(
                        format="%Y%m%d%H%M%S"
                    )
                )
            ),
            index=False
        )

    # ------------------------------------------------------------------------------------------------------------------
    #  Version: v_20190701_button_a_et_al
    # ------------------------------------------------------------------------------------------------------------------

    @staticmethod
    def _download_v_20190701_button_a_et_al(
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Download the data from the `v_20190701_button_a_et_al` version of the chemical reaction rule data source.

        :parameter output_directory_path: The path to the output directory where the data should be downloaded.
        """

        AbstractBaseDataSource._download_file(
            file_url="https://raw.githubusercontent.com/neo-chem-synth-wave/data-source/{file_url_suffix:s}".format(
                file_url_suffix="main/data/reaction_rule/v_20190701_button_a_et_al/rxn_set.txt"
            ),
            file_name="rxn_set.txt",
            output_directory_path=output_directory_path
        )

    @staticmethod
    def _format_v_20190701_button_a_et_al(
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Format the data from the `v_20190701_button_a_et_al` version of the chemical reaction rule data source.

        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        read_csv(
            filepath_or_buffer=Path(input_directory_path, "rxn_set.txt"),
            sep="|",
            header=None
        ).rename(
            columns={
                0: "reaction_name",
                1: "reaction_smarts",
                2: "reaction_label",
            }
        ).to_csv(
            path_or_buf=Path(
                output_directory_path,
                "{timestamp:s}_v_20190701_button_a_et_al.csv".format(
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
        Download the data from the chemical reaction rule data source.

        :parameter version: The version of the chemical reaction rule data source.
        :parameter output_directory_path: The path to the output directory where the data should be downloaded.
        """

        try:
            if version in self.available_versions.keys():
                if self.logger is not None:
                    self.logger.info(
                        msg="The download of the data from the {data_source:s} has been started.".format(
                            data_source="miscellaneous chemical reaction rule data source ({version:s})".format(
                                version=version
                            )
                        )
                    )

                if version == "v_20180421_avramova_s_et_al_1_0":
                    self._download_v_20180421_avramova_s_et_al_1_0(
                        output_directory_path=output_directory_path
                    )

                if version == "v_20190701_button_a_et_al":
                    self._download_v_20190701_button_a_et_al(
                        output_directory_path=output_directory_path
                    )

                if self.logger is not None:
                    self.logger.info(
                        msg="The download of the data from the {data_source:s} has been completed.".format(
                            data_source="miscellaneous chemical reaction rule data source ({version:s})".format(
                                version=version
                            )
                        )
                    )

            else:
                raise ValueError(
                    "The {data_source:s} is not supported.".format(
                        data_source="miscellaneous chemical reaction rule data source ({version:s})".format(
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
        Extract the data from the chemical reaction rule data source.

        :parameter version: The version of the chemical reaction rule data source.
        :parameter input_directory_path: The path to the input directory where the data is downloaded.
        :parameter output_directory_path: The path to the output directory where the data should be extracted.
        """

        try:
            if version in self.available_versions.keys():
                if self.logger is not None:
                    self.logger.info(
                        msg="The extraction of the data from the {data_source:s} has been started.".format(
                            data_source="miscellaneous chemical reaction rule data source ({version:s})".format(
                                version=version
                            )
                        )
                    )

                if self.logger is not None:
                    self.logger.info(
                        msg="The extraction of the data from the {data_source:s} has been completed.".format(
                            data_source="miscellaneous chemical reaction rule data source ({version:s})".format(
                                version=version
                            )
                        )
                    )

            else:
                raise ValueError(
                    "The {data_source:s} is not supported.".format(
                        data_source="miscellaneous chemical reaction rule data source ({version:s})".format(
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
        Format the data from the chemical reaction rule data source.

        :parameter version: The version of the chemical reaction rule data source.
        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        try:
            if version in self.available_versions.keys():
                if self.logger is not None:
                    self.logger.info(
                        msg="The formatting of the data from the {data_source:s} has been started.".format(
                            data_source="miscellaneous chemical reaction rule data source ({version:s})".format(
                                version=version
                            )
                        )
                    )

                if version == "v_20180421_avramova_s_et_al_1_0":
                    self._format_v_20180421_avramova_s_et_al_1_0(
                        input_directory_path=input_directory_path,
                        output_directory_path=output_directory_path
                    )

                if version == "v_20190701_button_a_et_al":
                    self._format_v_20190701_button_a_et_al(
                        input_directory_path=input_directory_path,
                        output_directory_path=output_directory_path
                    )

                if self.logger is not None:
                    self.logger.info(
                        msg="The formatting of the data from the {data_source:s} has been completed.".format(
                            data_source="miscellaneous chemical reaction rule data source ({version:s})".format(
                                version=version
                            )
                        )
                    )

            else:
                raise ValueError(
                    "The {data_source:s} is not supported.".format(
                        data_source="miscellaneous chemical reaction rule data source ({version:s})".format(
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
