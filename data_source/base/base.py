""" The ``data_source.base`` package ``base`` module. """

from abc import ABC, abstractmethod
from logging import Logger
from typing import Optional


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

    @abstractmethod
    def download(
            self,
            **kwargs
    ) -> None:
        """
        Download the data from the data source.

        :parameter kwargs: The keyword arguments of the method.
        """

    @abstractmethod
    def extract(
            self,
            **kwargs
    ) -> None:
        """
        Extract the data from the data source.

        :parameter kwargs: The keyword arguments of the method.
        """

    @abstractmethod
    def format(
            self,
            **kwargs
    ) -> None:
        """
        Format the data from the data source.

        :parameter kwargs: The keyword arguments of the method.
        """
