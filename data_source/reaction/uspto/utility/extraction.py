""" The ``data_source.reaction.uspto.utility`` package ``extraction`` module. """

from os import PathLike
from pathlib import Path
from shutil import copyfileobj
from typing import Union

from gzip import GzipFile

from py7zr.py7zr import SevenZipFile

from zipfile import ZipFile


class USPTOReactionDatasetExtractionUtility:
    """
    The `United States Patent and Trademark Office (USPTO) <https://www.repository.cam.ac.uk/handle/1810/244727>`_
    chemical reaction dataset extraction utility class.
    """

    @staticmethod
    def extract_v_1976_to_2013_rsmi_by_20121009_lowe_d_m(
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Extract the data from the `v_1976_to_2013_rsmi_by_20121009_lowe_d_m` version of the dataset.

        :parameter input_directory_path: The path to the input directory where the data is downloaded.
        :parameter output_directory_path: The path to the output directory where the data should be extracted.
        """

        input_file_names = [
            "1976-2013_USPTOgrants_reactionSmiles_feb2014filters.7z",
            "2001-2013_USPTOapplications_reactionSmiles_feb2014filters.7z",
        ]

        for input_file_name in input_file_names:
            with SevenZipFile(
                file=Path(input_directory_path, input_file_name)
            ) as seven_zip_archive_file_handle:
                seven_zip_archive_file_handle.extractall(
                    path=output_directory_path
                )

    @staticmethod
    def extract_v_50k_by_20141226_schneider_n_et_al(
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Extract the data from the `v_50k_by_20141226_schneider_n_et_al` version of the dataset.

        :parameter input_directory_path: The path to the input directory where the data is downloaded.
        :parameter output_directory_path: The path to the output directory where the data should be extracted.
        """

        input_file_name = "ci5006614_si_002.zip"

        output_file_names = [
            "training_test_set_patent_data.pkl.gz",
            "unclassified_reactions_patent_data.pkl.gz",
            "names_rTypes_classes_superclasses_training_test_set_patent_data.pkl",
        ]

        with ZipFile(
            file=Path(input_directory_path, input_file_name)
        ) as zip_archive_file_handle:
            for output_file_name in output_file_names:
                with zip_archive_file_handle.open(
                    name="ChemReactionClassification/data/{file_name:s}".format(
                        file_name=output_file_name
                    )
                ) as source_file_handle:
                    with open(
                        file=Path(output_directory_path, output_file_name),
                        mode="wb"
                    ) as destination_file_handle:
                        copyfileobj(
                            fsrc=source_file_handle,
                            fdst=destination_file_handle
                        )

                if output_file_name.endswith(".gz"):
                    with GzipFile(
                        filename=Path(output_directory_path, output_file_name),
                    ) as gzip_archive_file_handle:
                        with open(
                            file=Path(output_directory_path, output_file_name[:-3]),
                            mode="wb"
                        ) as destination_file_handle:
                            copyfileobj(
                                fsrc=gzip_archive_file_handle,
                                fdst=destination_file_handle
                            )

    @staticmethod
    def extract_v_50k_by_20161122_schneider_n_et_al(
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Extract the data from the `v_50k_by_20161122_schneider_n_et_al` version of the chemical reaction dataset.

        :parameter input_directory_path: The path to the input directory where the data is downloaded.
        :parameter output_directory_path: The path to the output directory where the data should be extracted.
        """

        input_file_name = "ci6b00564_si_002.zip"

        output_file_names = [
            "dataSetA.csv",
            "dataSetB.csv",
        ]

        with ZipFile(
            file=Path(input_directory_path, input_file_name)
        ) as zip_archive_file_handle:
            for output_file_name in output_file_names:
                with zip_archive_file_handle.open(
                    name="data/{file_name:s}".format(
                        file_name=output_file_name
                    )
                ) as source_file_handle:
                    with open(
                        file=Path(output_directory_path, output_file_name),
                        mode="wb"
                    ) as destination_file_handle:
                        copyfileobj(
                            fsrc=source_file_handle,
                            fdst=destination_file_handle
                        )

    @staticmethod
    def extract_v_15k_by_20170418_coley_c_w_et_al(
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Extract the data from the `v_15k_by_20170418_coley_c_w_et_al` version of the chemical reaction dataset.

        :parameter input_directory_path: The path to the input directory where the data is downloaded.
        :parameter output_directory_path: The path to the output directory where the data should be extracted.
        """

        input_file_name = "data.zip"

        output_file_names = [
            "train.txt",
            "valid.txt",
            "test.txt",
        ]

        with ZipFile(
            file=Path(input_directory_path, input_file_name)
        ) as zip_archive_file_handle:
            for output_file_name in output_file_names:
                with zip_archive_file_handle.open(
                    name="data/{file_name:s}".format(
                        file_name=output_file_name
                    )
                ) as source_file_handle:
                    with open(
                        file=Path(output_directory_path, output_file_name),
                        mode="wb"
                    ) as destination_file_handle:
                        copyfileobj(
                            fsrc=source_file_handle,
                            fdst=destination_file_handle
                        )

    @staticmethod
    def extract_v_1976_to_2016_by_20121009_lowe_d_m(
            version: str,
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Extract the data from a `v_1976_to_2016_*_by_20121009_lowe_d_m` version of the chemical reaction dataset.

        :parameter version: The version of the chemical reaction dataset.
        :parameter input_directory_path: The path to the input directory where the data is downloaded.
        :parameter output_directory_path: The path to the output directory where the data should be extracted.
        """

        if version == "v_1976_to_2016_by_20121009_lowe_d_m":
            input_file_names = [
                "5104873.zip",
                "cml_xsd.zip",
            ]

            for input_file_name in input_file_names:
                with ZipFile(
                    file=Path(input_directory_path, input_file_name)
                ) as zip_archive_file_handle:
                    zip_archive_file_handle.extractall(
                        path=output_directory_path
                    )

            input_file_names = [
                "1976_Sep2016_USPTOgrants_cml.7z",
                "2001_Sep2016_USPTOapplications_cml.7z",
                "1976_Sep2016_USPTOgrants_smiles.7z",
                "2001_Sep2016_USPTOapplications_smiles.7z",
            ]

        elif version == "v_1976_to_2016_cml_by_20121009_lowe_d_m":
            input_file_names = [
                "1976_Sep2016_USPTOgrants_cml.7z",
                "2001_Sep2016_USPTOapplications_cml.7z",
            ]

        elif version == "v_1976_to_2016_rsmi_by_20121009_lowe_d_m":
            input_file_names = [
                "1976_Sep2016_USPTOgrants_smiles.7z",
                "2001_Sep2016_USPTOapplications_smiles.7z",
            ]

        else:
            raise ValueError(
                "The extraction of the data from the {data_source:s} is not supported.".format(
                    data_source="USPTO chemical reaction dataset ({version:s})".format(
                        version=version
                    )
                )
            )

        for input_file_name in input_file_names:
            with SevenZipFile(
                file=Path(input_directory_path, input_file_name)
            ) as seven_zip_archive_file_handle:
                seven_zip_archive_file_handle.extractall(
                    path=output_directory_path
                )

    @staticmethod
    def extract_v_480k_or_mit_by_20171204_jin_w_et_al(
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Extract the data from the `v_480k_or_mit_by_20171204_jin_w_et_al` version of the chemical reaction dataset.

        :parameter input_directory_path: The path to the input directory where the data is downloaded.
        :parameter output_directory_path: The path to the output directory where the data should be extracted.
        """

        input_file_name = "data.zip"

        output_file_names = [
            "train.txt",
            "valid.txt",
            "test.txt",
        ]

        with ZipFile(
            file=Path(input_directory_path, input_file_name)
        ) as zip_archive_file_handle:
            for output_file_name in output_file_names:
                with zip_archive_file_handle.open(
                    name="data/{file_name:s}".format(
                        file_name=output_file_name
                    )
                ) as source_file_handle:
                    with open(
                        file=Path(output_directory_path, output_file_name),
                        mode="wb"
                    ) as destination_file_handle:
                        copyfileobj(
                            fsrc=source_file_handle,
                            fdst=destination_file_handle
                        )

    @staticmethod
    def extract_v_by_20180622_schwaller_p_et_al(
            version: str,
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Extract the data from a `v_*_by_20180622_schwaller_p_et_al` version of the chemical reaction dataset.

        :parameter version: The version of the chemical reaction dataset.
        :parameter input_directory_path: The path to the input directory where the data is downloaded.
        :parameter output_directory_path: The path to the output directory where the data should be extracted.
        """

        input_file_name = "ReactionSeq2Seq_Dataset.zip"

        if version == "v_480k_or_mit_by_20180622_schwaller_p_et_al":
            output_file_names = [
                "Jin_USPTO_1product_train.txt",
                "Jin_USPTO_1product_valid.txt",
                "Jin_USPTO_1product_test.txt",
            ]

        elif version == "v_stereo_by_20180622_schwaller_p_et_al":
            output_file_names = [
                "US_patents_1976-Sep2016_1product_reactions_train.csv",
                "US_patents_1976-Sep2016_1product_reactions_valid.csv",
                "US_patents_1976-Sep2016_1product_reactions_test.csv",
            ]

        else:
            raise ValueError(
                "The extraction of the data from the {data_source:s} is not supported.".format(
                    data_source="USPTO chemical reaction dataset ({version:s})".format(
                        version=version
                    )
                )
            )

        with ZipFile(
            file=Path(input_directory_path, input_file_name)
        ) as zip_archive_file_handle:
            for output_file_name in output_file_names:
                with zip_archive_file_handle.open(
                    name="ReactionSeq2Seq_Dataset/{file_name:s}".format(
                        file_name=output_file_name
                    )
                ) as source_file_handle:
                    with open(
                        file=Path(output_directory_path, output_file_name),
                        mode="wb"
                    ) as destination_file_handle:
                        copyfileobj(
                            fsrc=source_file_handle,
                            fdst=destination_file_handle
                        )

    @staticmethod
    def extract_v_lef_by_20181221_bradshaw_j_et_al(
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Extract the data from the `v_lef_by_20181221_bradshaw_j_et_al` version of the chemical reaction dataset.

        :parameter input_directory_path: The path to the input directory where the data is downloaded.
        :parameter output_directory_path: The path to the output directory where the data should be extracted.
        """

        input_file_name = "lef_uspto.zip"

        output_file_names = [
            "filtered_train.txt",
            "filtered_valid.txt",
            "filtered_test.txt",
        ]

        with ZipFile(
            file=Path(input_directory_path, input_file_name)
        ) as zip_archive_file_handle:
            for output_file_name in output_file_names:
                with zip_archive_file_handle.open(
                    name="lef_uspto/{file_name:s}".format(
                        file_name=output_file_name
                    )
                ) as source_file_handle:
                    with open(
                        file=Path(output_directory_path, output_file_name),
                        mode="wb"
                    ) as destination_file_handle:
                        copyfileobj(
                            fsrc=source_file_handle,
                            fdst=destination_file_handle
                        )

    @staticmethod
    def extract_v_1k_tpl_by_20210128_schwaller_p_et_al(
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Extract the data from the `v_1k_tpl_by_20210128_schwaller_p_et_al` version of the chemical reaction dataset.

        :parameter input_directory_path: The path to the input directory where the data is downloaded.
        :parameter output_directory_path: The path to the output directory where the data should be extracted.
        """

        input_file_name = "MappingChemicalReactions.zip"

        output_file_names = [
            "uspto_1k_TPL_train_valid.tsv.gzip",
            "uspto_1k_TPL_test.tsv.gzip",
        ]

        with ZipFile(
            file=Path(input_directory_path, input_file_name)
        ) as zip_archive_file_handle:
            for output_file_name in output_file_names:
                with zip_archive_file_handle.open(
                    name="data_set/{file_name:s}".format(
                        file_name=output_file_name
                    )
                ) as source_file_handle:
                    with open(
                        file=Path(output_directory_path, output_file_name),
                        mode="wb"
                    ) as destination_file_handle:
                        copyfileobj(
                            fsrc=source_file_handle,
                            fdst=destination_file_handle
                        )

                with GzipFile(
                    filename=Path(input_directory_path, output_file_name)
                ) as gzip_archive_file_handle:
                    with open(
                        file=Path(output_directory_path, output_file_name[:-5]),
                        mode="wb"
                    ) as destination_file_handle:
                        copyfileobj(
                            fsrc=gzip_archive_file_handle,
                            fdst=destination_file_handle
                        )

    @staticmethod
    def extract_v_1976_to_2016_remapped_by_20210407_schwaller_p_et_al(
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Extract the data from the `v_1976_to_2016_remapped_by_20210407_schwaller_p_et_al` version of the chemical
        reaction dataset.

        :parameter input_directory_path: The path to the input directory where the data is downloaded.
        :parameter output_directory_path: The path to the output directory where the data should be extracted.
        """

        input_file_name = "USPTO_remapped.zip"

        output_file_names = [
            "1976_Sep2016_USPTOgrants_smiles_mapped.tsv",
            "2001_Sep2016_USPTOapplications_smiles_mapped.tsv",
        ]

        with ZipFile(
            file=Path(input_directory_path, input_file_name)
        ) as zip_archive_file_handle:
            for output_file_name in output_file_names:
                with zip_archive_file_handle.open(
                    name="USPTO_remapped/{file_name:s}".format(
                        file_name=output_file_name
                    )
                ) as source_file_handle:
                    with open(
                        file=Path(output_directory_path, output_file_name),
                        mode="wb"
                    ) as destination_file_handle:
                        copyfileobj(
                            fsrc=source_file_handle,
                            fdst=destination_file_handle
                        )
