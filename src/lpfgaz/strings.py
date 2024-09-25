#
# This file is part of lpf2pleiades
# by Tom Elliott for the Institute for the Study of the Ancient World
# (c) Copyright 2024 by New York University
# Licensed under the AGPL-3.0; see LICENSE.txt file.
#

"""
Manipulate strings
"""

from textnorm import *


def clean_string(s: str) -> str:
    """
    Clean a string
    """
    return normalize_space(normalize_unicode(s))
