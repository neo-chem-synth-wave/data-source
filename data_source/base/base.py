""" The ``data_source.base`` package ``base`` module. """

from abc import ABC, abstractmethod
from logging import Logger
from typing import Dict, Optional, Type


class BaseDataSource(ABC):
    """ The base data source class. """

    def __init__(
            self,
            logger: Optional[Logger] = None
    ) -> None:
        """
        The constructor method of the class.

        :parameter logger: The logger. The value `None` indicates that the logger should not be utilized.
        """

        self.logger = logger

    @property
    def logger(
            self
    ) -> Optional[Logger]:
        """
        Get the logger.

        :returns: The logger.
        """

        return self.__logger

    @logger.setter
    def logger(
            self,
            value: Optional[Logger]
    ) -> None:
        """
        Set the logger.

        :parameter value: The logger. The value `None` indicates that the logger should not be utilized.
        """

        self.__logger = value

    def _raise_and_log_exception(
            self,
            exception_class: Type[Exception],
            exception_message: str
    ) -> None:
        """
        Raise and log an exception.

        :parameter exception_class: The class of the exception.
        :parameter exception_message: The message of the exception.
        """

        exception_handle = exception_class(exception_message)

        if self.__logger is not None:
            self.__logger.error(
                msg=exception_handle
            )

        raise exception_handle

    @abstractmethod
    def get_supported_versions(
            self,
            **kwargs
    ) -> Dict[str, str]:
        """
        Get the supported versions of the data source.

        :parameter kwargs: The keyword arguments.

        :returns: The supported versions of the data source.
        """

    @abstractmethod
    def download(
            self,
            **kwargs
    ) -> None:
        """
        Download the data from the data source.

        :parameter kwargs: The keyword arguments.
        """

    @abstractmethod
    def extract(
            self,
            **kwargs
    ) -> None:
        """
        Extract the data from the data source.

        :parameter kwargs: The keyword arguments.
        """

    @abstractmethod
    def format(
            self,
            **kwargs
    ) -> None:
        """
        Format the data from the data source.

        :parameter kwargs: The keyword arguments.
        """
