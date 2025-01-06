""" The ``data_source.reaction.miscellaneous.utility`` package ``formatting`` module. """

from datetime import datetime
from os import PathLike
from pathlib import Path
from typing import Union

from pandas.core.reshape.concat import concat
from pandas.io.parquet import read_parquet
from pandas.io.parsers.readers import DataFrame, read_csv

from rdkit.Chem.rdChemReactions import ReactionFromRxnBlock, ReactionToSmiles


class MiscellaneousReactionDataSourceFormattingUtility:
    """ The miscellaneous chemical reaction data source formatting utility class. """

    @staticmethod
    def format_v_20131008_kraut_h_et_al(
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Format the data from the `v_20131008_kraut_h_et_al` version of the data source.

        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        input_file_names = [
            "MapTestExamplesV1.0.rdf",
            "MapTestExamplesV1_ICMapRctCpy.rdf",
            "MapTestExamplesV1_ICMap.rdf",
        ]

        output_file_name = "{timestamp:s}_miscellaneous_v_20131008_kraut_h_et_al.csv".format(
            timestamp=datetime.now().strftime(
                format="%Y%m%d%H%M%S"
            )
        )

        dataframe_rows = list()

        for input_file_name in input_file_names:
            with open(
                file=Path(input_directory_path, input_file_name)
            ) as input_file_handle:
                # noinspection PyUnresolvedReferences
                for reaction_rxn_block_without_identifier in input_file_handle.read().split(
                    sep="$RXN"
                )[1:]:
                    reaction_rxn = ReactionFromRxnBlock(
                        rxnblock="$RXN{reaction_rxn_block_without_identifier:s}".format(
                            reaction_rxn_block_without_identifier=reaction_rxn_block_without_identifier
                        )
                    )

                    if reaction_rxn is not None:
                        reaction_smiles = ReactionToSmiles(
                            reaction=reaction_rxn
                        )

                        if reaction_smiles is not None:
                            dataframe_rows.append((
                                reaction_smiles,
                                input_file_name,
                            ))

        DataFrame(
            data=dataframe_rows,
            columns=[
                "reaction_smiles",
                "file_name",
            ]
        ).to_csv(
            path_or_buf=Path(output_directory_path, output_file_name),
            index=False
        )

    @staticmethod
    def format_v_20161014_wei_j_n_et_al(
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Format the data from the `v_20161014_wei_j_n_et_al` version of the data source.

        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        input_file_names = [
            "Wade8_47.ans_smi.txt",
            "Wade8_48.ans_smi.txt",
        ]

        output_file_name = "{timestamp:s}_miscellaneous_v_20161014_wei_j_n_et_al.csv".format(
            timestamp=datetime.now().strftime(
                format="%Y%m%d%H%M%S"
            )
        )

        dataframes = list()

        for input_file_name in input_file_names:
            dataframe = read_csv(
                filepath_or_buffer=Path(input_directory_path, input_file_name),
                header=None
            ).rename(
                columns={
                    0: "reaction_smiles",
                }
            )

            dataframe["file_name"] = input_file_name

            dataframes.append(
                dataframe
            )

        concat(
            objs=dataframes
        ).to_csv(
            path_or_buf=Path(output_directory_path, output_file_name),
            index=False
        )

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

        dataframe = read_csv(
            filepath_or_buffer=Path(input_directory_path, input_file_name),
            sep="\t",
            header=0
        ).dropna(
            how="all"
        )

        dataframe["FileName"] = input_file_name

        dataframe.astype(
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

        dataframe = read_csv(
            filepath_or_buffer=Path(input_directory_path, input_file_name),
            sep="|",
            header=None
        )

        dataframe["file_name"] = input_file_name

        dataframe.rename(
            columns={
                0: "reaction_name",
                1: "reaction_smarts",
                2: "reaction_label",
            }
        ).to_csv(
            path_or_buf=Path(output_directory_path, output_file_name),
            index=False
        )

    @staticmethod
    def format_v_20200508_grambow_c_et_al(
            version: str,
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Format the data from a `v_*_20200508_grambow_c_et_al` version of the data source.

        :parameter version: The version of the data source.
        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        if version == "v_20200508_grambow_c_et_al":
            input_file_names = [
                "b97d3.csv",
                "wb97xd3.csv",
            ]

        elif version == "v_add_on_by_20200508_grambow_c_et_al":
            input_file_names = [
                "b97d3_rad.csv",
                "wb97xd3_rad.csv",
            ]

        else:
            raise ValueError(
                "The formatting of the data from the {data_source:s} is not supported.".format(
                    data_source="miscellaneous chemical reaction data source ({version:s})".format(
                        version=version
                    )
                )
            )

        output_file_name = "{timestamp:s}_miscellaneous_{version:s}.csv".format(
            timestamp=datetime.now().strftime(
                format="%Y%m%d%H%M%S"
            ),
            version=version
        )

        dataframes = list()

        for input_file_name in input_file_names:
            dataframe = read_csv(
                filepath_or_buffer=Path(input_directory_path, input_file_name),
                header=0
            )

            dataframe["file_name"] = input_file_name

            dataframes.append(
                dataframe
            )

        concat(
            objs=dataframes
        ).to_csv(
            path_or_buf=Path(output_directory_path, output_file_name),
            index=False
        )

    @staticmethod
    def format_v_golden_dataset_by_20211102_lin_a_et_al(
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Format the data from the `v_golden_dataset_by_20211102_lin_a_et_al` version of the data source.

        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        input_file_name = "golden_dataset.rdf"

        output_file_name = "{timestamp:s}_miscellaneous_v_golden_dataset_by_20211102_lin_a_et_al.csv".format(
            timestamp=datetime.now().strftime(
                format="%Y%m%d%H%M%S"
            )
        )

        dataframe_rows = list()

        with open(
            file=Path(input_directory_path, input_file_name)
        ) as input_file_handle:
            for reaction_rxn_block_without_identifier in input_file_handle.read().split(
                sep="$RXN"
            )[1:]:
                reaction_rxn = ReactionFromRxnBlock(
                    rxnblock="$RXN{reaction_rxn_block_without_identifier:s}".format(
                        reaction_rxn_block_without_identifier=reaction_rxn_block_without_identifier
                    )
                )

                if reaction_rxn is not None:
                    reaction_smiles = ReactionToSmiles(
                        reaction=reaction_rxn
                    )

                    if reaction_smiles is not None:
                        dataframe_rows.append(
                            reaction_smiles
                        )

        dataframe = DataFrame(
            data=dataframe_rows,
            columns=[
                "reaction_smiles",
            ]
        )

        dataframe["file_name"] = input_file_name

        dataframe.to_csv(
            path_or_buf=Path(output_directory_path, output_file_name),
            index=False
        )

    @staticmethod
    def format_v_rdb7_by_20220718_spiekermann_k_et_al(
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Format the data from the `v_rdb7_by_20220718_spiekermann_k_et_al` version of the data source.

        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        input_file_names = [
            "b97d3.csv",
            "wb97xd3.csv",
            "ccsdtf12_dz.csv",
            "ccsdtf12_tz.csv",
        ]

        output_file_name = "{timestamp:s}_miscellaneous_v_rdb7_by_20220718_spiekermann_k_et_al.csv".format(
            timestamp=datetime.now().strftime(
                format="%Y%m%d%H%M%S"
            )
        )

        dataframes = list()

        for input_file_name in input_file_names:
            dataframe = read_csv(
                filepath_or_buffer=Path(input_directory_path, input_file_name),
                header=0
            )

            dataframe["file_name"] = input_file_name

            dataframes.append(
                dataframe
            )

        concat(
            objs=dataframes
        ).to_csv(
            path_or_buf=Path(output_directory_path, output_file_name),
            index=False
        )

    @staticmethod
    def format_v_orderly(
            version: str,
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Format the data from a `v_orderly_*` version of the database.

        :parameter version: The version of the chemical reaction database.
        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        if version == "v_orderly_condition_by_20240422_wigh_d_s_et_al":
            input_file_names = [
                "orderly_condition_train.parquet",
                "orderly_condition_test.parquet",
                "orderly_condition_with_rare_train.parquet",
                "orderly_condition_with_rare_test.parquet",
            ]

        elif version == "v_orderly_forward_by_20240422_wigh_d_s_et_al":
            input_file_names = [
                "orderly_forward_train.parquet",
                "orderly_forward_test.parquet",
            ]

        elif version == "v_orderly_retro_by_20240422_wigh_d_s_et_al":
            input_file_names = [
                "orderly_retro_train.parquet",
                "orderly_retro_test.parquet",
            ]

        else:
            raise ValueError(
                "The formatting of the data from the {data_source:s} is not supported.".format(
                    data_source="miscellaneous chemical reaction data source ({version:s})".format(
                        version=version
                    )
                )
            )

        output_file_name = "{timestamp:s}_miscellaneous_{version:s}.csv".format(
            timestamp=datetime.now().strftime(
                format="%Y%m%d%H%M%S"
            ),
            version=version
        )

        dataframes = list()

        for input_file_name in input_file_names:
            dataframe = read_parquet(
                path=Path(input_directory_path, input_file_name)
            )

            dataframe["file_name"] = input_file_name

            dataframes.append(
                dataframe
            )

        concat(
            objs=dataframes
        ).to_csv(
            path_or_buf=Path(output_directory_path, output_file_name),
            index=False
        )
