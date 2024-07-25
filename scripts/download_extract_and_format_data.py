""" The ``scripts`` package ``download_extract_and_format_data`` script. """

from argparse import ArgumentParser, Namespace
from datetime import datetime
from logging import Formatter, Logger, StreamHandler, getLogger
from os import PathLike
from pathlib import Path
from shutil import rmtree
from typing import Callable, Union

from data_source.compound import *
from data_source.reaction import *
from data_source.reaction_rule import *


def get_script_arguments() -> Namespace:
    """
    Get the script arguments.

    :returns: The script arguments.
    """

    argument_parser = ArgumentParser()

    argument_parser.add_argument(
        "-dsc",
        "--data_source_category",
        type=str,
        choices=[
            "compound",
            "reaction",
            "reaction_rule",
        ],
        help="The indicator of the data source category."
    )

    argument_parser.add_argument(
        "-gdsi",
        "--get_data_source_information",
        action="store_true",
        help="The indicator of whether to get the data source information."
    )

    argument_parser.add_argument(
        "-ds",
        "--data_source",
        type=str,
        choices=[
            "chembl",
            "crd",
            "miscellaneous",
            "ord",
            "retro_rules",
            "rhea",
            "uspto",
            "zinc20",
        ],
        help="The indicator of the data source."
    )

    argument_parser.add_argument(
        "-gdsvi",
        "--get_data_source_version_information",
        action="store_true",
        help="The indicator of whether to get the data source version information."
    )

    argument_parser.add_argument(
        "-dsv",
        "--data_source_version",
        type=str,
        help="The indicator of the data source version."
    )

    argument_parser.add_argument(
        "-odp",
        "--output_directory_path",
        type=str,
        help="The path to the output directory where the data should be formatted."
    )

    argument_parser.add_argument(
        "-nop",
        "--number_of_processes",
        default=1,
        type=str,
        help="The number of processes, if relevant."
    )

    return argument_parser.parse_args()


def get_script_logger() -> Logger:
    """
    Get the script logger.

    :returns: The script logger.
    """

    logger = getLogger(
        name="script_logger"
    )

    logger.setLevel(
        level="DEBUG"
    )

    formatter = Formatter(
        fmt="[{name:s} @ {asctime:s}] {levelname:s}: \"{message:s}\"",
        style="{"
    )

    stream_handler = StreamHandler()

    stream_handler.setLevel(
        level="DEBUG"
    )

    stream_handler.setFormatter(
        fmt=formatter
    )

    logger.addHandler(
        hdlr=stream_handler
    )

    return logger


def download_extract_and_format_data(
        data_source_class: Callable,
        data_source_version: str,
        output_directory_path: Union[str, PathLike[str]],
        number_of_processes: int = 1
) -> None:
    """
    Download, extract, and format the data from the data source.

    :parameter data_source_class: The data source class.
    :parameter data_source_version: The version of the data source.
    :parameter output_directory_path: The path to the output directory where the data should be formatted.
    :parameter number_of_processes: The number of processes.
    """

    data_source = data_source_class(
        logger=script_logger
    )

    temporary_output_directory_path = Path(
        output_directory_path,
        "{timestamp:s}_temporary_output_directory".format(
            timestamp=datetime.now().strftime(
                format="%Y%m%d%H%M%S"
            )
        )
    )

    temporary_output_directory_path.mkdir()

    data_source.download(
        version=data_source_version,
        output_directory_path=temporary_output_directory_path
    )

    data_source.extract(
        version=data_source_version,
        input_directory_path=temporary_output_directory_path,
        output_directory_path=temporary_output_directory_path
    )

    if isinstance(data_source, OpenReactionDatabase):
        data_source.format(
            version=data_source_version,
            input_directory_path=temporary_output_directory_path,
            output_directory_path=output_directory_path,
            number_of_processes=number_of_processes
        )

    else:
        data_source.format(
            version=data_source_version,
            input_directory_path=temporary_output_directory_path,
            output_directory_path=output_directory_path
        )

    rmtree(
        path=temporary_output_directory_path
    )


if __name__ == "__main__":
    script_logger = get_script_logger()

    try:
        script_arguments = get_script_arguments()

        data_source_classes = {
            "compound": {
                "chembl": ChEMBLCompoundDatabase,
                "miscellaneous": MiscellaneousCompoundDataSource,
                "zinc20": ZINC20CompoundDatabase,
            },
            "reaction": {
                "crd": ChemicalReactionDatabase,
                "miscellaneous": MiscellaneousReactionDataSource,
                "ord": OpenReactionDatabase,
                "rhea": RheaReactionDatabase,
                "uspto": USPTOReactionDataset,
            },
            "reaction_rule": {
                "miscellaneous": MiscellaneousReactionRuleDataSource,
                "retro_rules": RetroRulesReactionRuleDatabase,
            },
        }

        if script_arguments.get_data_source_information:
            print(script_arguments.data_source_category)
            print(
                list(data_source_classes[script_arguments.data_source_category].keys())
            )

        elif script_arguments.get_data_source_version_information:
            print(script_arguments.data_source_category)
            print(script_arguments.data_source)
            print(
                data_source_classes[script_arguments.data_source_category][script_arguments.data_source](
                    logger=script_logger
                ).available_versions
            )

        else:
            download_extract_and_format_data(
                data_source_class=data_source_classes[script_arguments.data_source_category][
                    script_arguments.data_source
                ],
                data_source_version=script_arguments.data_source_version,
                output_directory_path=script_arguments.output_directory_path,
                number_of_processes=script_arguments.number_of_processes
            )

    except:
        raise
