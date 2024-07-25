""" The ``data_source.reaction_rule`` package ``retro_rules`` module. """

from datetime import datetime
from logging import Logger
from os import PathLike
from pathlib import Path
from shutil import copyfileobj
from typing import Dict, Optional, Union

from pandas.io.parsers.readers import read_csv

from tarfile import open as open_tar_archive_file

from data_source.abstract_base.abstract_base import AbstractBaseDataSource


class RetroRulesReactionRuleDatabase(AbstractBaseDataSource):
    """ The `RetroRules <https://retrorules.org>`_ chemical reaction rule database class. """

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
        Get the available versions of the chemical reaction rule database.

        :returns: The available versions of the chemical reaction rule database.
        """

        return {
            "v_release_rr01_rp2_hs": "https://doi.org/10.5281/zenodo.5827427",
            "v_release_rr02_rp2_hs": "https://doi.org/10.5281/zenodo.5828017",
            "v_release_rr02_rp3_hs": "https://doi.org/10.5281/zenodo.5827977",
            "v_release_rr02_rp3_nohs": "https://doi.org/10.5281/zenodo.5827969",
        }

    # ------------------------------------------------------------------------------------------------------------------
    #  Version: v_release_rr01_rp2_hs
    # ------------------------------------------------------------------------------------------------------------------

    @staticmethod
    def _download_v_release_rr01_rp2_hs(
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Download the data from the `v_release_rr01_rp2_hs` version of the chemical reaction rule database.

        :parameter output_directory_path: The path to the output directory where the data should be downloaded.
        """

        AbstractBaseDataSource._download_file(
            file_url="https://zenodo.org/records/5827427/files/retrorules_rr01_rp2.tar.gz",
            file_name="retrorules_rr01_rp2.tar.gz",
            output_directory_path=output_directory_path
        )

    @staticmethod
    def _extract_v_release_rr01_rp2_hs(
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Extract the data from the `v_release_rr01_rp2_hs` version of the chemical reaction rule database.

        :parameter input_directory_path: The path to the input directory where the data is downloaded.
        :parameter output_directory_path: The path to the output directory where the data should be extracted.
        """

        with open_tar_archive_file(
            name=Path(input_directory_path, "retrorules_rr01_rp2.tar.gz"),
            mode="r:gz"
        ) as tar_archive_file_handle:
            with tar_archive_file_handle.extractfile(
                member="retrorules_rr01_rp2/retrorules_rr01_rp2_flat_all.csv"
            ) as source_file_handle:
                with open(
                    file=Path(output_directory_path, "retrorules_rr01_rp2_flat_all.csv"),
                    mode="wb"
                ) as destination_file_handle:
                    copyfileobj(
                        fsrc=source_file_handle,
                        fdst=destination_file_handle
                    )

    @staticmethod
    def _format_v_release_rr01_rp2_hs(
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Format the data from the `v_release_rr01_rp2_hs` version of the chemical reaction rule database.

        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        read_csv(
            filepath_or_buffer=Path(input_directory_path, "retrorules_rr01_rp2_flat_all.csv"),
            header=0
        ).to_csv(
            path_or_buf=Path(
                output_directory_path,
                "{timestamp:s}_retro_rules_v_release_rr01_rp2_hs.csv".format(
                    timestamp=datetime.now().strftime(
                        format="%Y%m%d%H%M%S"
                    )
                )
            ),
            index=False
        )

    # ------------------------------------------------------------------------------------------------------------------
    #  Version: v_release_rr02_rp2_hs
    # ------------------------------------------------------------------------------------------------------------------

    @staticmethod
    def _download_v_release_rr02_rp2_hs(
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Download the data from the `v_release_rr02_rp2_hs` version of the chemical reaction rule database.

        :parameter output_directory_path: The path to the output directory where the data should be downloaded.
        """

        AbstractBaseDataSource._download_file(
            file_url="https://zenodo.org/records/5828017/files/retrorules_rr02_rp2_hs.tar.gz",
            file_name="retrorules_rr02_rp2_hs.tar.gz",
            output_directory_path=output_directory_path
        )

    @staticmethod
    def _extract_v_release_rr02_rp2_hs(
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Extract the data from the `v_release_rr02_rp2_hs` version of the chemical reaction rule database.

        :parameter input_directory_path: The path to the input directory where the data is downloaded.
        :parameter output_directory_path: The path to the output directory where the data should be extracted.
        """

        with open_tar_archive_file(
            name=Path(input_directory_path, "retrorules_rr02_rp2_hs.tar.gz"),
            mode="r:gz"
        ) as tar_archive_file_handle:
            with tar_archive_file_handle.extractfile(
                member="retrorules_rr02_rp2_hs/retrorules_rr02_rp2_flat_all.csv"
            ) as source_file_handle:
                with open(
                    file=Path(output_directory_path, "retrorules_rr02_rp2_flat_all.csv"),
                    mode="wb"
                ) as destination_file_handle:
                    copyfileobj(
                        fsrc=source_file_handle,
                        fdst=destination_file_handle
                    )

    @staticmethod
    def _format_v_release_rr02_rp2_hs(
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Format the data from the `v_release_rr02_rp2_hs` version of the chemical reaction rule database.

        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        read_csv(
            filepath_or_buffer=Path(input_directory_path, "retrorules_rr02_rp2_flat_all.csv"),
            header=0
        ).to_csv(
            path_or_buf=Path(
                output_directory_path,
                "{timestamp:s}_retro_rules_v_release_rr02_rp2_hs.csv".format(
                    timestamp=datetime.now().strftime(
                        format="%Y%m%d%H%M%S"
                    )
                )
            ),
            index=False
        )

    # ------------------------------------------------------------------------------------------------------------------
    #  Version: v_release_rr02_rp3_hs
    # ------------------------------------------------------------------------------------------------------------------

    @staticmethod
    def _download_v_release_rr02_rp3_hs(
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Download the data from the `v_release_rr02_rp3_hs` version of the chemical reaction rule database.

        :parameter output_directory_path: The path to the output directory where the data should be downloaded.
        """

        AbstractBaseDataSource._download_file(
            file_url="https://zenodo.org/records/5827977/files/retrorules_rr02_rp3_hs.tar.gz",
            file_name="retrorules_rr02_rp3_hs.tar.gz",
            output_directory_path=output_directory_path
        )

    @staticmethod
    def _extract_v_release_rr02_rp3_hs(
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Extract the data from the `v_release_rr02_rp3_hs` version of the chemical reaction rule database.

        :parameter input_directory_path: The path to the input directory where the data is downloaded.
        :parameter output_directory_path: The path to the output directory where the data should be extracted.
        """

        with open_tar_archive_file(
            name=Path(input_directory_path, "retrorules_rr02_rp3_hs.tar.gz"),
            mode="r:gz"
        ) as tar_archive_file_handle:
            with tar_archive_file_handle.extractfile(
                member="retrorules_rr02_rp3_hs/retrorules_rr02_flat_all.tsv"
            ) as source_file_handle:
                with open(
                    file=Path(output_directory_path, "retrorules_rr02_flat_all.tsv"),
                    mode="wb"
                ) as destination_file_handle:
                    copyfileobj(
                        fsrc=source_file_handle,
                        fdst=destination_file_handle
                    )

    @staticmethod
    def _format_v_release_rr02_rp3_hs(
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Format the data from the `v_release_rr02_rp3_hs` version of the chemical reaction rule database.

        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        read_csv(
            filepath_or_buffer=Path(input_directory_path, "retrorules_rr02_flat_all.tsv"),
            sep="\t",
            header=0
        ).to_csv(
            path_or_buf=Path(
                output_directory_path,
                "{timestamp:s}_retro_rules_v_release_rr02_rp3_hs.csv".format(
                    timestamp=datetime.now().strftime(
                        format="%Y%m%d%H%M%S"
                    )
                )
            ),
            index=False
        )

    # ------------------------------------------------------------------------------------------------------------------
    #  Version: v_release_rr02_rp3_nohs
    # ------------------------------------------------------------------------------------------------------------------

    @staticmethod
    def _download_v_release_rr02_rp3_nohs(
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Download the data from the `v_release_rr02_rp3_nohs` version of the chemical reaction rule database.

        :parameter output_directory_path: The path to the output directory where the data should be downloaded.
        """

        AbstractBaseDataSource._download_file(
            file_url="https://zenodo.org/records/5827969/files/retrorules_rr02_rp3_nohs.tar.gz",
            file_name="retrorules_rr02_rp3_nohs.tar.gz",
            output_directory_path=output_directory_path
        )

    @staticmethod
    def _extract_v_release_rr02_rp3_nohs(
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Extract the data from the `v_release_rr02_rp3_nohs` version of the chemical reaction rule database.

        :parameter input_directory_path: The path to the input directory where the data is downloaded.
        :parameter output_directory_path: The path to the output directory where the data should be extracted.
        """

        with open_tar_archive_file(
            name=Path(input_directory_path, "retrorules_rr02_rp3_nohs.tar.gz"),
            mode="r:gz"
        ) as tar_archive_file_handle:
            with tar_archive_file_handle.extractfile(
                member="retrorules_rr02_rp3_nohs/retrorules_rr02_flat_all.tsv"
            ) as source_file_handle:
                with open(
                    file=Path(output_directory_path, "retrorules_rr02_flat_all.tsv"),
                    mode="wb"
                ) as destination_file_handle:
                    copyfileobj(
                        fsrc=source_file_handle,
                        fdst=destination_file_handle
                    )

    @staticmethod
    def _format_v_release_rr02_rp3_nohs(
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Format the data from the `v_release_rr02_rp3_nohs` version of the chemical reaction rule database.

        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        read_csv(
            filepath_or_buffer=Path(input_directory_path, "retrorules_rr02_flat_all.tsv"),
            sep="\t",
            header=0
        ).to_csv(
            path_or_buf=Path(
                output_directory_path,
                "{timestamp:s}_retro_rules_v_release_rr02_rp3_nohs.csv".format(
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
        Download the data from the chemical reaction rule database.

        :parameter version: The version of the chemical reaction rule database.
        :parameter output_directory_path: The path to the output directory where the data should be downloaded.
        """

        try:
            if version in self.available_versions.keys():
                if self.logger is not None:
                    self.logger.info(
                        msg="The download of the data from the {data_source:s} has been started.".format(
                            data_source="RetroRules chemical reaction rule database ({version:s})".format(
                                version=version
                            )
                        )
                    )

                if version == "v_release_rr01_rp2_hs":
                    self._download_v_release_rr01_rp2_hs(
                        output_directory_path=output_directory_path
                    )

                if version == "v_release_rr02_rp2_hs":
                    self._download_v_release_rr02_rp2_hs(
                        output_directory_path=output_directory_path
                    )

                if version == "v_release_rr02_rp3_hs":
                    self._download_v_release_rr02_rp3_hs(
                        output_directory_path=output_directory_path
                    )

                if version == "v_release_rr02_rp3_nohs":
                    self._download_v_release_rr02_rp3_nohs(
                        output_directory_path=output_directory_path
                    )

                if self.logger is not None:
                    self.logger.info(
                        msg="The download of the data from the {data_source:s} has been completed.".format(
                            data_source="RetroRules chemical reaction rule database ({version:s})".format(
                                version=version
                            )
                        )
                    )

            else:
                raise ValueError(
                    "The {data_source:s} is not supported.".format(
                        data_source="RetroRules chemical reaction rule database ({version:s})".format(
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
        Extract the data from the chemical reaction rule database.

        :parameter version: The version of the chemical reaction rule database.
        :parameter input_directory_path: The path to the input directory where the data is downloaded.
        :parameter output_directory_path: The path to the output directory where the data should be extracted.
        """

        try:
            if version in self.available_versions.keys():
                if self.logger is not None:
                    self.logger.info(
                        msg="The extraction of the data from the {data_source:s} has been started.".format(
                            data_source="RetroRules chemical reaction rule database ({version:s})".format(
                                version=version
                            )
                        )
                    )

                if version == "v_release_rr01_rp2_hs":
                    self._extract_v_release_rr01_rp2_hs(
                        input_directory_path=input_directory_path,
                        output_directory_path=output_directory_path
                    )

                if version == "v_release_rr02_rp2_hs":
                    self._extract_v_release_rr02_rp2_hs(
                        input_directory_path=input_directory_path,
                        output_directory_path=output_directory_path
                    )

                if version == "v_release_rr02_rp3_hs":
                    self._extract_v_release_rr02_rp3_hs(
                        input_directory_path=input_directory_path,
                        output_directory_path=output_directory_path
                    )

                if version == "v_release_rr02_rp3_nohs":
                    self._extract_v_release_rr02_rp3_nohs(
                        input_directory_path=input_directory_path,
                        output_directory_path=output_directory_path
                    )

                if self.logger is not None:
                    self.logger.info(
                        msg="The extraction of the data from the {data_source:s} has been completed.".format(
                            data_source="RetroRules chemical reaction rule database ({version:s})".format(
                                version=version
                            )
                        )
                    )

            else:
                raise ValueError(
                    "The {data_source:s} is not supported.".format(
                        data_source="RetroRules chemical reaction rule database ({version:s})".format(
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
        Format the data from the chemical reaction rule database.

        :parameter version: The version of the chemical reaction rule database.
        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        try:
            if version in self.available_versions.keys():
                if self.logger is not None:
                    self.logger.info(
                        msg="The formatting of the data from the {data_source:s} has been started.".format(
                            data_source="RetroRules chemical reaction rule database ({version:s})".format(
                                version=version
                            )
                        )
                    )

                if version == "v_release_rr01_rp2_hs":
                    self._format_v_release_rr01_rp2_hs(
                        input_directory_path=input_directory_path,
                        output_directory_path=output_directory_path
                    )

                if version == "v_release_rr02_rp2_hs":
                    self._format_v_release_rr02_rp2_hs(
                        input_directory_path=input_directory_path,
                        output_directory_path=output_directory_path
                    )

                if version == "v_release_rr02_rp3_hs":
                    self._format_v_release_rr02_rp3_hs(
                        input_directory_path=input_directory_path,
                        output_directory_path=output_directory_path
                    )

                if version == "v_release_rr02_rp3_nohs":
                    self._format_v_release_rr02_rp3_nohs(
                        input_directory_path=input_directory_path,
                        output_directory_path=output_directory_path
                    )

                if self.logger is not None:
                    self.logger.info(
                        msg="The formatting of the data from the {data_source:s} has been completed.".format(
                            data_source="RetroRules chemical reaction rule database ({version:s})".format(
                                version=version
                            )
                        )
                    )

            else:
                raise ValueError(
                    "The {data_source:s} is not supported.".format(
                        data_source="RetroRules chemical reaction rule database ({version:s})".format(
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
