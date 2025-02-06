""" The ``data_source.reaction.retro_rules.utility`` package ``extraction`` module. """

from os import PathLike
from pathlib import Path
from shutil import copyfileobj
from typing import Union

from tarfile import TarFile


class RetroRulesReactionDatabaseExtractionUtility:
    """ The `RetroRules <https://retrorules.org>`_ chemical reaction database extraction utility class. """

    @staticmethod
    def extract_v_release(
            version: str,
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Extract the data from a `v_release_*` version of the database.

        :parameter version: The version of the database.
        :parameter input_directory_path: The path to the input directory where the data is downloaded.
        :parameter output_directory_path: The path to the output directory where the data should be extracted.
        """

        if version == "v_release_rr01_rp2_hs":
            input_file_name = "retrorules_rr01_rp2.tar.gz"
            output_file_name = "retrorules_rr01_rp2_flat_all.csv"

            output_file_path = "retrorules_rr01_rp2/{output_file_name:s}".format(
                output_file_name=output_file_name
            )

        elif version == "v_release_rr02_rp2_hs":
            input_file_name = "retrorules_rr02_rp2_hs.tar.gz"
            output_file_name = "retrorules_rr02_rp2_flat_all.csv"

            output_file_path = "retrorules_rr02_rp2_hs/{output_file_name:s}".format(
                output_file_name=output_file_name
            )

        elif version == "v_release_rr02_rp3_hs":
            input_file_name = "retrorules_rr02_rp3_hs.tar.gz"
            output_file_name = "retrorules_rr02_flat_all.tsv"

            output_file_path = "retrorules_rr02_rp3_hs/{output_file_name:s}".format(
                output_file_name=output_file_name
            )

        elif version == "v_release_rr02_rp3_nohs":
            input_file_name = "retrorules_rr02_rp3_nohs.tar.gz"
            output_file_name = "retrorules_rr02_flat_all.tsv"

            output_file_path = "retrorules_rr02_rp3_nohs/{output_file_name:s}".format(
                output_file_name=output_file_name
            )

        else:
            raise ValueError(
                "The extraction of the data from the {data_source:s} is not supported.".format(
                    data_source="RetroRules chemical reaction database ({version:s})".format(
                        version=version
                    )
                )
            )

        with TarFile.open(
            name=Path(input_directory_path, input_file_name),
            mode="r:gz"
        ) as tar_archive_file_handle:
            with tar_archive_file_handle.extractfile(
                member=output_file_path
            ) as source_file_handle:
                with open(
                    file=Path(output_directory_path, output_file_name),
                    mode="wb"
                ) as destination_file_handle:
                    copyfileobj(
                        fsrc=source_file_handle,
                        fdst=destination_file_handle
                    )
