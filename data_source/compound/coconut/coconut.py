""" The ``data_source.compound.coconut`` package ``coconut`` module. """

from os import PathLike
from typing import Dict, Union

from data_source.base.base import DataSourceBase
from data_source.compound.coconut.utility.download import COCONUTCompoundDatabaseDownloadUtility
from data_source.compound.coconut.utility.extraction import COCONUTCompoundDatabaseExtractionUtility
from data_source.compound.coconut.utility.formatting import COCONUTCompoundDatabaseFormattingUtility


class COCONUTCompoundDatabase(DataSourceBase):
    """ The `COCONUT <https://coconut.naturalproducts.net>`_ chemical compound database class. """

    @staticmethod
    def get_supported_versions() -> Dict[str, str]:
        """
        Get the supported versions of the database.

        :returns: The supported versions of the database.
        """

        return {
            "v_2_0_by_20241126_chandrasekhar_v_et_al": "https://doi.org/10.5281/zenodo.13382750",
            "v_2_0_complete_by_20241126_chandrasekhar_v_et_al": "https://doi.org/10.5281/zenodo.13382750",
        }

    def download(
            self,
            version: str,
            output_directory_path: Union[str, PathLike[str]],
            **kwargs
    ) -> None:
        """
        Download the data from the database.

        :parameter version: The version of the database.
        :parameter output_directory_path: The path to the output directory where the data should be downloaded.
        """

        try:
            if version in self.get_supported_versions().keys():
                if self.logger is not None:
                    self.logger.info(
                        msg="The download of the data from the {data_source:s} has been started.".format(
                            data_source="COCONUT chemical compound database ({version:s})".format(
                                version=version
                            )
                        )
                    )

                if version in [
                    "v_2_0_by_20241126_chandrasekhar_v_et_al",
                    "v_2_0_complete_by_20241126_chandrasekhar_v_et_al",
                ]:
                    COCONUTCompoundDatabaseDownloadUtility.download_v_2_0_by_20241126_chandrasekhar_v_et_al(
                        version=version,
                        output_directory_path=output_directory_path
                    )

                if self.logger is not None:
                    self.logger.info(
                        msg="The download of the data from the {data_source:s} has been completed.".format(
                            data_source="COCONUT chemical compound database ({version:s})".format(
                                version=version
                            )
                        )
                    )

            else:
                raise ValueError(
                    "The download of the data from the {data_source:s} is not supported.".format(
                        data_source="COCONUT chemical compound database ({version:s})".format(
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
        Extract the data from the database.

        :parameter version: The version of the database.
        :parameter input_directory_path: The path to the input directory where the data is downloaded.
        :parameter output_directory_path: The path to the output directory where the data should be extracted.
        """

        try:
            if version in self.get_supported_versions().keys():
                if self.logger is not None:
                    self.logger.info(
                        msg="The extraction of the data from the {data_source:s} has been started.".format(
                            data_source="COCONUT chemical compound database ({version:s})".format(
                                version=version
                            )
                        )
                    )

                if version in [
                    "v_2_0_by_20241126_chandrasekhar_v_et_al",
                    "v_2_0_complete_by_20241126_chandrasekhar_v_et_al",
                ]:
                    COCONUTCompoundDatabaseExtractionUtility.extract_v_2_0_by_20241126_chandrasekhar_v_et_al(
                        version=version,
                        input_directory_path=input_directory_path,
                        output_directory_path=output_directory_path
                    )

                if self.logger is not None:
                    self.logger.info(
                        msg="The extraction of the data from the {data_source:s} has been completed.".format(
                            data_source="COCONUT chemical compound database ({version:s})".format(
                                version=version
                            )
                        )
                    )

            else:
                raise ValueError(
                    "The extraction of the data from the {data_source:s} is not supported.".format(
                        data_source="COCONUT chemical compound database ({version:s})".format(
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
        Format the data from the database.

        :parameter version: The version of the database.
        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        try:
            if version in self.get_supported_versions().keys():
                if self.logger is not None:
                    self.logger.info(
                        msg="The formatting of the data from the {data_source:s} has been started.".format(
                            data_source="COCONUT chemical compound database ({version:s})".format(
                                version=version
                            )
                        )
                    )

                if version in [
                    "v_2_0_by_20241126_chandrasekhar_v_et_al",
                    "v_2_0_complete_by_20241126_chandrasekhar_v_et_al",
                ]:
                    COCONUTCompoundDatabaseFormattingUtility.format_v_2_0_by_20241126_chandrasekhar_v_et_al(
                        version=version,
                        input_directory_path=input_directory_path,
                        output_directory_path=output_directory_path
                    )

                if self.logger is not None:
                    self.logger.info(
                        msg="The formatting of the data from the {data_source:s} has been completed.".format(
                            data_source="COCONUT chemical compound database ({version:s})".format(
                                version=version
                            )
                        )
                    )

            else:
                raise ValueError(
                    "The formatting of the data from the {data_source:s} is not supported.".format(
                        data_source="COCONUT chemical compound database ({version:s})".format(
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
