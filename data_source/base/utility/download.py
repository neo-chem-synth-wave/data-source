""" The ``data_source.base.utility`` package ``download`` module. """

from functools import partial
from os import PathLike
from pathlib import Path
from shutil import copyfileobj
from typing import Union

from requests.api import get
from requests.models import Response

from tqdm.auto import tqdm


class DataSourceDownloadUtility:
    """ The data source download utility class. """

    @staticmethod
    def send_http_get_request(
            http_get_request_url: str,
            **kwargs
    ) -> Response:
        """
        Send an HTTP GET request.

        :parameter http_get_request_url: The URL of the HTTP GET request.
        :parameter kwargs: The keyword arguments for the adjustment of the following underlying functions:
            { `requests.api.get` }.

        :returns: The response to the HTTP GET request.
        """

        kwargs.pop("url", None)

        http_get_request_response = get(
            url=http_get_request_url,
            **kwargs
        )

        http_get_request_response.raise_for_status()

        return http_get_request_response

    @staticmethod
    def download_file(
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

        http_get_request_response = DataSourceDownloadUtility.send_http_get_request(
            http_get_request_url=file_url,
            stream=True
        )

        http_get_request_response.raw.read = partial(
            http_get_request_response.raw.read,
            decode_content=True
        )

        try:
            file_size = http_get_request_response.headers.get("Content-Length", None)

            if file_size is not None:
                file_size = float(file_size)

        except:
            file_size = None

        tqdm_description = "Downloading the '{file_name:s}' file".format(
            file_name=file_name
        )

        with tqdm.wrapattr(
            stream=http_get_request_response.raw,
            method="read",
            total=file_size,
            desc=tqdm_description,
            ncols=len(tqdm_description) + 50
        ) as file_download_stream_handle:
            with Path(output_directory_path, file_name).open(
                mode="wb"
            ) as destination_file_handle:
                copyfileobj(
                    fsrc=file_download_stream_handle,
                    fdst=destination_file_handle
                )
