""" The ``data_source.compound.coconut.utility`` package ``download`` module. """

from os import PathLike
from typing import Union

from data_source.base.utility.download import DataSourceDownloadUtility


class COCONUTCompoundDatabaseDownloadUtility:
    """ The `COCONUT <https://coconut.naturalproducts.net>`_ chemical compound database download utility class. """

    @staticmethod
    def download_v_2_0_by_20241126_chandrasekhar_v_et_al(
            version: str,
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Download the data from a `v_2_0_*_by_20241126_chandrasekhar_v_et_al` version of the database.

        :parameter version: The version of the database.
        :parameter output_directory_path: The path to the output directory where the data should be downloaded.
        """

        if version == "v_2_0_by_20241126_chandrasekhar_v_et_al":
            file_url = "https://zenodo.org/records/13897048/files/coconut-10-2024.csv.zip"

        elif version == "v_2_0_complete_by_20241126_chandrasekhar_v_et_al":
            file_url = "https://zenodo.org/records/13897048/files/coconut_complete-10-2024.csv.zip"

        else:
            raise ValueError(
                "The download of the data from the {data_source:s} is not supported.".format(
                    data_source="COCONUT chemical compound database ({version:s})".format(
                        version=version
                    )
                )
            )

        DataSourceDownloadUtility.download_file(
            url=file_url,
            name=file_url.split(
                sep="/"
            )[-1],
            output_directory_path=output_directory_path
        )
