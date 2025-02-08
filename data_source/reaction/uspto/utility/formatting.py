""" The ``data_source.reaction.uspto.utility`` package ``formatting`` module. """

from datetime import datetime
from os import PathLike, walk
from pathlib import Path
from pickle import load
from typing import List, Optional, Tuple, Union

from pandas.core.reshape.concat import concat
from pandas.io.parsers.readers import DataFrame, read_csv

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
        Format the data from the `v_1976_to_2013_rsmi_by_20121009_lowe_d_m` version of the dataset.

        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        input_file_names = [
            "1976-2013_USPTOgrants_reactionSmiles_feb2014filters.rsmi",
            "2001-2013_USPTOapplications_reactionSmiles_feb2014filters.rsmi",
        ]

        output_file_name = "{timestamp:s}_uspto_v_1976_to_2013_rsmi_by_20121009_lowe_d_m.csv".format(
            timestamp=datetime.now().strftime(
                format="%Y%m%d%H%M%S"
            )
        )

        dataframes = list()

        for input_file_name in input_file_names:
            dataframe = read_csv(
                filepath_or_buffer=Path(input_directory_path, input_file_name),
                sep="\t",
                header=None,
                low_memory=False
            )

            dataframe["FileName"] = input_file_name

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
            path_or_buf=Path(output_directory_path, output_file_name),
            index=False
        )

    @staticmethod
    def format_v_50k_by_20141226_schneider_n_et_al(
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Format the data from the `v_50k_by_20141226_schneider_n_et_al` version of the dataset.

        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        input_file_names = [
            "training_test_set_patent_data.pkl",
            "unclassified_reactions_patent_data.pkl",
            "names_rTypes_classes_superclasses_training_test_set_patent_data.pkl",
        ]

        output_file_name = "{timestamp:s}_uspto_v_50k_by_20141226_schneider_n_et_al.csv".format(
            timestamp=datetime.now().strftime(
                format="%Y%m%d%H%M%S"
            )
        )

        dataframes = list()

        with open(
            file=Path(input_directory_path, input_file_names[-1]),
            mode="rb"
        ) as input_file_handle:
            reaction_clas_id_to_name = load(
                file=input_file_handle
            )

        for input_file_name in input_file_names[0:-1]:
            dataframe_rows = list()

            with open(
                file=Path(input_directory_path, input_file_name),
                mode="rb"
            ) as input_file_handle:
                while True:
                    try:
                        dataframe_rows.append(
                            load(
                                file=input_file_handle
                            )
                        )

                    except:
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
    def format_v_50k_by_20161122_schneider_n_et_al(
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Format the data from the `v_50k_by_20161122_schneider_n_et_al` version of the dataset.

        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        input_file_names = [
            "dataSetA.csv",
            "dataSetB.csv",
        ]

        output_file_name = "{timestamp:s}_uspto_v_50k_by_20161122_schneider_n_et_al.csv".format(
            timestamp=datetime.now().strftime(
                format="%Y%m%d%H%M%S"
            )
        )

        dataframes = list()

        for input_file_name in input_file_names:
            dataframe = read_csv(
                filepath_or_buffer=Path(input_directory_path, input_file_name),
                sep=",",
                header=0
            )

            dataframe["file_Name"] = input_file_name

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
    def format_v_15k_by_20170418_coley_c_w_et_al(
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Format the data from the `v_15k_by_20170418_coley_c_w_et_al` version of the dataset.

        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        input_file_names = [
            "train.txt",
            "valid.txt",
            "test.txt",
        ]

        output_file_name = "{timestamp:s}_uspto_v_15k_by_20170418_coley_c_w_et_al.csv".format(
            timestamp=datetime.now().strftime(
                format="%Y%m%d%H%M%S"
            )
        )

        dataframes = list()

        for input_file_name in input_file_names:
            dataframe = read_csv(
                filepath_or_buffer=Path(input_directory_path, input_file_name),
                sep="\t",
                header=None
            )

            dataframe["file_name"] = input_file_name

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
            path_or_buf=Path(output_directory_path, output_file_name),
            index=False
        )

    @staticmethod
    def _parse_v_1976_to_2016_cml_by_20121009_lowe_d_m_file(
            input_file_path: Union[str, PathLike[str]]
    ) -> List[Tuple[Optional[Union[int, str]], ...]]:
        """
        Parse a file from the `v_1976_to_2016_cml_by_20121009_lowe_d_m` version of the dataset.

        :parameter input_file_path: The path to the input file.

        :returns: The parsed input file.
        """

        parsed_input_file = list()

        for xml_element in ElementTree.parse(
            source=input_file_path
        ).getroot():
            document_id = xml_element.find(
                path="{xml_element_name_prefix:s}{xml_element_name:s}".format(
                    xml_element_name_prefix="{http://bitbucket.org/dan2097}source/{http://bitbucket.org/dan2097}",
                    xml_element_name="documentId"
                )
            )

            paragraph_number = xml_element.find(
                path="{xml_element_name_prefix:s}{xml_element_name:s}".format(
                    xml_element_name_prefix="{http://bitbucket.org/dan2097}source/{http://bitbucket.org/dan2097}",
                    xml_element_name="paragraphNum"
                )
            )

            heading_text = xml_element.find(
                path="{xml_element_name_prefix:s}{xml_element_name:s}".format(
                    xml_element_name_prefix="{http://bitbucket.org/dan2097}source/{http://bitbucket.org/dan2097}",
                    xml_element_name="headingText"
                )
            )

            paragraph_text = xml_element.find(
                path="{xml_element_name_prefix:s}{xml_element_name:s}".format(
                    xml_element_name_prefix="{http://bitbucket.org/dan2097}source/{http://bitbucket.org/dan2097}",
                    xml_element_name="paragraphText"
                )
            )

            reaction_smiles = xml_element.find(
                path="{xml_element_name_prefix:s}{xml_element_name:s}".format(
                    xml_element_name_prefix="{http://bitbucket.org/dan2097}",
                    xml_element_name="reactionSmiles"
                )
            )

            parsed_input_file.append((
                int(input_file_path.split(
                    sep="/"
                )[-2]),
                document_id.text if document_id is not None else None,
                paragraph_number.text if paragraph_number is not None else None,
                heading_text.text if heading_text is not None else None,
                paragraph_text.text if paragraph_text is not None else None,
                reaction_smiles.text if reaction_smiles is not None else None,
                input_file_path.split(
                    sep="/"
                )[-1]
            ))

        return parsed_input_file

    @staticmethod
    def format_v_1976_to_2016_by_20121009_lowe_d_m(
            version: str,
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]],
            number_of_processes: int = 1
    ) -> None:
        """
        Format the data from a `v_1976_to_2016_*_by_20121009_lowe_d_m` version of the dataset.

        :parameter version: The version of the dataset.
        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        :parameter number_of_processes: The number of processes.
        """

        if version == "v_1976_to_2016_cml_by_20121009_lowe_d_m":
            input_directory_names = [
                "grants",
                "applications",
            ]

            input_file_paths = list()

            for input_directory_name in input_directory_names:
                for directory_path, _, file_names in walk(
                    top=Path(input_directory_path, input_directory_name)
                ):
                    for file_name in file_names:
                        if file_name.endswith(".xml"):
                            input_file_paths.append(
                                Path(directory_path, file_name).resolve().as_posix()
                            )

            dataframe_rows = list()

            for parsed_input_file in pqdm(
                array=input_file_paths,
                function=USPTOReactionDatasetFormattingUtility._parse_v_1976_to_2016_cml_by_20121009_lowe_d_m_file,
                n_jobs=number_of_processes,
                desc="Parsing the files",
                total=len(input_file_paths),
                ncols=150
            ):
                dataframe_rows.extend(
                    parsed_input_file
                )

            dataframe = DataFrame(
                data=dataframe_rows,
                columns=[
                    "year",
                    "document_id",
                    "paragraph_number",
                    "heading_text",
                    "paragraph_text",
                    "reaction_smiles",
                    "file_name",
                ]
            )

        elif version == "v_1976_to_2016_rsmi_by_20121009_lowe_d_m":
            input_file_names = [
                "1976_Sep2016_USPTOgrants_smiles.rsmi",
                "2001_Sep2016_USPTOapplications_smiles.rsmi",
            ]

            dataframes = list()

            for input_file_name in input_file_names:
                dataframe = read_csv(
                    filepath_or_buffer=Path(input_directory_path, input_file_name),
                    sep="\t",
                    header=0,
                    low_memory=False
                )

                dataframe["FileName"] = input_file_name

                dataframes.append(
                    dataframe
                )

            dataframe = concat(
                objs=dataframes
            )

        else:
            raise ValueError(
                "The formatting of the data from the {data_source:s} is not supported.".format(
                    data_source="USPTO chemical reaction dataset ({version:s})".format(
                        version=version
                    )
                )
            )

        output_file_name = "{timestamp:s}_uspto_{version:s}.csv".format(
            timestamp=datetime.now().strftime(
                format="%Y%m%d%H%M%S"
            ),
            version=version
        )

        dataframe.to_csv(
            path_or_buf=Path(output_directory_path, output_file_name),
            index=False
        )

    @staticmethod
    def format_v_50k_by_20170905_liu_b_et_al(
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Format the data from the `v_50k_by_20170905_liu_b_et_al` version of the dataset.

        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        input_file_name_prefixes = [
            "train",
            "valid",
            "test",
        ]

        output_file_name = "{timestamp:s}_uspto_v_50k_by_20170905_liu_b_et_al.csv".format(
            timestamp=datetime.now().strftime(
                format="%Y%m%d%H%M%S"
            )
        )

        dataframes = list()

        for input_file_name_prefix in input_file_name_prefixes:
            dataframe = concat(
                objs=[
                    read_csv(
                        filepath_or_buffer=Path(
                            input_directory_path,
                            "{input_file_name_prefix:s}_targets".format(
                                input_file_name_prefix=input_file_name_prefix
                            )
                        ),
                        header=None
                    ),
                    read_csv(
                        filepath_or_buffer=Path(
                            input_directory_path,
                            "{input_file_name_prefix:s}_sources".format(
                                input_file_name_prefix=input_file_name_prefix
                            )
                        ),
                        header=None
                    ),
                ],
                axis=1
            )

            dataframe["file_name_prefix"] = input_file_name_prefix

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
            path_or_buf=Path(output_directory_path, output_file_name),
            index=False
        )

    @staticmethod
    def format_v_50k_by_20171116_coley_c_w_et_al(
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Format the data from the `v_50k_by_20171116_coley_c_w_et_al` version of the dataset.

        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        input_file_name = "data_processed.csv"

        output_file_name = "{timestamp:s}_uspto_v_50k_by_20171116_coley_c_w_et_al.csv".format(
            timestamp=datetime.now().strftime(
                format="%Y%m%d%H%M%S"
            )
        )

        dataframe = read_csv(
            filepath_or_buffer=Path(input_directory_path, input_file_name),
            header=0,
            index_col=0
        )

        dataframe["file_name"] = input_file_name

        dataframe.to_csv(
            path_or_buf=Path(output_directory_path, output_file_name),
            index=False
        )

    @staticmethod
    def format_v_480k_or_mit_by_20171204_jin_w_et_al(
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Format the data from the `v_480k_or_mit_by_20171204_jin_w_et_al` version of the dataset.

        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        input_file_names = [
            "train.txt",
            "valid.txt",
            "test.txt",
        ]

        output_file_name = "{timestamp:s}_uspto_v_480k_or_mit_by_20171204_jin_w_et_al.csv".format(
            timestamp=datetime.now().strftime(
                format="%Y%m%d%H%M%S"
            )
        )

        dataframes = list()

        for input_file_name in input_file_names:
            dataframe = read_csv(
                filepath_or_buffer=Path(input_directory_path, input_file_name),
                sep="\t",
                header=None
            )

            dataframe["file_name"] = input_file_name

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
            path_or_buf=Path(output_directory_path, output_file_name),
            index=False
        )

    @staticmethod
    def format_v_by_20180622_schwaller_p_et_al(
            version: str,
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Format the data from a `v_*_by_20180622_schwaller_p_et_al` version of the dataset.

        :parameter version: The version of the dataset.
        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        dataframes = list()

        if version == "v_480k_or_mit_by_20180622_schwaller_p_et_al":
            input_file_names = [
                "Jin_USPTO_1product_train.txt",
                "Jin_USPTO_1product_valid.txt",
                "Jin_USPTO_1product_test.txt",
            ]

            for input_file_name in input_file_names:
                dataframe = read_csv(
                    filepath_or_buffer=Path(input_directory_path, input_file_name),
                    sep="\t",
                    header=None,
                    skiprows=[0, ]
                ).rename(
                    columns={
                        0: "reaction_smiles",
                    }
                )

                dataframe["file_name"] = input_file_name

                dataframes.append(
                    dataframe
                )

        elif version == "v_stereo_by_20180622_schwaller_p_et_al":
            input_file_names = [
                "US_patents_1976-Sep2016_1product_reactions_train.csv",
                "US_patents_1976-Sep2016_1product_reactions_valid.csv",
                "US_patents_1976-Sep2016_1product_reactions_test.csv",
            ]

            for input_file_name in input_file_names:
                dataframe = read_csv(
                    filepath_or_buffer=Path(input_directory_path, input_file_name),
                    sep="\t",
                    header=2,
                    low_memory=False
                )

                dataframe["FileName"] = input_file_name

                dataframes.append(
                    dataframe
                )

        else:
            raise ValueError(
                "The formatting of the data from the {data_source:s} is not supported.".format(
                    data_source="USPTO chemical reaction dataset ({version:s})".format(
                        version=version
                    )
                )
            )

        output_file_name = "{timestamp:s}_uspto_{version:s}.csv".format(
            timestamp=datetime.now().strftime(
                format="%Y%m%d%H%M%S"
            ),
            version=version
        )

        concat(
            objs=dataframes
        ).to_csv(
            path_or_buf=Path(output_directory_path, output_file_name),
            index=False
        )

    @staticmethod
    def format_v_lef_by_20181221_bradshaw_j_et_al(
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Format the data from the `v_lef_by_20181221_bradshaw_j_et_al` version of the dataset.

        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        input_file_names = [
            "filtered_train.txt",
            "filtered_valid.txt",
            "filtered_test.txt",
        ]

        output_file_name = "{timestamp:s}_uspto_v_lef_by_20181221_bradshaw_j_et_al.csv".format(
            timestamp=datetime.now().strftime(
                format="%Y%m%d%H%M%S"
            )
        )

        dataframes = list()

        for input_file_name in input_file_names:
            dataframe = read_csv(
                filepath_or_buffer=Path(input_directory_path, input_file_name),
                header=None
            )

            dataframe["file_name"] = input_file_name

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
            path_or_buf=Path(output_directory_path, output_file_name),
            index=False
        )

    @staticmethod
    def format_v_1k_tpl_by_20210128_schwaller_p_et_al(
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Format the data from the `v_1k_tpl_by_20210128_schwaller_p_et_al` version of the dataset.

        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        input_file_names = [
            "uspto_1k_TPL_test.tsv",
            "uspto_1k_TPL_train_valid.tsv",
        ]

        output_file_name = "{timestamp:s}_uspto_v_1k_tpl_by_20210128_schwaller_p_et_al.csv".format(
            timestamp=datetime.now().strftime(
                format="%Y%m%d%H%M%S"
            )
        )

        dataframes = list()

        for input_file_name in input_file_names:
            dataframe = read_csv(
                filepath_or_buffer=Path(input_directory_path, input_file_name),
                sep="\t",
                header=0,
                index_col=0
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

        input_file_names = [
            "1976_Sep2016_USPTOgrants_smiles_mapped.tsv",
            "2001_Sep2016_USPTOapplications_smiles_mapped.tsv",
        ]

        output_file_name = "{timestamp:s}_uspto_v_1976_to_2016_by_20210407_schwaller_p_et_al.csv".format(
            timestamp=datetime.now().strftime(
                format="%Y%m%d%H%M%S"
            )
        )

        dataframes = list()

        for input_file_name in input_file_names:
            dataframe = read_csv(
                filepath_or_buffer=Path(input_directory_path, input_file_name),
                sep="\t",
                header=0,
                index_col=0
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
    def format_v_chen_s_et_al(
            version: str,
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Format the data from a `v_*_chen_s_et_al` version of the dataset.

        :parameter version: The version of the dataset.
        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        if version == "v_1976_to_2016_remapped_by_20240313_chen_s_et_al":
            input_file_name = "remapped_USPTO_FULL.csv"

        elif version == "v_50k_remapped_by_20240313_chen_s_et_al":
            input_file_name = "remapped_USPTO_50K.csv"

        elif version == "v_mech_31k_by_20240810_chen_s_et_al":
            input_file_name = "mech-USPTO-31k.csv"

        else:
            raise ValueError(
                "The formatting of the data from the {data_source:s} is not supported.".format(
                    data_source="USPTO chemical reaction dataset ({version:s})".format(
                        version=version
                    )
                )
            )

        output_file_name = "{timestamp:s}_uspto_{version:s}.csv".format(
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
