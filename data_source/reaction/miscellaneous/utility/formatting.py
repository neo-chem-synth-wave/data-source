""" The ``data_source.reaction.miscellaneous.utility`` package ``formatting`` module. """

from datetime import datetime
from os import PathLike
from pathlib import Path
from typing import Union

from pandas import DataFrame, concat, read_csv

from rdkit.Chem.rdChemReactions import ReactionFromRxnBlock, ReactionToSmiles


class MiscellaneousReactionDataSourceFormattingUtility:
    """ The miscellaneous chemical reaction data source formatting utility class. """

    @staticmethod
    def format_v_20131008_kraut_h_et_al(
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Format the data from the `v_20131008_kraut_h_et_al` version of the chemical reaction data source.

        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        dataframe_rows = list()

        for file_name in [
            "MapTestExamplesV1.0.rdf",
            "MapTestExamplesV1_ICMapRctCpy.rdf",
            "MapTestExamplesV1_ICMap.rdf",
        ]:
            with open(
                file=Path(input_directory_path, file_name)
            ) as file_handle:
                for reaction_rxn_block_without_identifier in file_handle.read().split(
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
                                file_name,
                            ))

        DataFrame(
            data=dataframe_rows,
            columns=[
                "reaction_smiles",
                "file_name",
            ]
        ).to_csv(
            path_or_buf=Path(
                output_directory_path,
                "{timestamp:s}_miscellaneous_v_20131008_kraut_h_et_al.csv".format(
                    timestamp=datetime.now().strftime(
                        format="%Y%m%d%H%M%S"
                    )
                )
            ),
            index=False
        )

    @staticmethod
    def format_v_20161014_wei_j_n_et_al(
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Format the data from the `v_20161014_wei_j_n_et_al` version of the chemical reaction data source.

        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        dataframes = list()

        for file_name in [
            "Wade8_47.ans_smi.txt",
            "Wade8_48.ans_smi.txt",
        ]:
            dataframe = read_csv(
                filepath_or_buffer=Path(input_directory_path, file_name),
                header=None
            ).rename(
                columns={
                    0: "reaction_smiles",
                }
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
                "{timestamp:s}_miscellaneous_v_20161014_wei_j_n_et_al.csv".format(
                    timestamp=datetime.now().strftime(
                        format="%Y%m%d%H%M%S"
                    )
                )
            ),
            index=False
        )

    @staticmethod
    def format_v_20200508_grambow_c_et_al(
            version: str,
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Format the data from a `v_*_20200508_grambow_c_et_al` version of the chemical reaction data source.

        :parameter version: The version of the chemical reaction data source.
        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        if version == "v_20200508_grambow_c_et_al":
            file_names = [
                "b97d3.csv",
                "wb97xd3.csv",
            ]

        else:
            file_names = [
                "b97d3_rad.csv",
                "wb97xd3_rad.csv",
            ]

        dataframes = list()

        for file_name in file_names:
            dataframe = read_csv(
                filepath_or_buffer=Path(input_directory_path, file_name),
                header=0
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
                "{timestamp:s}_miscellaneous_{version:s}.csv".format(
                    timestamp=datetime.now().strftime(
                        format="%Y%m%d%H%M%S"
                    ),
                    version=version
                )
            ),
            index=False
        )

    @staticmethod
    def format_v_golden_dataset_by_20211103_lin_a_et_al(
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Format the data from the `v_golden_dataset_by_20211103_lin_a_et_al` version of the chemical reaction data
        source.

        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        dataframe_rows = list()

        with open(
            file=Path(input_directory_path, "golden_dataset.rdf")
        ) as file_handle:
            for reaction_rxn_block_without_identifier in file_handle.read().split(
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

        DataFrame(
            data=dataframe_rows,
            columns=[
                "reaction_smiles",
            ]
        ).to_csv(
            path_or_buf=Path(
                output_directory_path,
                "{timestamp:s}_miscellaneous_v_golden_dataset_by_20211103_lin_a_et_al.csv".format(
                    timestamp=datetime.now().strftime(
                        format="%Y%m%d%H%M%S"
                    )
                )
            ),
            index=False
        )

    @staticmethod
    def format_v_rdb7_by_20220718_spiekermann_k_et_al(
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Format the data from the `v_rdb7_by_20220718_spiekermann_k_et_al` version of the chemical reaction data source.

        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        dataframes = list()

        for file_name in [
            "b97d3.csv",
            "wb97xd3.csv",
            "ccsdtf12_dz.csv",
            "ccsdtf12_tz.csv",
        ]:
            dataframe = read_csv(
                filepath_or_buffer=Path(input_directory_path, file_name),
                header=0
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
                "{timestamp:s}_miscellaneous_v_rdb7_by_20220718_spiekermann_k_et_al.csv".format(
                    timestamp=datetime.now().strftime(
                        format="%Y%m%d%H%M%S"
                    )
                )
            ),
            index=False
        )
