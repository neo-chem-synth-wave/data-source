""" The ``data_source.base.utility`` package ``download`` module. """

from functools import partial
from os import PathLike
from pathlib import Path
from shutil import copyfileobj
from typing import Union

from requests import Response, get

from tqdm.auto import tqdm


class BaseDataSourceDownloadUtility:
    """ The base data source download utility class. """

    @staticmethod
    def send_http_get_request(
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

        http_get_request_response = BaseDataSourceDownloadUtility.send_http_get_request(
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
            ) as destination_file_handle:
                copyfileobj(
                    fsrc=file_download_stream_handle,
                    fdst=destination_file_handle
                )
