""" The ``data_source.reaction.uspto`` package ``uspto`` module. """

from os import PathLike
from typing import Dict, Union

from data_source.base.base import DataSourceBase
from data_source.reaction.uspto.utility.download import USPTOReactionDatasetDownloadUtility
from data_source.reaction.uspto.utility.extraction import USPTOReactionDatasetExtractionUtility
from data_source.reaction.uspto.utility.formatting import USPTOReactionDatasetFormattingUtility


class USPTOReactionDataset(DataSourceBase):
    """
    The `United States Patent and Trademark Office (USPTO) <https://www.repository.cam.ac.uk/handle/1810/244727>`_
    chemical reaction dataset class.
    """

    @staticmethod
    def get_supported_versions() -> Dict[str, str]:
        """
        Get the supported versions of the dataset.

        :returns: The supported versions of the dataset.
        """

        return {
            "v_1976_to_2013_rsmi_by_20121009_lowe_d_m": "https://doi.org/10.6084/m9.figshare.12084729.v1",
            "v_50k_by_20141226_schneider_n_et_al": "https://doi.org/10.1021/ci5006614",
            "v_50k_by_20161122_schneider_n_et_al": "https://doi.org/10.1021/acs.jcim.6b00564",
            "v_15k_by_20170418_coley_c_w_et_al": "https://doi.org/10.1021/acscentsci.7b00064",
            "v_1976_to_2016_cml_by_20121009_lowe_d_m": "https://doi.org/10.6084/m9.figshare.5104873.v1",
            "v_1976_to_2016_rsmi_by_20121009_lowe_d_m": "https://doi.org/10.6084/m9.figshare.5104873.v1",
            "v_50k_by_20170905_liu_b_et_al": "https://doi.org/10.1021/acscentsci.7b00303",
            "v_50k_by_20171116_coley_c_w_et_al": "https://doi.org/10.1021/acscentsci.7b00355",
            "v_480k_or_mit_by_20171204_jin_w_et_al": "https://doi.org/10.48550/arXiv.1709.04555",
            "v_480k_or_mit_by_20180622_schwaller_p_et_al": "https://doi.org/10.1039/C8SC02339E",
            "v_stereo_by_20180622_schwaller_p_et_al": "https://doi.org/10.1039/C8SC02339E",
            "v_lef_by_20181221_bradshaw_j_et_al": "https://doi.org/10.48550/arXiv.1805.10970",
            "v_1k_tpl_by_20210128_schwaller_p_et_al": "https://doi.org/10.1038/s42256-020-00284-w",
            "v_1976_to_2016_remapped_by_20210407_schwaller_p_et_al": "https://doi.org/10.1126/sciadv.abe4166",
            "v_1976_to_2016_remapped_by_20240313_chen_s_et_al": "https://doi.org/10.6084/m9.figshare.25046471.v1",
            "v_50k_remapped_by_20240313_chen_s_et_al": "https://doi.org/10.6084/m9.figshare.25046471.v1",
            "v_mech_31k_by_20240810_chen_s_et_al": "https://doi.org/10.6084/m9.figshare.24797220.v2",
        }

    def download_(
            self,
            version: str,
            output_directory_path: Union[str, PathLike[str]],
            **kwargs
    ) -> None:
        """
        Download the data from the dataset.

        :parameter version: The version of the dataset.
        :parameter output_directory_path: The path to the output directory where the data should be downloaded.
        """

        try:
            if version in self.get_supported_versions().keys():
                if self.logger is not None:
                    self.logger.info(
                        msg="The download of the data from the {data_source:s} has been started.".format(
                            data_source="USPTO chemical reaction dataset ({version:s})".format(
                                version=version
                            )
                        )
                    )

                if version == "v_1976_to_2013_rsmi_by_20121009_lowe_d_m":
                    USPTOReactionDatasetDownloadUtility.download_v_1976_to_2013_by_20121009_lowe_d_m(
                        version=version,
                        output_directory_path=output_directory_path
                    )

                if version == "v_50k_by_20141226_schneider_n_et_al":
                    USPTOReactionDatasetDownloadUtility.download_v_50k_by_20141226_schneider_n_et_al(
                        output_directory_path=output_directory_path
                    )

                if version == "v_50k_by_20161122_schneider_n_et_al":
                    USPTOReactionDatasetDownloadUtility.download_v_50k_by_20161122_schneider_n_et_al(
                        output_directory_path=output_directory_path
                    )

                if version == "v_15k_by_20170418_coley_c_w_et_al":
                    USPTOReactionDatasetDownloadUtility.download_v_15k_by_20170418_coley_c_w_et_al(
                        output_directory_path=output_directory_path
                    )

                if version in [
                    "v_1976_to_2016_cml_by_20121009_lowe_d_m",
                    "v_1976_to_2016_rsmi_by_20121009_lowe_d_m",
                ]:
                    USPTOReactionDatasetDownloadUtility.download_v_1976_to_2016_by_20121009_lowe_d_m(
                        version=version,
                        output_directory_path=output_directory_path
                    )

                if version == "v_50k_by_20170905_liu_b_et_al":
                    USPTOReactionDatasetDownloadUtility.download_v_50k_by_20170905_liu_b_et_al(
                        output_directory_path=output_directory_path
                    )

                if version == "v_50k_by_20171116_coley_c_w_et_al":
                    USPTOReactionDatasetDownloadUtility.download_v_50k_by_20171116_coley_c_w_et_al(
                        output_directory_path=output_directory_path
                    )

                if version == "v_480k_or_mit_by_20171204_jin_w_et_al":
                    USPTOReactionDatasetDownloadUtility.download_v_480k_or_mit_by_20171204_jin_w_et_al(
                        output_directory_path=output_directory_path
                    )

                if version in [
                    "v_480k_or_mit_by_20180622_schwaller_p_et_al",
                    "v_stereo_by_20180622_schwaller_p_et_al",
                ]:
                    USPTOReactionDatasetDownloadUtility.download_v_by_20180622_schwaller_p_et_al(
                        output_directory_path=output_directory_path
                    )

                if version == "v_lef_by_20181221_bradshaw_j_et_al":
                    USPTOReactionDatasetDownloadUtility.download_v_lef_by_20181221_bradshaw_j_et_al(
                        output_directory_path=output_directory_path
                    )

                if version == "v_1k_tpl_by_20210128_schwaller_p_et_al":
                    USPTOReactionDatasetDownloadUtility.download_v_1k_tpl_by_20210128_schwaller_p_et_al(
                        output_directory_path=output_directory_path
                    )

                if version == "v_1976_to_2016_remapped_by_20210407_schwaller_p_et_al":
                    USPTOReactionDatasetDownloadUtility.download_v_1976_to_2016_remapped_by_20210407_schwaller_p_et_al(
                        output_directory_path=output_directory_path
                    )

                if version in [
                    "v_1976_to_2016_remapped_by_20240313_chen_s_et_al",
                    "v_50k_remapped_by_20240313_chen_s_et_al",
                    "v_mech_31k_by_20240810_chen_s_et_al",
                ]:
                    USPTOReactionDatasetDownloadUtility.download_v_chen_s_et_al(
                        version=version,
                        output_directory_path=output_directory_path
                    )

                if self.logger is not None:
                    self.logger.info(
                        msg="The download of the data from the {data_source:s} has been completed.".format(
                            data_source="USPTO chemical reaction dataset ({version:s})".format(
                                version=version
                            )
                        )
                    )

            else:
                raise ValueError(
                    "The download of the data from the {data_source:s} is not supported.".format(
                        data_source="USPTO chemical reaction dataset ({version:s})".format(
                            version=version
                        )
                    )
                )

        except Exception as exception_handle:
            if self.logger is not None:
                self.logger.error(
                    msg=exception_handle
                )

            raise

    def extract_(
            self,
            version: str,
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]],
            **kwargs
    ) -> None:
        """
        Extract the data from the dataset.

        :parameter version: The version of the dataset.
        :parameter input_directory_path: The path to the input directory where the data is downloaded.
        :parameter output_directory_path: The path to the output directory where the data should be extracted.
        """

        try:
            if version in self.get_supported_versions().keys():
                if self.logger is not None:
                    self.logger.info(
                        msg="The extraction of the data from the {data_source:s} has been started.".format(
                            data_source="USPTO chemical reaction dataset ({version:s})".format(
                                version=version
                            )
                        )
                    )

                if version == "v_1976_to_2013_rsmi_by_20121009_lowe_d_m":
                    USPTOReactionDatasetExtractionUtility.extract_v_1976_to_2013_rsmi_by_20121009_lowe_d_m(
                        input_directory_path=input_directory_path,
                        output_directory_path=output_directory_path
                    )

                if version == "v_50k_by_20141226_schneider_n_et_al":
                    USPTOReactionDatasetExtractionUtility.extract_v_50k_by_20141226_schneider_n_et_al(
                        input_directory_path=input_directory_path,
                        output_directory_path=output_directory_path
                    )

                if version == "v_50k_by_20161122_schneider_n_et_al":
                    USPTOReactionDatasetExtractionUtility.extract_v_50k_by_20161122_schneider_n_et_al(
                        input_directory_path=input_directory_path,
                        output_directory_path=output_directory_path
                    )

                if version == "v_15k_by_20170418_coley_c_w_et_al":
                    USPTOReactionDatasetExtractionUtility.extract_v_15k_by_20170418_coley_c_w_et_al(
                        input_directory_path=input_directory_path,
                        output_directory_path=output_directory_path
                    )

                if version in [
                    "v_1976_to_2016_cml_by_20121009_lowe_d_m",
                    "v_1976_to_2016_rsmi_by_20121009_lowe_d_m",
                ]:
                    USPTOReactionDatasetExtractionUtility.extract_v_1976_to_2016_by_20121009_lowe_d_m(
                        version=version,
                        input_directory_path=input_directory_path,
                        output_directory_path=output_directory_path
                    )

                if version == "v_480k_or_mit_by_20171204_jin_w_et_al":
                    USPTOReactionDatasetExtractionUtility.extract_v_480k_or_mit_by_20171204_jin_w_et_al(
                        input_directory_path=input_directory_path,
                        output_directory_path=output_directory_path
                    )

                if version in [
                    "v_480k_or_mit_by_20180622_schwaller_p_et_al",
                    "v_stereo_by_20180622_schwaller_p_et_al",
                ]:
                    USPTOReactionDatasetExtractionUtility.extract_v_by_20180622_schwaller_p_et_al(
                        version=version,
                        input_directory_path=input_directory_path,
                        output_directory_path=output_directory_path
                    )

                if version == "v_lef_by_20181221_bradshaw_j_et_al":
                    USPTOReactionDatasetExtractionUtility.extract_v_lef_by_20181221_bradshaw_j_et_al(
                        input_directory_path=input_directory_path,
                        output_directory_path=output_directory_path
                    )

                if version == "v_1k_tpl_by_20210128_schwaller_p_et_al":
                    USPTOReactionDatasetExtractionUtility.extract_v_1k_tpl_by_20210128_schwaller_p_et_al(
                        input_directory_path=input_directory_path,
                        output_directory_path=output_directory_path
                    )

                if version == "v_1976_to_2016_remapped_by_20210407_schwaller_p_et_al":
                    USPTOReactionDatasetExtractionUtility.extract_v_1976_to_2016_remapped_by_20210407_schwaller_p_et_al(
                        input_directory_path=input_directory_path,
                        output_directory_path=output_directory_path
                    )

                if self.logger is not None:
                    self.logger.info(
                        msg="The extraction of the data from the {data_source:s} has been completed.".format(
                            data_source="USPTO chemical reaction dataset ({version:s})".format(
                                version=version
                            )
                        )
                    )

            else:
                raise ValueError(
                    "The extraction of the data from the {data_source:s} is not supported.".format(
                        data_source="USPTO chemical reaction dataset ({version:s})".format(
                            version=version
                        )
                    )
                )

        except Exception as exception_handle:
            if self.logger is not None:
                self.logger.error(
                    msg=exception_handle
                )

            raise

    def format_(
            self,
            version: str,
            input_directory_path: Union[str, PathLike[str]],
            output_directory_path: Union[str, PathLike[str]],
            **kwargs
    ) -> None:
        """
        Format the data from the dataset.

        :parameter version: The version of the dataset.
        :parameter input_directory_path: The path to the input directory where the data is extracted.
        :parameter output_directory_path: The path to the output directory where the data should be formatted.
        """

        try:
            if version in self.get_supported_versions().keys():
                if self.logger is not None:
                    self.logger.info(
                        msg="The formatting of the data from the {data_source:s} has been started.".format(
                            data_source="USPTO chemical reaction dataset ({version:s})".format(
                                version=version
                            )
                        )
                    )

                if version == "v_1976_to_2013_rsmi_by_20121009_lowe_d_m":
                    USPTOReactionDatasetFormattingUtility.format_v_1976_to_2013_rsmi_by_20121009_lowe_d_m(
                        input_directory_path=input_directory_path,
                        output_directory_path=output_directory_path
                    )

                if version == "v_50k_by_20141226_schneider_n_et_al":
                    USPTOReactionDatasetFormattingUtility.format_v_50k_by_20141226_schneider_n_et_al(
                        input_directory_path=input_directory_path,
                        output_directory_path=output_directory_path
                    )

                if version == "v_50k_by_20161122_schneider_n_et_al":
                    USPTOReactionDatasetFormattingUtility.format_v_50k_by_20161122_schneider_n_et_al(
                        input_directory_path=input_directory_path,
                        output_directory_path=output_directory_path
                    )

                if version == "v_15k_by_20170418_coley_c_w_et_al":
                    USPTOReactionDatasetFormattingUtility.format_v_15k_by_20170418_coley_c_w_et_al(
                        input_directory_path=input_directory_path,
                        output_directory_path=output_directory_path
                    )

                if version in [
                    "v_1976_to_2016_cml_by_20121009_lowe_d_m",
                    "v_1976_to_2016_rsmi_by_20121009_lowe_d_m",
                ]:
                    USPTOReactionDatasetFormattingUtility.format_v_1976_to_2016_by_20121009_lowe_d_m(
                        version=version,
                        input_directory_path=input_directory_path,
                        output_directory_path=output_directory_path,
                        number_of_processes=kwargs.get("number_of_processes", 1)
                    )

                if version == "v_50k_by_20170905_liu_b_et_al":
                    USPTOReactionDatasetFormattingUtility.format_v_50k_by_20170905_liu_b_et_al(
                        input_directory_path=input_directory_path,
                        output_directory_path=output_directory_path
                    )

                if version == "v_50k_by_20171116_coley_c_w_et_al":
                    USPTOReactionDatasetFormattingUtility.format_v_50k_by_20171116_coley_c_w_et_al(
                        input_directory_path=input_directory_path,
                        output_directory_path=output_directory_path
                    )

                if version == "v_480k_or_mit_by_20171204_jin_w_et_al":
                    USPTOReactionDatasetFormattingUtility.format_v_480k_or_mit_by_20171204_jin_w_et_al(
                        input_directory_path=input_directory_path,
                        output_directory_path=output_directory_path
                    )

                if version in [
                    "v_480k_or_mit_by_20180622_schwaller_p_et_al",
                    "v_stereo_by_20180622_schwaller_p_et_al",
                ]:
                    USPTOReactionDatasetFormattingUtility.format_v_by_20180622_schwaller_p_et_al(
                        version=version,
                        input_directory_path=input_directory_path,
                        output_directory_path=output_directory_path
                    )

                if version == "v_lef_by_20181221_bradshaw_j_et_al":
                    USPTOReactionDatasetFormattingUtility.format_v_lef_by_20181221_bradshaw_j_et_al(
                        input_directory_path=input_directory_path,
                        output_directory_path=output_directory_path
                    )

                if version == "v_1k_tpl_by_20210128_schwaller_p_et_al":
                    USPTOReactionDatasetFormattingUtility.format_v_1k_tpl_by_20210128_schwaller_p_et_al(
                        input_directory_path=input_directory_path,
                        output_directory_path=output_directory_path
                    )

                if version == "v_1976_to_2016_remapped_by_20210407_schwaller_p_et_al":
                    USPTOReactionDatasetFormattingUtility.format_v_1976_to_2016_remapped_by_20210407_schwaller_p_et_al(
                        input_directory_path=input_directory_path,
                        output_directory_path=output_directory_path
                    )

                if version in [
                    "v_1976_to_2016_remapped_by_20240313_chen_s_et_al",
                    "v_50k_remapped_by_20240313_chen_s_et_al",
                    "v_mech_31k_by_20240810_chen_s_et_al",
                ]:
                    USPTOReactionDatasetFormattingUtility.format_v_chen_s_et_al(
                        version=version,
                        input_directory_path=input_directory_path,
                        output_directory_path=output_directory_path
                    )

                if self.logger is not None:
                    self.logger.info(
                        msg="The formatting of the data from the {data_source:s} has been completed.".format(
                            data_source="USPTO chemical reaction dataset ({version:s})".format(
                                version=version
                            )
                        )
                    )

            else:
                raise ValueError(
                    "The formatting of the data from the {data_source:s} is not supported.".format(
                        data_source="USPTO chemical reaction dataset ({version:s})".format(
                            version=version
                        )
                    )
                )

        except Exception as exception_handle:
            if self.logger is not None:
                self.logger.error(
                    msg=exception_handle
                )

            raise
