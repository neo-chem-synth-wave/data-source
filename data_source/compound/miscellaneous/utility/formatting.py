""" The ``data_source.compound.miscellaneous.utility`` package ``formatting`` module. """

from datetime import datetime
from os import PathLike
from pathlib import Path
from typing import Union

from pandas.io.parsers.readers import read_csv


class MiscellaneousCompoundDataSourceFormattingUtility:
    """ The miscellaneous chemical compound data source formatting utility class. """

    @staticmethod
    def format_v_moses_by_20201218_polykovskiy_d_et_al(
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Format the data from the `v_moses_by_20201218_polykovskiy_d_et_al` version of the data source.

        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        input_file_name = "dataset_v1.csv"

        output_file_name = "{timestamp:s}_miscellaneous_v_moses_by_20201218_polykovskiy_d_et_al.csv".format(
            timestamp=datetime.now().strftime(
                format="%Y%m%d%H%M%S"
            )
        )

        dataframe = read_csv(
            filepath_or_buffer=Path(input_directory_path, input_file_name),
            header=0
        )

        dataframe["FILE_NAME"] = input_file_name

        dataframe.to_csv(
            path_or_buf=Path(output_directory_path, output_file_name),
            index=False
        )
