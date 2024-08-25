""" The ``data_source.reaction_rule.retro_rules.utility`` package ``formatting`` module. """

from datetime import datetime
from os import PathLike
from pathlib import Path
from typing import Union

from pandas import read_csv


class RetroRulesReactionRuleDatabaseFormattingUtility:
    """ The `RetroRules <https://retrorules.org>`_ chemical reaction rule database formatting utility class. """

    @staticmethod
    def format_v_release(
            version: str,
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Format the data from a `v_release_*` version of the chemical reaction rule database.

        :parameter version: The version of the chemical reaction rule database.
        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        if version == "v_release_rr01_rp2_hs":
            file_name = "retrorules_rr01_rp2_flat_all.csv"

        elif version == "v_release_rr02_rp2_hs":
            file_name = "retrorules_rr02_rp2_flat_all.csv"

        else:
            file_name = "retrorules_rr02_flat_all.tsv"

        read_csv(
            filepath_or_buffer=Path(input_directory_path, file_name),
            sep="\t" if file_name.endswith(".tsv") else ",",
            header=0
        ).to_csv(
            path_or_buf=Path(
                output_directory_path,
                "{timestamp:s}_retro_rules_{version:s}.csv".format(
                    timestamp=datetime.now().strftime(
                        format="%Y%m%d%H%M%S"
                    ),
                    version=version
                )
            ),
            index=False
        )
