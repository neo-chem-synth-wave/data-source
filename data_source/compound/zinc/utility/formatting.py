""" The ``data_source.compound.zinc.utility`` package ``formatting`` module. """

from datetime import datetime
from os import PathLike
from pathlib import Path
from typing import Union

from pandas.io.parsers.readers import read_csv


class ZINCCompoundDatabaseFormattingUtility:
    """ The `ZINC <https://zinc20.docking.org>`_ chemical compound database formatting utility class. """

    @staticmethod
    def format_v_building_blocks(
            version: str,
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Format the data from a `v_building_blocks_*` version of the database.

        :parameter version: The version of the database.
        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        input_file_name = "{input_file_name_prefix:s}.smi".format(
            input_file_name_prefix=version.split(
                sep="_",
                maxsplit=3
            )[-1]
        )

        output_file_name = "{timestamp:s}_zinc_{version:s}.csv".format(
            timestamp=datetime.now().strftime(
                format="%Y%m%d%H%M%S"
            ),
            version=version
        )

        dataframe = read_csv(
            filepath_or_buffer=Path(input_directory_path, input_file_name),
            sep=r"\s+",
            header=None
        ).rename(
            columns={
                0: "smiles",
                1: "id",
            }
        )

        dataframe["file_name"] = input_file_name

        dataframe.to_csv(
            path_or_buf=Path(output_directory_path, output_file_name),
            index=False
        )

    @staticmethod
    def format_v_catalog(
            version: str,
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Format the data from a `v_catalog_*` version of the database.

        :parameter version: The version of the database.
        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        input_file_name = "{input_file_name_prefix:s}.src.txt".format(
            input_file_name_prefix=version.split(
                sep="_",
                maxsplit=2
            )[-1]
        )

        output_file_name = "{timestamp:s}_zinc_{version:s}.csv".format(
            timestamp=datetime.now().strftime(
                format="%Y%m%d%H%M%S"
            ),
            version=version.replace("-", "_")
        )

        dataframe = read_csv(
            filepath_or_buffer=Path(input_directory_path, input_file_name),
            sep=r"\s+",
            header=None
        ).rename(
            columns={
                0: "smiles",
                1: "id",
            }
        )

        dataframe["file_name"] = input_file_name

        dataframe.to_csv(
            path_or_buf=Path(output_directory_path, output_file_name),
            index=False
        )
