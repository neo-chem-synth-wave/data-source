""" The ``data_source.compound.coconut.utility`` package ``formatting`` module. """

from datetime import datetime
from os import PathLike
from pathlib import Path
from typing import Union

from pandas.io.parsers.readers import read_csv


class COCONUTCompoundDatabaseFormattingUtility:
    """ The `COCONUT <https://coconut.naturalproducts.net>`_ chemical compound database formatting utility class. """

    @staticmethod
    def format_v_2_0_by_20241126_chandrasekhar_v_et_al(
            version: str,
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Format the data from a `v_2_0_*_by_20241126_chandrasekhar_v_et_al` version of the database.

        :parameter version: The version of the database.
        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        if version == "v_2_0_by_20241126_chandrasekhar_v_et_al":
            input_file_name = "coconut-10-2024.csv"

        elif version == "v_2_0_complete_by_20241126_chandrasekhar_v_et_al":
            input_file_name = "coconut_complete-10-2024.csv"

        else:
            raise ValueError(
                "The formatting of the data from the {data_source:s} is not supported.".format(
                    data_source="COCONUT chemical compound database ({version:s})".format(
                        version=version
                    )
                )
            )

        output_file_name = "{timestamp:s}_coconut_{version:s}.csv".format(
            timestamp=datetime.now().strftime(
                format="%Y%m%d%H%M%S"
            ),
            version=version
        )

        dataframe = read_csv(
            filepath_or_buffer=Path(input_directory_path, input_file_name),
            header=0
        )

        dataframe["file_name"] = input_file_name

        dataframe.to_csv(
            path_or_buf=Path(output_directory_path, output_file_name),
            index=False
        )
