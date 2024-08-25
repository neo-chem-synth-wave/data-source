""" The ``data_source.compound.miscellaneous.utility`` package ``formatting`` module. """

from datetime import datetime
from os import PathLike
from pathlib import Path
from typing import Union

from pandas import read_csv


class MiscellaneousCompoundDataSourceFormattingUtility:
    """ The miscellaneous chemical compound data source formatting utility class. """

    @staticmethod
    def format_v_moses_by_20201218_polykovskiy_d_et_al(
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Format the data from the `v_moses_by_20201218_polykovskiy_d_et_al` version of the chemical compound data source.

        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        read_csv(
            filepath_or_buffer=Path(input_directory_path, "dataset_v1.csv"),
            header=0
        ).to_csv(
            path_or_buf=Path(
                output_directory_path,
                "{timestamp:s}_miscellaneous_v_moses_by_20201218_polykovskiy_d_et_al.csv".format(
                    timestamp=datetime.now().strftime(
                        format="%Y%m%d%H%M%S"
                    )
                )
            ),
            index=False
        )
