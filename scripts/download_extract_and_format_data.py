""" The ``scripts`` package ``download_extract_and_format_data`` script. """

from argparse import ArgumentParser, Namespace
from datetime import datetime
from logging import Formatter, Logger, StreamHandler, getLogger
from pathlib import Path
from shutil import rmtree

from data_source.compound import CompoundDataSource
from data_source.compound_pattern import CompoundPatternDataSource
from data_source.reaction import ReactionDataSource
from data_source.reaction_pattern import ReactionPatternDataSource


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
            "compound_pattern",
            "reaction",
            "reaction_pattern",
        ],
        required=True,
        help="The category of the data source."
    )

    argument_parser.add_argument(
        "-gdsni",
        "--get_data_source_name_information",
        action="store_true",
        help="The indicator of whether to get the data source name information."
    )

    argument_parser.add_argument(
        "-dsn",
        "--data_source_name",
        default=None,
        type=str,
        choices=[
            "chembl",
            "crd",
            "miscellaneous",
            "ord",
            "rdkit",
            "retro_rules",
            "rhea",
            "uspto",
            "zinc",
        ],
        help="The name of the data source."
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
        default=None,
        type=str,
        help="The indicator of the data source version."
    )

    argument_parser.add_argument(
        "-odp",
        "--output_directory_path",
        default=None,
        type=str,
        help="The path to the output directory where the data should be downloaded, extracted, and formatted."
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


if __name__ == "__main__":
    script_arguments = get_script_arguments()

    script_logger = get_script_logger()

    if script_arguments.data_source_category == "compound":
        data_source = CompoundDataSource(
            logger=script_logger
        )

    elif script_arguments.data_source_category == "compound_pattern":
        data_source = CompoundPatternDataSource(
            logger=script_logger
        )

    elif script_arguments.data_source_category == "reaction":
        data_source = ReactionDataSource(
            logger=script_logger
        )

    elif script_arguments.data_source_category == "reaction_pattern":
        data_source = ReactionPatternDataSource(
            logger=script_logger
        )

    else:
        raise ValueError(
            "The data source category '{category:s}' is not supported.".format(
                category=script_arguments.data_source_category
            )
        )

    if script_arguments.get_data_source_name_information:
        print(script_arguments.data_source_category)
        print(data_source.get_names_of_supported_data_sources())

    elif script_arguments.get_data_source_version_information:
        print(script_arguments.data_source_category)
        print(script_arguments.data_source_name)
        print(data_source.get_supported_versions(
            name=script_arguments.data_source_name
        ))

    else:
        temporary_output_directory_path = Path(
            script_arguments.output_directory_path,
            "{timestamp:s}_temporary_output_directory".format(
                timestamp=datetime.now().strftime(
                    format="%Y%m%d%H%M%S"
                )
            )
        )

        temporary_output_directory_path.mkdir()

        data_source.download(
            name=script_arguments.data_source_name,
            version=script_arguments.data_source_version,
            output_directory_path=temporary_output_directory_path
        )

        data_source.extract(
            name=script_arguments.data_source_name,
            version=script_arguments.data_source_version,
            input_directory_path=temporary_output_directory_path,
            output_directory_path=temporary_output_directory_path
        )

        data_source.format(
            name=script_arguments.data_source_name,
            version=script_arguments.data_source_version,
            input_directory_path=temporary_output_directory_path,
            output_directory_path=script_arguments.output_directory_path,
            number_of_processes=script_arguments.number_of_processes
        )

        rmtree(
            path=temporary_output_directory_path
        )
