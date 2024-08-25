""" The ``data_source.reaction.ord.utility`` package ``formatting`` module. """

from datetime import datetime
from os import PathLike, walk
from pathlib import Path
from typing import List, Optional, Tuple, Union

from ord_schema.message_helpers import get_reaction_smiles, load_message
from ord_schema.proto.dataset_pb2 import Dataset

from pandas import DataFrame, concat, read_parquet

from pqdm.processes import pqdm

from rdkit.RDLogger import DisableLog


class OpenReactionDatabaseFormattingUtility:
    """ The `Open Reaction Database (ORD) <https://open-reaction-database.org>`_ formatting utility class. """

    @staticmethod
    def _parse_v_release_file(
            file_path: Union[str, PathLike[str]]
    ) -> List[Tuple[Optional[str], ...]]:
        """
        Parse a file from a `v_release_*` version of the chemical reaction database.

        :parameter file_path: The path to the file that should be parsed.

        :returns: The chemical reaction data.
        """

        reaction_data = list()

        try:
            dataset_protocol_buffer_message = load_message(
                filename=file_path,
                message_type=Dataset
            )

            for reaction_protocol_buffer_message in dataset_protocol_buffer_message.reactions:
                try:
                    reaction_data.append((
                        dataset_protocol_buffer_message.dataset_id,
                        reaction_protocol_buffer_message.reaction_id,
                        get_reaction_smiles(
                            message=reaction_protocol_buffer_message,
                            generate_if_missing=True,
                            canonical=False
                        ),
                    ))

                except ValueError:
                    continue

            return reaction_data

        except ValueError:
            return reaction_data

    @staticmethod
    def format_v_release(
            version: str,
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]],
            number_of_processes: int = 1
    ) -> None:
        """
        Format the data from a `v_release_*` version of the chemical reaction database.

        :parameter version: The version of the chemical reaction database.
        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        :parameter number_of_processes: The number of processes.
        """

        if version == "v_release_0_1_0":
            directory_name = "ord-data-0.1.0"

        else:
            directory_name = "ord-data-main"

        file_paths = list()

        for directory_path, _, file_names in walk(
            top=Path(input_directory_path, directory_name, "data")
        ):
            for file_name in file_names:
                if file_name.endswith(".pb.gz"):
                    file_paths.append(
                        Path(directory_path, file_name).resolve().as_posix()
                    )

        DisableLog(
            spec="rdApp.*"
        )

        dataframe_rows = list()

        for reaction_data in pqdm(
            array=file_paths,
            function=OpenReactionDatabaseFormattingUtility._parse_v_release_file,
            n_jobs=number_of_processes,
            desc="Parsing the files",
            total=len(file_paths),
            ncols=150
        ):
            dataframe_rows.extend(
                reaction_data
            )

        DataFrame(
            data=dataframe_rows,
            columns=[
                "dataset_id",
                "reaction_id",
                "reaction_smiles",
            ]
        ).to_csv(
            path_or_buf=Path(
                output_directory_path,
                "{timestamp:s}_ord_{version:s}.csv".format(
                    timestamp=datetime.now().strftime(
                        format="%Y%m%d%H%M%S"
                    ),
                    version=version
                )
            ),
            index=False
        )

    @staticmethod
    def format_v_orderly(
            version: str,
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Format the data from a `v_orderly_*` version of the chemical reaction database.

        :parameter version: The version of the chemical reaction database.
        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        if version == "v_orderly_condition_by_20240422_wigh_d_s_et_al":
            file_names = [
                "orderly_condition_train.parquet",
                "orderly_condition_test.parquet",
                "orderly_condition_with_rare_train.parquet",
                "orderly_condition_with_rare_test.parquet",
            ]

        elif version == "v_orderly_forward_by_20240422_wigh_d_s_et_al":
            file_names = [
                "orderly_forward_train.parquet",
                "orderly_forward_test.parquet",
            ]

        else:
            file_names = [
                "orderly_retro_train.parquet",
                "orderly_retro_test.parquet",
            ]

        dataframes = list()

        for file_name in file_names:
            dataframe = read_parquet(
                path=Path(input_directory_path, file_name)
            )

            dataframe["file_name"] = file_name

            dataframes.append(
                dataframe
            )

        concat(
            objs=dataframes
        ).to_csv(
            path_or_buf=Path(
                output_directory_path,
                "{timestamp:s}_ord_{version:s}.csv".format(
                    timestamp=datetime.now().strftime(
                        format="%Y%m%d%H%M%S"
                    ),
                    version=version
                )
            ),
            index=False
        )
