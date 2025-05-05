""" The ``data_source.reaction_pattern.retro_rules`` package ``retro_rules`` module. """

from os import PathLike
from typing import Dict, Union

from data_source.base.base import DataSourceBase
from data_source.reaction_pattern.retro_rules.utility.download import RetroRulesReactionPatternDatabaseDownloadUtility

from data_source.reaction_pattern.retro_rules.utility.extraction import (
    RetroRulesReactionPatternDatabaseExtractionUtility
)

from data_source.reaction_pattern.retro_rules.utility.formatting import (
    RetroRulesReactionPatternDatabaseFormattingUtility
)


class RetroRulesReactionPatternDatabase(DataSourceBase):
    """ The `RetroRules <https://retrorules.org>`_ chemical reaction pattern database class. """

    @staticmethod
    def get_supported_versions() -> Dict[str, str]:
        """
        Get the supported versions of the database.

        :returns: The supported versions of the database.
        """

        return {
            "v_release_rr01_rp2_hs": "https://doi.org/10.5281/zenodo.5827427",
            "v_release_rr02_rp2_hs": "https://doi.org/10.5281/zenodo.5828017",
            "v_release_rr02_rp3_hs": "https://doi.org/10.5281/zenodo.5827977",
            "v_release_rr02_rp3_nohs": "https://doi.org/10.5281/zenodo.5827969",
        }

    def download_(
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
                            data_source="RetroRules chemical reaction pattern database ({version:s})".format(
                                version=version
                            )
                        )
                    )

                if version.startswith("v_release"):
                    RetroRulesReactionPatternDatabaseDownloadUtility.download_v_release(
                        version=version,
                        output_directory_path=output_directory_path
                    )

                if self.logger is not None:
                    self.logger.info(
                        msg="The download of the data from the {data_source:s} has been completed.".format(
                            data_source="RetroRules chemical reaction pattern database ({version:s})".format(
                                version=version
                            )
                        )
                    )

            else:
                raise ValueError(
                    "The download of the data from the {data_source:s} is not supported.".format(
                        data_source="RetroRules chemical reaction pattern database ({version:s})".format(
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

    def extract_(
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
                            data_source="RetroRules chemical reaction pattern database ({version:s})".format(
                                version=version
                            )
                        )
                    )

                if version.startswith("v_release"):
                    RetroRulesReactionPatternDatabaseExtractionUtility.extract_v_release(
                        version=version,
                        input_directory_path=input_directory_path,
                        output_directory_path=output_directory_path
                    )

                if self.logger is not None:
                    self.logger.info(
                        msg="The extraction of the data from the {data_source:s} has been completed.".format(
                            data_source="RetroRules chemical reaction pattern database ({version:s})".format(
                                version=version
                            )
                        )
                    )

            else:
                raise ValueError(
                    "The extraction of the data from the {data_source:s} is not supported.".format(
                        data_source="RetroRules chemical reaction pattern database ({version:s})".format(
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

    def format_(
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
                            data_source="RetroRules chemical reaction pattern database ({version:s})".format(
                                version=version
                            )
                        )
                    )

                if version.startswith("v_release"):
                    RetroRulesReactionPatternDatabaseFormattingUtility.format_v_release(
                        version=version,
                        input_directory_path=input_directory_path,
                        output_directory_path=output_directory_path
                    )

                if self.logger is not None:
                    self.logger.info(
                        msg="The formatting of the data from the {data_source:s} has been completed.".format(
                            data_source="RetroRules chemical reaction pattern database ({version:s})".format(
                                version=version
                            )
                        )
                    )

            else:
                raise ValueError(
                    "The formatting of the data from the {data_source:s} is not supported.".format(
                        data_source="RetroRules chemical reaction pattern database ({version:s})".format(
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
