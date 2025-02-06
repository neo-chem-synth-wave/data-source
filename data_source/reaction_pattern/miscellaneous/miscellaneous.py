""" The ``data_source.reaction_pattern.miscellaneous`` package ``miscellaneous`` module. """

from os import PathLike
from typing import Dict, Union

from data_source.base.base import DataSourceBase

from data_source.reaction_pattern.miscellaneous.utility import *


class MiscellaneousReactionPatternDataSource(DataSourceBase):
    """ The miscellaneous chemical reaction pattern data source class. """

    @staticmethod
    def get_supported_versions() -> Dict[str, str]:
        """
        Get the supported versions of the data source.

        :returns: The supported versions of the data source.
        """

        return {
            "v_retro_transform_db_by_20180421_avramova_s_et_al": "https://zenodo.org/doi/10.5281/zenodo.1209312",
            "v_dingos_by_20190701_button_a_et_al": "https://doi.org/10.24433/CO.6930970.v1",
        }

    def download(
            self,
            version: str,
            output_directory_path: Union[str, PathLike[str]],
            **kwargs
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
                            data_source="miscellaneous chemical reaction pattern data source ({version:s})".format(
                                version=version
                            )
                        )
                    )

                if version == "v_retro_transform_db_by_20180421_avramova_s_et_al":
                    MiscellaneousReactionPatternDataSourceDownloadUtility.download_v_retro_transform_db_by_20180421_avramova_s_et_al(
                        output_directory_path=output_directory_path
                    )

                if version == "v_dingos_by_20190701_button_a_et_al":
                    MiscellaneousReactionPatternDataSourceDownloadUtility.download_v_dingos_by_20190701_button_a_et_al(
                        output_directory_path=output_directory_path
                    )

                if self.logger is not None:
                    self.logger.info(
                        msg="The download of the data from the {data_source:s} has been completed.".format(
                            data_source="miscellaneous chemical reaction pattern data source ({version:s})".format(
                                version=version
                            )
                        )
                    )

            else:
                raise ValueError(
                    "The download of the data from the {data_source:s} is not supported.".format(
                        data_source="miscellaneous chemical reaction pattern data source ({version:s})".format(
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
            output_directory_path: Union[str, PathLike[str]],
            **kwargs
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
                            data_source="miscellaneous chemical reaction pattern data source ({version:s})".format(
                                version=version
                            )
                        )
                    )

                if self.logger is not None:
                    self.logger.info(
                        msg="The extraction of the data from the {data_source:s} has been completed.".format(
                            data_source="miscellaneous chemical reaction pattern data source ({version:s})".format(
                                version=version
                            )
                        )
                    )

            else:
                raise ValueError(
                    "The extraction of the data from the {data_source:s} is not supported.".format(
                        data_source="miscellaneous chemical reaction pattern data source ({version:s})".format(
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
                            data_source="miscellaneous chemical reaction pattern data source ({version:s})".format(
                                version=version
                            )
                        )
                    )

                if version == "v_retro_transform_db_by_20180421_avramova_s_et_al":
                    MiscellaneousReactionPatternDataSourceFormattingUtility.format_v_retro_transform_db_by_20180421_avramova_s_et_al(
                        input_directory_path=input_directory_path,
                        output_directory_path=output_directory_path
                    )

                if version == "v_dingos_by_20190701_button_a_et_al":
                    MiscellaneousReactionPatternDataSourceFormattingUtility.format_v_dingos_by_20190701_button_a_et_al(
                        input_directory_path=input_directory_path,
                        output_directory_path=output_directory_path
                    )

                if self.logger is not None:
                    self.logger.info(
                        msg="The formatting of the data from the {data_source:s} has been completed.".format(
                            data_source="miscellaneous chemical reaction pattern data source ({version:s})".format(
                                version=version
                            )
                        )
                    )

            else:
                raise ValueError(
                    "The formatting of the data from the {data_source:s} is not supported.".format(
                        data_source="miscellaneous chemical reaction pattern data source ({version:s})".format(
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
