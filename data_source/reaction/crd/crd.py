""" The ``data_source.reaction.crd`` package ``crd`` module. """

from os import PathLike
from typing import Dict, Union

from data_source.base.base import DataSourceBase

from data_source.reaction.crd.utility import *


class ChemicalReactionDatabase(DataSourceBase):
    """ The `Chemical Reaction Database (CRD) <https://kmt.vander-lingen.nl>`_ class. """

    @staticmethod
    def get_supported_versions() -> Dict[str, str]:
        """
        Get the supported versions of the database.

        :returns: The supported versions of the database.
        """

        return {
            "v_reaction_smiles_2001_to_2021": "https://doi.org/10.6084/m9.figshare.20279733.v1",
            "v_reaction_smiles_2001_to_2023": "https://doi.org/10.6084/m9.figshare.22491730.v1",
            "v_reaction_smiles_2023": "https://doi.org/10.6084/m9.figshare.24921555.v1",
            "v_reaction_smiles_1976_to_2024": "https://doi.org/10.6084/m9.figshare.28230053.v1",
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
                            data_source="Chemical Reaction Database ({version:s})".format(
                                version=version
                            )
                        )
                    )

                if version in [
                    "v_reaction_smiles_2001_to_2021",
                    "v_reaction_smiles_2001_to_2023",
                    "v_reaction_smiles_2023",
                    "v_reaction_smiles_1976_to_2024",
                ]:
                    ChemicalReactionDatabaseDownloadUtility.download_v_reaction_smiles(
                        version=version,
                        output_directory_path=output_directory_path
                    )

                if self.logger is not None:
                    self.logger.info(
                        msg="The download of the data from the {data_source:s} has been completed.".format(
                            data_source="Chemical Reaction Database ({version:s})".format(
                                version=version
                            )
                        )
                    )

            else:
                raise ValueError(
                    "The download of the data from the {data_source:s} is not supported.".format(
                        data_source="Chemical Reaction Database ({version:s})".format(
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
                            data_source="Chemical Reaction Database ({version:s})".format(
                                version=version
                            )
                        )
                    )

                if version == "v_reaction_smiles_1976_to_2024":
                    ChemicalReactionDatabaseExtractionUtility.extract_v_reaction_smiles(
                        version=version,
                        input_directory_path=input_directory_path,
                        output_directory_path=output_directory_path
                    )

                if self.logger is not None:
                    self.logger.info(
                        msg="The extraction of the data from the {data_source:s} has been completed.".format(
                            data_source="Chemical Reaction Database ({version:s})".format(
                                version=version
                            )
                        )
                    )

            else:
                raise ValueError(
                    "The extraction of the data from the {data_source:s} is not supported.".format(
                        data_source="Chemical Reaction Database ({version:s})".format(
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
                            data_source="Chemical Reaction Database ({version:s})".format(
                                version=version
                            )
                        )
                    )

                if version in [
                    "v_reaction_smiles_2001_to_2021",
                    "v_reaction_smiles_2001_to_2023",
                    "v_reaction_smiles_2023",
                    "v_reaction_smiles_1976_to_2024",
                ]:
                    ChemicalReactionDatabaseFormattingUtility.format_v_reaction_smiles(
                        version=version,
                        input_directory_path=input_directory_path,
                        output_directory_path=output_directory_path
                    )

                if self.logger is not None:
                    self.logger.info(
                        msg="The formatting of the data from the {data_source:s} has been completed.".format(
                            data_source="Chemical Reaction Database ({version:s})".format(
                                version=version
                            )
                        )
                    )

            else:
                raise ValueError(
                    "The formatting of the data from the {data_source:s} is not supported.".format(
                        data_source="Chemical Reaction Database ({version:s})".format(
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
