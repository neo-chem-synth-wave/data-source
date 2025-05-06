""" The ``data_source.compound_pattern.rdkit_`` package ``rdkit_`` module. """

from os import PathLike
from typing import Dict, Union

from data_source.base.base import DataSourceBase
from data_source.compound_pattern.rdkit_.utility.download import RDKitCompoundPatternDatasetDownloadUtility
from data_source.compound_pattern.rdkit_.utility.formatting import RDKitCompoundPatternDatasetFormattingUtility


class RDKitCompoundPatternDataset(DataSourceBase):
    """ The `RDKit <https://www.rdkit.org>`_ chemical compound pattern dataset class. """

    @staticmethod
    def get_supported_versions() -> Dict[str, str]:
        """
        Get the supported versions of the dataset.

        :returns: The supported versions of the dataset.
        """

        return {
            "v_brenk_by_20080307_brenk_r_et_al": "https://doi.org/10.1002/cmdc.200700139",
            "v_pains_by_20100204_baell_j_b_and_holloway_g_a": "https://doi.org/10.1021/jm901137j",
        }

    def download(
            self,
            version: str,
            output_directory_path: Union[str, PathLike[str]],
            **kwargs
    ) -> None:
        """
        Download the data from the dataset.

        :parameter version: The version of the dataset.
        :parameter output_directory_path: The path to the output directory where the data should be downloaded.
        """

        try:
            if version in self.get_supported_versions().keys():
                if self.logger is not None:
                    self.logger.info(
                        msg="The download of the data from the {data_source:s} has been started.".format(
                            data_source="RDKit chemical compound pattern dataset ({version:s})".format(
                                version=version
                            )
                        )
                    )

                if version == "v_brenk_by_20080307_brenk_r_et_al":
                    RDKitCompoundPatternDatasetDownloadUtility.download_v_brenk_by_20080307_brenk_r_et_al(
                        output_directory_path=output_directory_path
                    )

                if version == "v_pains_by_20100204_baell_j_b_and_holloway_g_a":
                    RDKitCompoundPatternDatasetDownloadUtility.download_v_pains_by_20100204_baell_j_b_and_holloway_g_a(
                        output_directory_path=output_directory_path
                    )

                if self.logger is not None:
                    self.logger.info(
                        msg="The download of the data from the {data_source:s} has been completed.".format(
                            data_source="RDKit chemical compound pattern dataset ({version:s})".format(
                                version=version
                            )
                        )
                    )

            else:
                raise ValueError(
                    "The download of the data from the {data_source:s} is not supported.".format(
                        data_source="RDKit chemical compound pattern dataset ({version:s})".format(
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
        Extract the data from the dataset.

        :parameter version: The version of the dataset.
        :parameter input_directory_path: The path to the input directory where the data is downloaded.
        :parameter output_directory_path: The path to the output directory where the data should be extracted.
        """

        try:
            if version in self.get_supported_versions().keys():
                if self.logger is not None:
                    self.logger.info(
                        msg="The extraction of the data from the {data_source:s} has been started.".format(
                            data_source="RDKit chemical compound pattern dataset ({version:s})".format(
                                version=version
                            )
                        )
                    )

                if self.logger is not None:
                    self.logger.info(
                        msg="The extraction of the data from the {data_source:s} has been completed.".format(
                            data_source="RDKit chemical compound pattern dataset ({version:s})".format(
                                version=version
                            )
                        )
                    )

            else:
                raise ValueError(
                    "The extraction of the data from the {data_source:s} is not supported.".format(
                        data_source="RDKit chemical compound pattern dataset ({version:s})".format(
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
        Format the data from the dataset.

        :parameter version: The version of the dataset.
        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        try:
            if version in self.get_supported_versions().keys():
                if self.logger is not None:
                    self.logger.info(
                        msg="The formatting of the data from the {data_source:s} has been started.".format(
                            data_source="RDKit chemical compound pattern dataset ({version:s})".format(
                                version=version
                            )
                        )
                    )

                if version == "v_brenk_by_20080307_brenk_r_et_al":
                    RDKitCompoundPatternDatasetFormattingUtility.format_v_brenk_by_20080307_brenk_r_et_al(
                        input_directory_path=input_directory_path,
                        output_directory_path=output_directory_path
                    )

                if version == "v_pains_by_20100204_baell_j_b_and_holloway_g_a":
                    RDKitCompoundPatternDatasetFormattingUtility.format_v_pains_by_20100204_baell_j_b_and_holloway_g_a(
                        input_directory_path=input_directory_path,
                        output_directory_path=output_directory_path
                    )

                if self.logger is not None:
                    self.logger.info(
                        msg="The formatting of the data from the {data_source:s} has been completed.".format(
                            data_source="RDKit chemical compound pattern dataset ({version:s})".format(
                                version=version
                            )
                        )
                    )

            else:
                raise ValueError(
                    "The formatting of the data from the {data_source:s} is not supported.".format(
                        data_source="RDKit chemical compound pattern dataset ({version:s})".format(
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
