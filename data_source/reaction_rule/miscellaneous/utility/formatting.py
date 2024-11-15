""" The ``data_source.reaction_rule.miscellaneous.utility`` package ``formatting`` module. """

from datetime import datetime
from os import PathLike
from pathlib import Path
from typing import Union

from pandas.io.parsers.readers import read_csv


class MiscellaneousReactionRuleDataSourceFormattingUtility:
    """ The miscellaneous chemical reaction rule data source formatting utility class. """

    @staticmethod
    def format_v_retro_transform_db_by_20180421_avramova_s_et_al(
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Format the data from the `v_retro_transform_db_by_20180421_avramova_s_et_al` version of the data source.

        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        input_file_name = "RetroTransformDB-v-1-0.txt"

        output_file_name = "{timestamp:s}_miscellaneous_v_retro_transform_db_by_20180421_avramova_s_et_al.csv".format(
            timestamp=datetime.now().strftime(
                format="%Y%m%d%H%M%S"
            )
        )

        read_csv(
            filepath_or_buffer=Path(input_directory_path, input_file_name),
            sep="\t",
            header=0
        ).dropna(
            how="all"
        ).astype(
            dtype={
                "ID": int,
            }
        ).to_csv(
            path_or_buf=Path(output_directory_path, output_file_name),
            index=False
        )

    @staticmethod
    def format_v_dingos_by_20190701_button_a_et_al(
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Format the data from the `v_dingos_by_20190701_button_a_et_al` version of the data source.

        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        input_file_name = "rxn_set.txt"

        output_file_name = "{timestamp:s}_miscellaneous_v_dingos_by_20190701_button_a_et_al.csv".format(
            timestamp=datetime.now().strftime(
                format="%Y%m%d%H%M%S"
            )
        )

        read_csv(
            filepath_or_buffer=Path(input_directory_path, input_file_name),
            sep="|",
            header=None
        ).rename(
            columns={
                0: "reaction_name",
                1: "reaction_smarts",
                2: "reaction_label",
            }
        ).to_csv(
            path_or_buf=Path(output_directory_path, output_file_name),
            index=False
        )
