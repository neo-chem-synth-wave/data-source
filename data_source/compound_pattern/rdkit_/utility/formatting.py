""" The ``data_source.compound_pattern.rdkit_.utility`` package ``formatting`` module. """

from ast import literal_eval
from datetime import datetime
from os import PathLike
from pathlib import Path
from re import DOTALL, search, sub
from typing import Union

from pandas import DataFrame


class RDKitCompoundPatternDatasetFormattingUtility:
    """ The `RDKit <https://www.rdkit.org>`_ chemical compound pattern dataset formatting utility class. """

    @staticmethod
    def format_v_htl_by_20080307_brenk_r_et_al(
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Format the data from the `v_htl_by_20080307_brenk_r_et_al` version of the dataset.

        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        input_file_name = "brenk.in"

        output_file_name = "{timestamp:s}_rdkit_v_htl_by_20080307_brenk_r_et_al.csv".format(
            timestamp=datetime.now().strftime(
                format="%Y%m%d%H%M%S"
            )
        )

        dataframe_rows = list()

        with open(
            file=Path(input_directory_path, input_file_name)
        ) as source_file_handle:
            source_file_content_string = search(
                pattern=r"\{(.*)\};",
                string=source_file_handle.read(),
                flags=DOTALL
            ).group(1).replace("{", "[").replace("}", "]")

            source_file_content_string = sub(
                pattern=r",\s*\"\"\s*\]",
                repl=", \"\"]",
                string=source_file_content_string
            )

            for compound_pattern_name, compound_pattern_smarts, _, _ in literal_eval(
                node_or_string="[{source_file_content_string:s}]".format(
                    source_file_content_string=source_file_content_string
                )
            ):
                dataframe_rows.append((
                    compound_pattern_name,
                    compound_pattern_smarts,
                    input_file_name,
                ))

        DataFrame(
            data=dataframe_rows,
            columns=[
                "compound_pattern_name",
                "compound_pattern_smarts",
                "file_name",
            ]
        ).to_csv(
            path_or_buf=Path(output_directory_path, output_file_name),
            index=False
        )

    @staticmethod
    def format_v_pains_by_20100204_baell_j_b_and_holloway_g_a(
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Format the data from the `v_pains_by_20100204_baell_j_b_and_holloway_g_a` version of the dataset.

        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        input_file_names = [
            "pains_a.in",
            "pains_b.in",
            "pains_c.in",
        ]

        output_file_name = "{timestamp:s}_rdkit_v_pains_by_20100204_baell_j_b_and_holloway_g_a.csv".format(
            timestamp=datetime.now().strftime(
                format="%Y%m%d%H%M%S"
            )
        )

        dataframe_rows = list()

        for input_file_name in input_file_names:
            with open(
                file=Path(input_directory_path, input_file_name)
            ) as source_file_handle:
                source_file_content_string = search(
                    pattern=r"\{(.*)\};",
                    string=source_file_handle.read(),
                    flags=DOTALL
                ).group(1).replace("{", "[").replace("}", "]")

                source_file_content_string = sub(
                    pattern=r",\s*\"\"\s*\]",
                    repl=", \"\"]",
                    string=source_file_content_string
                )

                for compound_pattern_name, compound_pattern_smarts, _, _ in literal_eval(
                    node_or_string="[{source_file_content_string:s}]".format(
                        source_file_content_string=source_file_content_string
                    )
                ):
                    dataframe_rows.append((
                        compound_pattern_name,
                        compound_pattern_smarts,
                        input_file_name,
                    ))

        DataFrame(
            data=dataframe_rows,
            columns=[
                "compound_pattern_name",
                "compound_pattern_smarts",
                "file_name",
            ]
        ).to_csv(
            path_or_buf=Path(output_directory_path, output_file_name),
            index=False
        )
