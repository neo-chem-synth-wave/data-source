""" The ``data_source.compound_pattern.rdkit_.utility`` package ``download`` module. """

from os import PathLike
from typing import Union

from data_source.base.utility.download import DataSourceDownloadUtility


class RDKitCompoundPatternDatasetDownloadUtility:
    """ The `RDKit <https://www.rdkit.org>`_ chemical compound pattern dataset download utility class. """

    @staticmethod
    def download_v_brenk_by_20080307_brenk_r_et_al(
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Download the data from the `v_brenk_by_20080307_brenk_r_et_al` version of the dataset.

        :parameter output_directory_path: The path to the output directory where the data should be downloaded.
        """

        file_url = "https://github.com/rdkit/rdkit/raw/refs/heads/master/Code/GraphMol/FilterCatalog/brenk.in"

        DataSourceDownloadUtility.download_file(
            url=file_url,
            name=file_url.split(
                sep="/"
            )[-1],
            output_directory_path=output_directory_path
        )

    @staticmethod
    def download_v_pains_by_20100204_baell_j_b_and_holloway_g_a(
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Download the data from the `v_pains_by_20100204_baell_j_b_and_holloway_g_a` version of the dataset.

        :parameter output_directory_path: The path to the output directory where the data should be downloaded.
        """

        file_urls = [
            "https://github.com/rdkit/rdkit/raw/refs/heads/master/Code/GraphMol/FilterCatalog/pains_a.in",
            "https://github.com/rdkit/rdkit/raw/refs/heads/master/Code/GraphMol/FilterCatalog/pains_b.in",
            "https://github.com/rdkit/rdkit/raw/refs/heads/master/Code/GraphMol/FilterCatalog/pains_c.in",
        ]

        for file_url in file_urls:
            DataSourceDownloadUtility.download_file(
                url=file_url,
                name=file_url.split(
                    sep="/"
                )[-1],
                output_directory_path=output_directory_path
            )
