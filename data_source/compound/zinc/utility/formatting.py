""" The ``data_source.compound.zinc.utility`` package ``formatting`` module. """

from datetime import datetime
from os import PathLike
from pathlib import Path
from typing import Union

from pandas import read_csv


class ZINCCompoundDatabaseFormattingUtility:
    """ The `ZINC <https://zinc20.docking.org>`_ chemical compound database formatting utility class. """

    @staticmethod
    def format_v_building_blocks(
            version: str,
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Format the data from a `v_building_blocks_*` version of the chemical compound database.

        :parameter version: The version of the chemical compound database.
        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        read_csv(
            filepath_or_buffer=Path(
                input_directory_path,
                "{file_name:s}.smi".format(
                    file_name=version.split(
                        sep="_",
                        maxsplit=3
                    )[-1]
                )
            ),
            sep=r"\s+",
            header=None
        ).rename(
            columns={
                0: "smiles",
                1: "id",
            }
        ).to_csv(
            path_or_buf=Path(
                output_directory_path,
                "{timestamp:s}_zinc_{version:s}.csv".format(
                    timestamp=datetime.now().strftime(
                        format="%Y%m%d%H%M%S"
                    ),
                    version=version.replace("-", "_")
                )
            ),
            index=False
        )

    @staticmethod
    def format_v_catalog(
            version: str,
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Format the data from a `v_catalog_*` version of the chemical compound database.

        :parameter version: The version of the chemical compound database.
        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        read_csv(
            filepath_or_buffer=Path(
                input_directory_path,
                "{file_name:s}.src.txt".format(
                    file_name=version.split(
                        sep="_",
                        maxsplit=2
                    )[-1]
                )
            ),
            sep=r"\s+",
            header=None
        ).rename(
            columns={
                0: "smiles",
                1: "id",
            }
        ).to_csv(
            path_or_buf=Path(
                output_directory_path,
                "{timestamp:s}_zinc_{version:s}.csv".format(
                    timestamp=datetime.now().strftime(
                        format="%Y%m%d%H%M%S"
                    ),
                    version=version.replace("-", "_")
                )
            ),
            index=False
        )

    @staticmethod
    def format_v_moses_by_20201218_polykovskiy_d_et_al(
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Format the data from the `v_moses_by_20201218_polykovskiy_d_et_al` version of the chemical compound database.

        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        read_csv(
            filepath_or_buffer=Path(input_directory_path, "dataset_v1.csv"),
            header=0
        ).to_csv(
            path_or_buf=Path(
                output_directory_path,
                "{timestamp:s}_zinc_v_moses_by_20201218_polykovskiy_d_et_al.csv".format(
                    timestamp=datetime.now().strftime(
                        format="%Y%m%d%H%M%S"
                    )
                )
            ),
            index=False
        )
