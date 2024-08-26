""" The ``data_source.reaction.uspto.utility`` package ``formatting`` module. """

from datetime import datetime
from os import PathLike, walk
from pathlib import Path
from pickle import load
from typing import List, Optional, Tuple, Union

from pandas import DataFrame, concat, read_csv

from pqdm.processes import pqdm

from xml.etree import ElementTree


class USPTOReactionDatasetFormattingUtility:
    """
    The `United States Patent and Trademark Office (USPTO) <https://www.repository.cam.ac.uk/handle/1810/244727>`_
    chemical reaction dataset formatting utility class.
    """

    @staticmethod
    def format_v_1976_to_2013_rsmi_by_20121009_lowe_d_m(
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Format the data from the `v_1976_to_2013_rsmi_by_20121009_lowe_d_m` version of the chemical reaction dataset.

        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        dataframes = list()

        for file_name in [
            "1976-2013_USPTOgrants_reactionSmiles_feb2014filters.rsmi",
            "2001-2013_USPTOapplications_reactionSmiles_feb2014filters.rsmi",
        ]:
            dataframe = read_csv(
                filepath_or_buffer=Path(input_directory_path, file_name),
                sep="\t",
                header=None,
                low_memory=False
            )

            dataframe["FileName"] = file_name

            dataframes.append(
                dataframe
            )

        concat(
            objs=dataframes
        ).rename(
            columns={
                0: "ReactionSmiles",
                1: "PatentNumber",
                2: "ParagraphNum",
            }
        ).to_csv(
            path_or_buf=Path(
                output_directory_path,
                "{timestamp:s}_uspto_v_1976_to_2013_rsmi_by_20121009_lowe_d_m.csv".format(
                    timestamp=datetime.now().strftime(
                        format="%Y%m%d%H%M%S"
                    )
                )
            ),
            index=False
        )

    @staticmethod
    def format_v_50k_by_20141226_schneider_n_et_al(
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Format the data from the `v_50k_by_20141226_schneider_n_et_al` version of the chemical reaction dataset.

        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        dataframes = list()

        with open(
            file=Path(input_directory_path, "names_rTypes_classes_superclasses_training_test_set_patent_data.pkl"),
            mode="rb"
        ) as file_handle:
            reaction_clas_id_to_name = load(
                file=file_handle
            )

        for file_name in [
            "training_test_set_patent_data.pkl",
            "unclassified_reactions_patent_data.pkl",
        ]:
            dataframe_rows = list()

            with open(
                file=Path(input_directory_path, file_name),
                mode="rb"
            ) as file_handle:
                while True:
                    try:
                        dataframe_rows.append(
                            load(
                                file=file_handle
                            )
                        )

                    except EOFError:
                        break

            dataframe = DataFrame(
                data=dataframe_rows,
                columns=[
                    "reaction_smiles",
                    "patent_number",
                    "reaction_class_id",
                ]
            )

            dataframe["reaction_class_name"] = dataframe["reaction_class_id"].map(
                arg=reaction_clas_id_to_name
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
                "{timestamp:s}_uspto_v_50k_by_20141226_schneider_n_et_al.csv".format(
                    timestamp=datetime.now().strftime(
                        format="%Y%m%d%H%M%S"
                    )
                )
            ),
            index=False
        )

    @staticmethod
    def format_v_50k_by_20161122_schneider_n_et_al(
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Format the data from the `v_50k_by_20161122_schneider_n_et_al` version of the chemical reaction dataset.

        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        dataframes = list()

        for file_name in [
            "dataSetA.csv",
            "dataSetB.csv",
        ]:
            dataframe = read_csv(
                filepath_or_buffer=Path(input_directory_path, file_name),
                sep=",",
                header=0
            )

            dataframe["file_Name"] = file_name

            dataframes.append(
                dataframe
            )

        concat(
            objs=dataframes
        ).to_csv(
            path_or_buf=Path(
                output_directory_path,
                "{timestamp:s}_uspto_v_50k_by_20161122_schneider_n_et_al.csv".format(
                    timestamp=datetime.now().strftime(
                        format="%Y%m%d%H%M%S"
                    )
                )
            ),
            index=False
        )

    @staticmethod
    def format_v_15k_by_20170418_coley_c_w_et_al(
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Format the data from the `v_15k_by_20170418_coley_c_w_et_al` version of the chemical reaction dataset.

        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        dataframes = list()

        for file_name in [
            "train.txt",
            "valid.txt",
            "test.txt",
        ]:
            dataframe = read_csv(
                filepath_or_buffer=Path(input_directory_path, file_name),
                sep="\t",
                header=None
            )

            dataframe["file_name"] = file_name

            dataframes.append(
                dataframe
            )

        concat(
            objs=dataframes
        ).rename(
            columns={
                0: "reaction_smiles",
            }
        ).to_csv(
            path_or_buf=Path(
                output_directory_path,
                "{timestamp:s}_uspto_v_15k_by_20170418_coley_c_w_et_al.csv".format(
                    timestamp=datetime.now().strftime(
                        format="%Y%m%d%H%M%S"
                    )
                )
            ),
            index=False
        )

    @staticmethod
    def _parse_v_1976_to_2016_cml_by_20121009_lowe_d_m_file(
            file_path: Union[str, PathLike[str]]
    ) -> List[Tuple[Optional[Union[int, str]], ...]]:
        """
        Parse a file from the `v_1976_to_2016_cml_by_20121009_lowe_d_m` version of the chemical reaction dataset.

        :parameter file_path: The path to the file that should be parsed.

        :returns: The chemical reaction data.
        """

        reaction_data = list()

        for reaction_xml_element in ElementTree.parse(
            source=file_path
        ).getroot():
            document_id = reaction_xml_element.find(
                path="{xml_element_name_prefix:s}{xml_element_name:s}".format(
                    xml_element_name_prefix="{http://bitbucket.org/dan2097}source/{http://bitbucket.org/dan2097}",
                    xml_element_name="documentId"
                )
            )

            paragraph_number = reaction_xml_element.find(
                path="{xml_element_name_prefix:s}{xml_element_name:s}".format(
                    xml_element_name_prefix="{http://bitbucket.org/dan2097}source/{http://bitbucket.org/dan2097}",
                    xml_element_name="paragraphNum"
                )
            )

            heading_text = reaction_xml_element.find(
                path="{xml_element_name_prefix:s}{xml_element_name:s}".format(
                    xml_element_name_prefix="{http://bitbucket.org/dan2097}source/{http://bitbucket.org/dan2097}",
                    xml_element_name="headingText"
                )
            )

            paragraph_text = reaction_xml_element.find(
                path="{xml_element_name_prefix:s}{xml_element_name:s}".format(
                    xml_element_name_prefix="{http://bitbucket.org/dan2097}source/{http://bitbucket.org/dan2097}",
                    xml_element_name="paragraphText"
                )
            )

            reaction_smiles = reaction_xml_element.find(
                path="{xml_element_name_prefix:s}{xml_element_name:s}".format(
                    xml_element_name_prefix="{http://bitbucket.org/dan2097}",
                    xml_element_name="reactionSmiles"
                )
            )

            reaction_data.append((
                int(file_path.split(
                    sep="/"
                )[-2]),
                document_id.text if document_id is not None else None,
                paragraph_number.text if paragraph_number is not None else None,
                heading_text.text if heading_text is not None else None,
                paragraph_text.text if paragraph_text is not None else None,
                reaction_smiles.text if reaction_smiles is not None else None,
            ))

        return reaction_data

    @staticmethod
    def format_v_1976_to_2016_cml_by_20121009_lowe_d_m(
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]],
            number_of_processes: int = 1
    ) -> None:
        """
        Format the data from the `v_1976_to_2016_cml_by_20121009_lowe_d_m` version of the chemical reaction dataset.

        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        :parameter number_of_processes: The number of processes.
        """

        file_paths = list()

        for directory_name in [
            "grants",
            "applications",
        ]:
            for directory_path, _, file_names in walk(
                top=Path(input_directory_path, directory_name)
            ):
                for file_name in file_names:
                    if file_name.endswith(".xml"):
                        file_paths.append(
                            Path(directory_path, file_name).resolve().as_posix()
                        )

        dataframe_rows = list()

        for reaction_data in pqdm(
            array=file_paths,
            function=USPTOReactionDatasetFormattingUtility._parse_v_1976_to_2016_cml_by_20121009_lowe_d_m_file,
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
                "year",
                "document_id",
                "paragraph_number",
                "heading_text",
                "paragraph_text",
                "reaction_smiles",
            ]
        ).to_csv(
            path_or_buf=Path(
                output_directory_path,
                "{timestamp:s}_v_1976_to_2016_cml_by_20121009_lowe_d_m.csv".format(
                    timestamp=datetime.now().strftime(
                        format="%Y%m%d%H%M%S"
                    )
                )
            ),
            index=False
        )

    @staticmethod
    def format_v_1976_to_2016_rsmi_by_20121009_lowe_d_m(
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Format the data from the `v_1976_to_2016_rsmi_by_20121009_lowe_d_m` version of the chemical reaction dataset.

        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        dataframes = list()

        for file_name in [
            "1976_Sep2016_USPTOgrants_smiles.rsmi",
            "2001_Sep2016_USPTOapplications_smiles.rsmi",
        ]:
            dataframe = read_csv(
                filepath_or_buffer=Path(input_directory_path, file_name),
                sep="\t",
                header=0,
                low_memory=False
            )

            dataframe["FileName"] = file_name

            dataframes.append(
                dataframe
            )

        concat(
            objs=dataframes
        ).to_csv(
            path_or_buf=Path(
                output_directory_path,
                "{timestamp:s}_v_1976_to_2016_rsmi_by_20121009_lowe_d_m.csv".format(
                    timestamp=datetime.now().strftime(
                        format="%Y%m%d%H%M%S"
                    )
                )
            ),
            index=False
        )

    @staticmethod
    def format_v_50k_by_20170905_liu_b_et_al(
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Format the data from the `v_50k_by_20170905_liu_b_et_al` version of the chemical reaction dataset.

        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        dataframes = list()

        for file_name_prefix in [
            "train",
            "valid",
            "test",
        ]:
            dataframe = concat(
                objs=[
                    read_csv(
                        filepath_or_buffer=Path(
                            input_directory_path,
                            "{file_name_prefix:s}_targets".format(
                                file_name_prefix=file_name_prefix
                            )
                        ),
                        header=None
                    ),
                    read_csv(
                        filepath_or_buffer=Path(
                            input_directory_path,
                            "{file_name_prefix:s}_sources".format(
                                file_name_prefix=file_name_prefix
                            )
                        ),
                        header=None
                    ),
                ],
                axis=1
            )

            dataframe["file_name_prefix"] = file_name_prefix

            dataframes.append(
                dataframe
            )

        concat(
            objs=dataframes
        ).rename(
            columns={
                0: "targets",
                1: "sources",
            }
        ).to_csv(
            path_or_buf=Path(
                output_directory_path,
                "{timestamp:s}_uspto_v_50k_by_20170905_liu_b_et_al.csv".format(
                    timestamp=datetime.now().strftime(
                        format="%Y%m%d%H%M%S"
                    )
                )
            ),
            index=False
        )

    @staticmethod
    def format_v_50k_by_20171116_coley_c_w_et_al(
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Format the data from the `v_50k_by_20171116_coley_c_w_et_al` version of the chemical reaction dataset.

        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        read_csv(
            filepath_or_buffer=Path(input_directory_path, "data_processed.csv"),
            header=0,
            index_col=0
        ).to_csv(
            path_or_buf=Path(
                output_directory_path,
                "{timestamp:s}_uspto_v_50k_by_20171116_coley_c_w_et_al.csv".format(
                    timestamp=datetime.now().strftime(
                        format="%Y%m%d%H%M%S"
                    )
                )
            ),
            index=False
        )

    @staticmethod
    def format_v_480k_or_mit_by_20171204_jin_w_et_al(
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Format the data from the `v_480k_or_mit_by_20171204_jin_w_et_al` version of the chemical reaction dataset.

        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        dataframes = list()

        for file_name in [
            "train.txt",
            "valid.txt",
            "test.txt",
        ]:
            dataframe = read_csv(
                filepath_or_buffer=Path(input_directory_path, file_name),
                sep="\t",
                header=None
            )

            dataframe["file_name"] = file_name

            dataframes.append(
                dataframe
            )

        concat(
            objs=dataframes
        ).rename(
            columns={
                0: "reaction_smiles",
            }
        ).to_csv(
            path_or_buf=Path(
                output_directory_path,
                "{timestamp:s}_uspto_v_480k_or_mit_by_20171229_jin_w_et_al.csv".format(
                    timestamp=datetime.now().strftime(
                        format="%Y%m%d%H%M%S"
                    )
                )
            ),
            index=False
        )

    @staticmethod
    def format_v_480k_or_mit_by_20180622_schwaller_p_et_al(
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Format the data from the `v_480k_or_mit_by_20180622_schwaller_p_et_al` version of the chemical reaction dataset.

        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        dataframes = list()

        for file_name in [
            "Jin_USPTO_1product_train.txt",
            "Jin_USPTO_1product_valid.txt",
            "Jin_USPTO_1product_test.txt",
        ]:
            dataframe = read_csv(
                filepath_or_buffer=Path(input_directory_path, file_name),
                sep="\t",
                header=None,
                skiprows=[0, ]
            )

            dataframe["file_name"] = file_name

            dataframes.append(
                dataframe
            )

        concat(
            objs=dataframes
        ).rename(
            columns={
                0: "reaction_smiles",
            }
        ).to_csv(
            path_or_buf=Path(
                output_directory_path,
                "{timestamp:s}_uspto_v_480k_or_mit_by_20180622_schwaller_p_et_al.csv".format(
                    timestamp=datetime.now().strftime(
                        format="%Y%m%d%H%M%S"
                    )
                )
            ),
            index=False
        )

    @staticmethod
    def format_v_stereo_by_20180622_schwaller_p_et_al(
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Format the data from the `v_stereo_by_20180622_schwaller_p_et_al` version of the chemical reaction dataset.

        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        dataframes = list()

        for file_name in [
            "US_patents_1976-Sep2016_1product_reactions_train.csv",
            "US_patents_1976-Sep2016_1product_reactions_valid.csv",
            "US_patents_1976-Sep2016_1product_reactions_test.csv",
        ]:
            dataframe = read_csv(
                filepath_or_buffer=Path(input_directory_path, file_name),
                sep="\t",
                header=2,
                low_memory=False
            )

            dataframe["FileName"] = file_name

            dataframes.append(
                dataframe
            )

        concat(
            objs=dataframes
        ).rename(
            columns={
                0: "reaction_smiles",
            }
        ).to_csv(
            path_or_buf=Path(
                output_directory_path,
                "{timestamp:s}_uspto_v_stereo_by_20180622_schwaller_p_et_al.csv".format(
                    timestamp=datetime.now().strftime(
                        format="%Y%m%d%H%M%S"
                    )
                )
            ),
            index=False
        )

    @staticmethod
    def format_v_lef_by_20181221_bradshaw_j_et_al(
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Format the data from the `v_lef_by_20181221_bradshaw_j_et_al` version of the chemical reaction dataset.

        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        dataframes = list()

        for file_name in [
            "filtered_train.txt",
            "filtered_valid.txt",
            "filtered_test.txt",
        ]:
            dataframe = read_csv(
                filepath_or_buffer=Path(input_directory_path, file_name),
                header=None
            )

            dataframe["file_name"] = file_name

            dataframes.append(
                dataframe
            )

        concat(
            objs=dataframes
        ).rename(
            columns={
                0: "reaction_smiles",
            }
        ).to_csv(
            path_or_buf=Path(
                output_directory_path,
                "{timestamp:s}_uspto_v_lef_by_20181221_bradshaw_j_et_al.csv".format(
                    timestamp=datetime.now().strftime(
                        format="%Y%m%d%H%M%S"
                    )
                )
            ),
            index=False
        )

    @staticmethod
    def format_v_1k_tpl_by_20210128_schwaller_p_et_al(
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Format the data from the `v_1k_tpl_by_20210128_schwaller_p_et_al` version of the chemical reaction dataset.

        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        dataframes = list()

        for file_name in [
            "uspto_1k_TPL_test.tsv",
            "uspto_1k_TPL_train_valid.tsv",
        ]:
            dataframe = read_csv(
                filepath_or_buffer=Path(input_directory_path, file_name),
                sep="\t",
                header=0,
                index_col=0
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
                "{timestamp:s}_uspto_v_1k_tpl_by_20210705_schwaller_p_et_al.csv".format(
                    timestamp=datetime.now().strftime(
                        format="%Y%m%d%H%M%S"
                    )
                )
            ),
            index=False
        )

    @staticmethod
    def format_v_1976_to_2016_remapped_by_20210407_schwaller_p_et_al(
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Format the data from the `v_1976_to_2016_by_20210407_schwaller_p_et_al` version of the chemical reaction
        dataset.

        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        dataframes = list()

        for file_name in [
            "1976_Sep2016_USPTOgrants_smiles_mapped.tsv",
            "2001_Sep2016_USPTOapplications_smiles_mapped.tsv",
        ]:
            dataframe = read_csv(
                filepath_or_buffer=Path(input_directory_path, file_name),
                sep="\t",
                header=0,
                index_col=0
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
                "{timestamp:s}_uspto_v_1976_to_2016_by_20210407_schwaller_p_et_al.csv".format(
                    timestamp=datetime.now().strftime(
                        format="%Y%m%d%H%M%S"
                    )
                )
            ),
            index=False
        )

    @staticmethod
    def format_v_chen_s_et_al(
            version: str,
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Format the data from a `v_*_chen_s_et_al` version of the chemical reaction dataset.

        :parameter version: The version of the chemical reaction dataset.
        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        if version == "v_1976_to_2016_remapped_by_20240313_chen_s_et_al":
            file_name = "remapped_USPTO_FULL.csv"

        elif version == "v_50k_remapped_by_20240313_chen_s_et_al":
            file_name = "remapped_USPTO_50K.csv"

        else:
            file_name = "mech-USPTO-31k.csv"

        read_csv(
            filepath_or_buffer=Path(input_directory_path, file_name),
            header=0
        ).to_csv(
            path_or_buf=Path(
                output_directory_path,
                "{timestamp:s}_uspto_{version:s}.csv".format(
                    timestamp=datetime.now().strftime(
                        format="%Y%m%d%H%M%S"
                    ),
                    version=version
                )
            ),
            index=False
        )
