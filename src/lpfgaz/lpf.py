#
# This file is part of lpfgaz
# by Tom Elliott for the Institute for the Study of the Ancient World
# (c) Copyright 2024 by New York University
# Licensed under the AGPL-3.0; see LICENSE.txt file.
#

"""
Read LPF files
"""
import json
import logging
from pathlib import Path

logger = logging.getLogger(__name__)


class LPFFeature:
    """
    Manage a Linked Places Format Feature
    """

    def __init__(self, data: dict):
        """
        Initialize LPF Feature
        """
        self._data = data  # original Linked Places Format data

    @property
    def ccodes(self) -> list:
        """
        Get the country codes of the LPF Feature
        """
        return self._data["properties"]["ccodes"]

    @property
    def country_codes(self) -> list:
        """
        Get the country codes of the LPF Feature
        """
        return self.ccodes

    @property
    def fclasses(self) -> list:
        """
        Get the feature classes of the LPF Feature
        """
        return self._data["properties"]["fclasses"]

    @property
    def feature_classes(self) -> list:
        """
        Get the feature classes of the LPF Feature
        """
        return self.fclasses

    @property
    def id(self) -> str:
        """
        Get the ID of the LPF Feature
        """
        return self._data["@id"]

    @property
    def title(self) -> str:
        """
        Get the title of the LPF Feature
        """
        return self._data["properties"]["title"]


class LPFFeatureCollection:
    """
    Manage a Linked Places Format Feature Collection
    """

    def __init__(self):
        """
        Initialize LPF Feature Collection
        """
        pass

    def read(self, lpf_file_path: Path):
        """
        Read LPF file
        """
        with open(lpf_file_path, "r", encoding="utf-8") as f:
            self.lpf = json.load(f)
        del f

    def write(self, lpf_file_path: Path):
        """
        Write LPF file
        """
        raise NotImplementedError(lpf_file_path)
