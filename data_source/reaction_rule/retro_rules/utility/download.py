""" The ``data_source.reaction_rule.retro_rules.utility`` package ``download`` module. """

from os import PathLike
from typing import Union

from data_source.base.utility.download import BaseDataSourceDownloadUtility


class RetroRulesReactionRuleDatabaseDownloadUtility:
    """ The `RetroRules <https://retrorules.org>`_ chemical reaction rule database download utility class. """

    @staticmethod
    def download_v_release(
            version: str,
            output_directory_path: Union[str, PathLike[str]]
    ) -> None:
        """
        Download the data from a `v_release_*` version of the database.

        :parameter version: The version of the database.
        :parameter output_directory_path: The path to the output directory where the data should be downloaded.
        """

        if version == "v_release_rr01_rp2_hs":
            file_name = "retrorules_rr01_rp2.tar.gz"

            file_url = "https://zenodo.org/records/5827427/files/{file_name:s}".format(
                file_name=file_name
            )

        elif version == "v_release_rr02_rp2_hs":
            file_name = "retrorules_rr02_rp2_hs.tar.gz"

            file_url = "https://zenodo.org/records/5828017/files/{file_name:s}".format(
                file_name=file_name
            )

        elif version == "v_release_rr02_rp3_hs":
            file_name = "retrorules_rr02_rp3_hs.tar.gz"

            file_url = "https://zenodo.org/records/5827977/files/{file_name:s}".format(
                file_name=file_name
            )

        else:
            file_name = "retrorules_rr02_rp3_nohs.tar.gz"

            file_url = "https://zenodo.org/records/5827969/files/{file_name:s}".format(
                file_name=file_name
            )

        BaseDataSourceDownloadUtility.download_file(
            file_url=file_url,
            file_name=file_name,
            output_directory_path=output_directory_path
        )
