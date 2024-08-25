""" The ``data_source.reaction_rule.retro_rules.utility`` package ``extraction`` module. """

from os import PathLike
from pathlib import Path
from shutil import copyfileobj
from typing import Union

from tarfile import open as open_tar_archive_file


class RetroRulesReactionRuleDatabaseExtractionUtility:
    """ The `RetroRules <https://retrorules.org>`_ chemical reaction rule database extraction utility class. """

    @staticmethod
    def extract_v_release(
            version: str,
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Extract the data from a `v_release_*` version of the chemical reaction rule database.

        :parameter version: The version of the chemical reaction rule database.
        :parameter input_directory_path: The path to the input directory where the data is downloaded.
        :parameter output_directory_path: The path to the output directory where the data should be extracted.
        """

        if version == "v_release_rr01_rp2_hs":
            tar_archive_file_name = "retrorules_rr01_rp2.tar.gz"
            file_path = "retrorules_rr01_rp2/retrorules_rr01_rp2_flat_all.csv"

        elif version == "v_release_rr02_rp2_hs":
            tar_archive_file_name = "retrorules_rr02_rp2_hs.tar.gz"
            file_path = "retrorules_rr02_rp2_hs/retrorules_rr02_rp2_flat_all.csv"

        elif version == "v_release_rr02_rp3_hs":
            tar_archive_file_name = "retrorules_rr02_rp3_hs.tar.gz"
            file_path = "retrorules_rr02_rp3_hs/retrorules_rr02_flat_all.tsv"

        else:
            tar_archive_file_name = "retrorules_rr02_rp3_nohs.tar.gz"
            file_path = "retrorules_rr02_rp3_nohs/retrorules_rr02_flat_all.tsv"

        with open_tar_archive_file(
            name=Path(input_directory_path, tar_archive_file_name),
            mode="r:gz"
        ) as tar_archive_file_handle:
            with tar_archive_file_handle.extractfile(
                member=file_path
            ) as source_file_handle:
                with open(
                    file=Path(
                        output_directory_path,
                        file_path.split(
                            sep="/"
                        )[-1]
                    ),
                    mode="wb"
                ) as destination_file_handle:
                    copyfileobj(
                        fsrc=source_file_handle,
                        fdst=destination_file_handle
                    )
