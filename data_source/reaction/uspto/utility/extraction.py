""" The ``data_source.reaction.uspto.utility`` package ``extraction`` module. """

from os import PathLike
from pathlib import Path
from shutil import copyfileobj
from typing import Union

from gzip import open as open_gzip_archive_file

from py7zr import SevenZipFile

from zipfile import ZipFile


class USPTOReactionDatasetExtractionUtility:
    """
    The `United States Patent and Trademark Office (USPTO) <https://www.repository.cam.ac.uk/handle/1810/244727>`_
    chemical reaction dataset extraction utility class.
    """

    @staticmethod
    def extract_v_1976_to_2013_by_20121009_lowe_d_m(
            version: str,
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Extract the data from a `v_1976_to_2013_*_by_20121009_lowe_d_m` version of the chemical reaction dataset.

        :parameter version: The version of the chemical reaction dataset.
        :parameter input_directory_path: The path to the input directory where the data is downloaded.
        :parameter output_directory_path: The path to the output directory where the data should be extracted.
        """

        if version == "v_1976_to_2013_cml_by_20121009_lowe_d_m":
            file_names = [
                "1976-2013_USPTOgrants_CML.7z",
                "2001-2013_USPTOapplications_CML.7z",
            ]

        elif version == "v_1976_to_2013_rsmi_by_20121009_lowe_d_m":
            file_names = [
                "1976-2013_USPTOgrants_reactionSmiles_feb2014filters.7z",
                "2001-2013_USPTOapplications_reactionSmiles_feb2014filters.7z",
            ]

        else:
            for file_name in [
                "12084729.zip",
                "2008-2011_USPTO_reactionSmiles_filtered.zip",
                "documentation.zip",
            ]:
                with ZipFile(
                    file=Path(input_directory_path, file_name)
                ) as zip_archive_file_handle:
                    zip_archive_file_handle.extractall(
                        path=output_directory_path
                    )

            file_names = [
                "1976-2013_USPTOgrants_CML.7z",
                "2001-2013_USPTOapplications_CML.7z",
                "1976-2013_USPTOgrants_reactionSmiles_feb2014filters.7z",
                "2001-2013_USPTOapplications_reactionSmiles_feb2014filters.7z",
            ]

        for file_name in file_names:
            with SevenZipFile(
                file=Path(input_directory_path, file_name)
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
        Extract the data from the `v_50k_by_20141226_schneider_n_et_al` version of the chemical reaction dataset.

        :parameter input_directory_path: The path to the input directory where the data is downloaded.
        :parameter output_directory_path: The path to the output directory where the data should be extracted.
        """

        with ZipFile(
            file=Path(input_directory_path, "ci5006614_si_002.zip")
        ) as zip_archive_file_handle:
            for file_name in [
                "training_test_set_patent_data.pkl.gz",
                "unclassified_reactions_patent_data.pkl.gz",
                "names_rTypes_classes_superclasses_training_test_set_patent_data.pkl",
            ]:
                with zip_archive_file_handle.open(
                    name="ChemReactionClassification/data/{file_name:s}".format(
                        file_name=file_name
                    )
                ) as source_file_handle:
                    with open(
                        file=Path(output_directory_path, file_name),
                        mode="wb"
                    ) as destination_file_handle:
                        copyfileobj(
                            fsrc=source_file_handle,
                            fdst=destination_file_handle
                        )

                if file_name.endswith(".gz"):
                    with open_gzip_archive_file(
                        filename=Path(output_directory_path, file_name)
                    ) as gzip_archive_file_handle:
                        with open(
                            file=Path(output_directory_path, file_name[:-3]),
                            mode="wb"
                        ) as file_handle:
                            copyfileobj(
                                fsrc=gzip_archive_file_handle,
                                fdst=file_handle
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

        with ZipFile(
            file=Path(input_directory_path, "ci6b00564_si_002.zip")
        ) as zip_archive_file_handle:
            for file_name in [
                "dataSetA.csv",
                "dataSetB.csv",
            ]:
                with zip_archive_file_handle.open(
                    name="data/{file_name:s}".format(
                        file_name=file_name
                    )
                ) as source_file_handle:
                    with open(
                        file=Path(output_directory_path, file_name),
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

        with ZipFile(
            file=Path(input_directory_path, "data.zip")
        ) as zip_archive_file_handle:
            for file_name in [
                "train.txt",
                "valid.txt",
                "test.txt",
            ]:
                with zip_archive_file_handle.open(
                    name="data/{file_name:s}".format(
                        file_name=file_name
                    )
                ) as source_file_handle:
                    with open(
                        file=Path(output_directory_path, file_name),
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

        if version == "v_1976_to_2016_cml_by_20121009_lowe_d_m":
            file_names = [
                "1976_Sep2016_USPTOgrants_cml.7z",
                "2001_Sep2016_USPTOapplications_cml.7z",
            ]

        elif version == "v_1976_to_2016_rsmi_by_20121009_lowe_d_m":
            file_names = [
                "1976_Sep2016_USPTOgrants_smiles.7z",
                "2001_Sep2016_USPTOapplications_smiles.7z",
            ]

        else:
            for file_name in [
                "5104873.zip",
                "cml_xsd.zip",
            ]:
                with ZipFile(
                    file=Path(input_directory_path, file_name)
                ) as zip_archive_file_handle:
                    zip_archive_file_handle.extractall(
                        path=output_directory_path
                    )

            file_names = [
                "1976_Sep2016_USPTOgrants_cml.7z",
                "2001_Sep2016_USPTOapplications_cml.7z",
                "1976_Sep2016_USPTOgrants_smiles.7z",
                "2001_Sep2016_USPTOapplications_smiles.7z",
            ]

        for file_name in file_names:
            with SevenZipFile(
                file=Path(input_directory_path, file_name)
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

        with ZipFile(
            file=Path(input_directory_path, "data.zip")
        ) as zip_archive_file_handle:
            for file_name in [
                "train.txt",
                "valid.txt",
                "test.txt",
            ]:
                with zip_archive_file_handle.open(
                    name="data/{file_name:s}".format(
                        file_name=file_name
                    )
                ) as source_file_handle:
                    with open(
                        file=Path(output_directory_path, file_name),
                        mode="wb"
                    ) as destination_file_handle:
                        copyfileobj(
                            fsrc=source_file_handle,
                            fdst=destination_file_handle
                        )

    @staticmethod
    def extract_v_20180622_schwaller_p_et_al(
            version: str,
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Extract the data from the `v_*_20180622_schwaller_p_et_al` version of the chemical reaction dataset.

        :parameter version: The version of the chemical reaction dataset.
        :parameter input_directory_path: The path to the input directory where the data is downloaded.
        :parameter output_directory_path: The path to the output directory where the data should be extracted.
        """

        if version == "v_480k_or_mit_by_20180622_schwaller_p_et_al":
            file_names = [
                "Jin_USPTO_1product_train.txt",
                "Jin_USPTO_1product_valid.txt",
                "Jin_USPTO_1product_test.txt",
            ]

        else:
            file_names = [
                "US_patents_1976-Sep2016_1product_reactions_train.csv",
                "US_patents_1976-Sep2016_1product_reactions_valid.csv",
                "US_patents_1976-Sep2016_1product_reactions_test.csv",
            ]

        with ZipFile(
            file=Path(input_directory_path, "ReactionSeq2Seq_Dataset.zip")
        ) as zip_archive_file_handle:
            for file_name in file_names:
                with zip_archive_file_handle.open(
                    name="ReactionSeq2Seq_Dataset/{file_name:s}".format(
                        file_name=file_name
                    )
                ) as source_file_handle:
                    with open(
                        file=Path(output_directory_path, file_name),
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

        with ZipFile(
            file=Path(input_directory_path, "lef_uspto.zip")
        ) as zip_archive_file_handle:
            for file_name in [
                "filtered_train.txt",
                "filtered_valid.txt",
                "filtered_test.txt",
            ]:
                with zip_archive_file_handle.open(
                    name="lef_uspto/{file_name:s}".format(
                        file_name=file_name
                    )
                ) as source_file_handle:
                    with open(
                        file=Path(output_directory_path, file_name),
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

        with ZipFile(
            file=Path(input_directory_path, "MappingChemicalReactions.zip")
        ) as zip_archive_file_handle:
            for file_name in [
                "uspto_1k_TPL_train_valid.tsv.gzip",
                "uspto_1k_TPL_test.tsv.gzip",
            ]:
                with zip_archive_file_handle.open(
                    name="data_set/{file_name:s}".format(
                        file_name=file_name
                    )
                ) as source_file_handle:
                    with open(
                        file=Path(output_directory_path, file_name),
                        mode="wb"
                    ) as destination_file_handle:
                        copyfileobj(
                            fsrc=source_file_handle,
                            fdst=destination_file_handle
                        )

                with open_gzip_archive_file(
                    filename=Path(input_directory_path, file_name)
                ) as gzip_archive_file_handle:
                    with open(
                        file=Path(output_directory_path, file_name[:-5]),
                        mode="wb"
                    ) as file_handle:
                        copyfileobj(
                            fsrc=gzip_archive_file_handle,
                            fdst=file_handle
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

        with ZipFile(
            file=Path(input_directory_path, "USPTO_remapped.zip")
        ) as zip_archive_file_handle:
            for file_name in [
                "1976_Sep2016_USPTOgrants_smiles_mapped.tsv",
                "2001_Sep2016_USPTOapplications_smiles_mapped.tsv",
            ]:
                with zip_archive_file_handle.open(
                    name="USPTO_remapped/{file_name:s}".format(
                        file_name=file_name
                    )
                ) as source_file_handle:
                    with open(
                        file=Path(output_directory_path, file_name),
                        mode="wb"
                    ) as destination_file_handle:
                        copyfileobj(
                            fsrc=source_file_handle,
                            fdst=destination_file_handle
                        )
