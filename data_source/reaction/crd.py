""" The ``data_source.reaction`` package ``crd`` module. """

from datetime import datetime
from logging import Logger
from os import PathLike
from pathlib import Path
from typing import Dict, Optional, Union

from pandas.io.parsers.readers import read_csv

from data_source.abstract_base.abstract_base import AbstractBaseDataSource


class ChemicalReactionDatabase(AbstractBaseDataSource):
    """ The `Chemical Reaction Database (CRD) <https://kmt.vander-lingen.nl>`_ class. """

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
        Get the available versions of the chemical reaction database.

        :returns: The available versions of the chemical reaction database.
        """

        return {
            "v_reaction_smiles_2001_to_2021": "https://doi.org/10.6084/m9.figshare.20279733.v1",
            "v_reaction_smiles_2001_to_2023": "https://doi.org/10.6084/m9.figshare.22491730.v1",
            "v_reaction_smiles_2023": "https://doi.org/10.6084/m9.figshare.24921555.v1",
        }

    # ------------------------------------------------------------------------------------------------------------------
    #  Version: v_reaction_smiles_2001_to_2021
    # ------------------------------------------------------------------------------------------------------------------

    @staticmethod
    def _download_v_reaction_smiles_2001_to_2021(
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Download the data from the `v_reaction_smiles_2001_to_2021` version of the chemical reaction database.

        :parameter output_directory_path: The path to the output directory where the data should be downloaded.
        """

        AbstractBaseDataSource._download_file(
            file_url="https://figshare.com/ndownloader/files/36222051",
            file_name="reactionSmilesFigShare.txt",
            output_directory_path=output_directory_path
        )

    @staticmethod
    def _format_v_reaction_smiles_2001_to_2021(
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Format the data from the `v_reaction_smiles_2001_to_2021` version of the chemical reaction database.

        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        read_csv(
            filepath_or_buffer=Path(input_directory_path, "reactionSmilesFigShare.txt"),
            header=None
        ).rename(
            columns={
                0: "reaction_smiles",
            }
        ).to_csv(
            path_or_buf=Path(
                output_directory_path,
                "{timestamp:s}_crd_v_reaction_smiles_2001_to_2021.csv".format(
                    timestamp=datetime.now().strftime(
                        format="%Y%m%d%H%M%S"
                    )
                )
            ),
            index=False
        )

    # ------------------------------------------------------------------------------------------------------------------
    #  Version: v_reaction_smiles_2001_to_2023
    # ------------------------------------------------------------------------------------------------------------------

    @staticmethod
    def _download_v_reaction_smiles_2001_to_2023(
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Download the data from the `v_reaction_smiles_2001_to_2023` version of the chemical reaction database.

        :parameter output_directory_path: The path to the output directory where the data should be downloaded.
        """

        AbstractBaseDataSource._download_file(
            file_url="https://figshare.com/ndownloader/files/39944236",
            file_name="reactionSmilesFigShare2023.txt",
            output_directory_path=output_directory_path
        )

    @staticmethod
    def _format_v_reaction_smiles_2001_to_2023(
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Format the data from the `v_reaction_smiles_2001_to_2023` version of the chemical reaction database.

        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        read_csv(
            filepath_or_buffer=Path(input_directory_path, "reactionSmilesFigShare2023.txt"),
            header=None
        ).rename(
            columns={
                0: "reaction_smiles",
            }
        ).to_csv(
            path_or_buf=Path(
                output_directory_path,
                "{timestamp:s}_crd_v_reaction_smiles_2001_to_2023.csv".format(
                    timestamp=datetime.now().strftime(
                        format="%Y%m%d%H%M%S"
                    )
                )
            ),
            index=False
        )

    # ------------------------------------------------------------------------------------------------------------------
    #  Version: v_reaction_smiles_2023
    # ------------------------------------------------------------------------------------------------------------------

    @staticmethod
    def _download_v_reaction_smiles_2023(
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Download the data from the `v_reaction_smiles_2023` version of the chemical reaction database.

        :parameter output_directory_path: The path to the output directory where the data should be downloaded.
        """

        AbstractBaseDataSource._download_file(
            file_url="https://figshare.com/ndownloader/files/43858050",
            file_name="reactionSmilesFigShareUSPTO2023.txt",
            output_directory_path=output_directory_path
        )

    @staticmethod
    def _format_v_reaction_smiles_2023(
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Format the data from the `v_reaction_smiles_2023` version of the chemical reaction database.

        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        read_csv(
            filepath_or_buffer=Path(input_directory_path, "reactionSmilesFigShareUSPTO2023.txt"),
            header=None
        ).rename(
            columns={
                0: "reaction_smiles",
            }
        ).to_csv(
            path_or_buf=Path(
                output_directory_path,
                "{timestamp:s}_crd_v_reaction_smiles_2023.csv".format(
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
        Download the data from the chemical reaction database.

        :parameter version: The version of the chemical reaction database.
        :parameter output_directory_path: The path to the output directory where the data should be downloaded.
        """

        try:
            if version in self.available_versions.keys():
                if self.logger is not None:
                    self.logger.info(
                        msg="The download of the data from the {data_source:s} has been started.".format(
                            data_source="Chemical Reaction Database ({version:s})".format(
                                version=version
                            )
                        )
                    )

                if version == "v_reaction_smiles_2001_to_2021":
                    self._download_v_reaction_smiles_2001_to_2021(
                        output_directory_path=output_directory_path
                    )

                if version == "v_reaction_smiles_2001_to_2023":
                    self._download_v_reaction_smiles_2001_to_2023(
                        output_directory_path=output_directory_path
                    )

                if version == "v_reaction_smiles_2023":
                    self._download_v_reaction_smiles_2023(
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
                    "The {data_source:s} is not supported.".format(
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
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Extract the data from the chemical reaction database.

        :parameter version: The version of the chemical reaction database.
        :parameter input_directory_path: The path to the input directory where the data is downloaded.
        :parameter output_directory_path: The path to the output directory where the data should be extracted.
        """

        try:
            if version in self.available_versions.keys():
                if self.logger is not None:
                    self.logger.info(
                        msg="The extraction of the data from the {data_source:s} has been started.".format(
                            data_source="Chemical Reaction Database ({version:s})".format(
                                version=version
                            )
                        )
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
                    "The {data_source:s} is not supported.".format(
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
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Format the data from the chemical reaction database.

        :parameter version: The version of the chemical reaction database.
        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        try:
            if version in self.available_versions.keys():
                if self.logger is not None:
                    self.logger.info(
                        msg="The formatting of the data from the {data_source:s} has been started.".format(
                            data_source="Chemical Reaction Database ({version:s})".format(
                                version=version
                            )
                        )
                    )

                if version == "v_reaction_smiles_2001_to_2021":
                    self._format_v_reaction_smiles_2001_to_2021(
                        input_directory_path=input_directory_path,
                        output_directory_path=output_directory_path
                    )

                if version == "v_reaction_smiles_2001_to_2023":
                    self._format_v_reaction_smiles_2001_to_2023(
                        input_directory_path=input_directory_path,
                        output_directory_path=output_directory_path
                    )

                if version == "v_reaction_smiles_2023":
                    self._format_v_reaction_smiles_2023(
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
                    "The {data_source:s} is not supported.".format(
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
