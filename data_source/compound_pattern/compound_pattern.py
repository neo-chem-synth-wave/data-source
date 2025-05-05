""" The ``data_source.compound_pattern`` package ``compound_pattern`` module. """

from logging import Logger
from os import PathLike
from typing import Dict, List, Optional, Union

from data_source.base.base import DataSourceBase
from data_source.compound_pattern.rdkit_.rdkit_ import RDKitCompoundPatternDataset


class CompoundPatternDataSource(DataSourceBase):
    """ The chemical compound pattern data source class. """

    def __init__(
            self,
            logger: Optional[Logger] = None
    ) -> None:
        """
        The `__init__` method of the class.

        :parameter logger: The logger. The value `None` indicates that the logger should not be utilized.
        """

        super().__init__(
            logger=logger
        )

        self.supported_data_sources = {
            "rdkit": RDKitCompoundPatternDataset(
                logger=logger
            ),
        }

    def get_names_of_supported_data_sources(
            self
    ) -> List[str]:
        """
        Get the names of the supported data sources.

        :returns: The names of the supported data sources.
        """

        return list(self.supported_data_sources.keys())

    def get_supported_versions(
            self,
            name: str
    ) -> Dict[str, str]:
        """
        Get the supported versions of a data source.

        :parameter name: The name of the data source.

        :returns: The supported versions of the data source.
        """

        if name in self.get_names_of_supported_data_sources():
            return self.supported_data_sources[name].get_supported_versions()

        else:
            exception_handle = ValueError(
                "The chemical compound pattern data source name '{name:s}' is not supported.".format(
                    name=name
                )
            )

            if self.logger is not None:
                self.logger.error(
                    msg=exception_handle
                )

            raise exception_handle

    def download_(
            self,
            name: str,
            version: str,
            output_directory_path: Union[str, PathLike[str]],
            **kwargs
    ) -> None:
        """
        Download the data from a data source.

        :parameter name: The name of the data source.
        :parameter version: The version of the data source.
        :parameter output_directory_path: The path to the output directory where the data should be downloaded.
        """

        if name in self.get_names_of_supported_data_sources():
            self.supported_data_sources[name].download_(
                version=version,
                output_directory_path=output_directory_path,
                **kwargs
            )

        else:
            exception_handle = ValueError(
                "The chemical compound pattern data source name '{name:s}' is not supported.".format(
                    name=name
                )
            )

            if self.logger is not None:
                self.logger.error(
                    msg=exception_handle
                )

            raise exception_handle

    def extract_(
            self,
            name: str,
            version: str,
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]],
            **kwargs
    ) -> None:
        """
        Extract the data from a data source.

        :parameter name: The name of the data source.
        :parameter version: The version of the data source.
        :parameter input_directory_path: The path to the input directory where the data is downloaded.
        :parameter output_directory_path: The path to the output directory where the data should be extracted.
        """

        if name in self.get_names_of_supported_data_sources():
            self.supported_data_sources[name].extract_(
                version=version,
                input_directory_path=input_directory_path,
                output_directory_path=output_directory_path,
                **kwargs
            )

        else:
            exception_handle = ValueError(
                "The chemical compound pattern data source name '{name:s}' is not supported.".format(
                    name=name
                )
            )

            if self.logger is not None:
                self.logger.error(
                    msg=exception_handle
                )

            raise exception_handle

    def format_(
            self,
            name: str,
            version: str,
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]],
            **kwargs
    ) -> None:
        """
        Format the data from a data source.

        :parameter name: The name of the data source.
        :parameter version: The version of the data source.
        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        if name in self.get_names_of_supported_data_sources():
            self.supported_data_sources[name].format_(
                version=version,
                input_directory_path=input_directory_path,
                output_directory_path=output_directory_path,
                **kwargs
            )

        else:
            exception_handle = ValueError(
                "The chemical compound pattern data source name '{name:s}' is not supported.".format(
                    name=name
                )
            )

            if self.logger is not None:
                self.logger.error(
                    msg=exception_handle
                )

            raise exception_handle
