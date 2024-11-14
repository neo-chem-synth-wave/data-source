""" The ``data_source.compound.miscellaneous.utility`` package ``download`` module. """

from os import PathLike
from typing import Union

from data_source.base.utility.download import BaseDataSourceDownloadUtility


class MiscellaneousCompoundDataSourceDownloadUtility:
    """ The miscellaneous chemical compound data source download utility class. """

    @staticmethod
    def download_v_moses_by_20201218_polykovskiy_d_et_al(
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Download the data from the `v_moses_by_20201218_polykovskiy_d_et_al` version of the data source.

        :parameter output_directory_path: The path to the output directory where the data should be downloaded.
        """

        file_name = "dataset_v1.csv"

        file_url = "https://media.githubusercontent.com/media/molecularsets/moses/master/data/{file_name:s}".format(
            file_name=file_name
        )

        BaseDataSourceDownloadUtility.download_file(
            file_url=file_url,
            file_name=file_name,
            output_directory_path=output_directory_path
        )
