#
# This file is part of lpf2pleiades
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
