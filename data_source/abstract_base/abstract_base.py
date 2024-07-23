""" The ``data_source.abstract_base`` package ``abstract_base`` module. """

from abc import ABC, abstractmethod
from functools import partial
from logging import Logger
from os import PathLike
from pathlib import Path
from shutil import copyfileobj
from typing import Dict, Optional, Union

from requests.api import get
from requests.models import Response

from tqdm.auto import tqdm


class AbstractBaseDataSource(ABC):
    """ The abstract base data source class. """

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

    @staticmethod
    def _send_http_get_request(
            http_get_request_url: str,
            **kwargs
    ) -> Response:
        """
        Send an `HTTP GET` request.

        :parameter http_get_request_url: The URL of the `HTTP GET` request.
        :parameter kwargs: The keyword arguments for the adjustment of the following underlying functions:
            { `requests.api.get` }.

        :returns: The response to the `HTTP GET` request.
        """

        http_get_request_response = get(
            url=http_get_request_url,
            **kwargs
        )

        http_get_request_response.raise_for_status()

        return http_get_request_response

    @staticmethod
    def _download_file(
            file_url: str,
            file_name: str,
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Download a file.

        :parameter file_url: The URL of the file.
        :parameter file_name: The name of the file.
        :parameter output_directory_path: The path to the output directory where the file should be downloaded.
        """

        http_get_request_response = AbstractBaseDataSource._send_http_get_request(
            http_get_request_url=file_url,
            stream=True
        )

        http_get_request_response.raw.read = partial(
            http_get_request_response.raw.read,
            decode_content=True
        )

        file_size = http_get_request_response.headers.get("Content-Length", None)

        with tqdm.wrapattr(
            stream=http_get_request_response.raw,
            method="read",
            total=float(file_size) if file_size is not None else None,
            desc="Downloading the '{file_name:s}' file".format(
                file_name=file_name
            ),
            ncols=150
        ) as file_download_stream_handle:
            with Path(output_directory_path, file_name).open(
                mode="wb"
            ) as file_handle:
                copyfileobj(
                    fsrc=file_download_stream_handle,
                    fdst=file_handle
                )

    @property
    @abstractmethod
    def available_versions(
            self
    ) -> Dict[str, str]:
        """
        Get the available versions of the data source.

        :returns: The available versions of the data source.
        """

    @abstractmethod
    def download(
            self,
            version: str,
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Download the data from the data source.

        :parameter version: The version of the data source.
        :parameter output_directory_path: The path to the output directory where the data should be downloaded.
        """

    @abstractmethod
    def extract(
            self,
            version: str,
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Extract the data from the data source.

        :parameter version: The version of the data source.
        :parameter input_directory_path: The path to the input directory where the data is downloaded.
        :parameter output_directory_path: The path to the output directory where the data should be extracted.
        """

    @abstractmethod
    def format(
            self,
            version: str,
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Format the data from the data source.

        :parameter version: The version of the data source.
        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """
