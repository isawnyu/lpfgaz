#
# This file is part of lpf2pleiades
# by Tom Elliott for the Institute for the Study of the Ancient World
# (c) Copyright 2024 by New York University
# Licensed under the AGPL-3.0; see LICENSE.txt file.
#

"""
Define Class for a Linked Places Format Name
"""

from language_tags import tags
from lpfgaz.strings import clean_string


class LPFName:
    """
    Manage a Linked Places Format Name
    """

    def __init__(self, data: dict):
        """
        Initialize LPF Name
        """
        self._data = data  # original LPF Name data
        self._citations = None  # list of derived LPFCitation objects
        self._lang = None  # str: clean and validated language code
        self._toponym = None  # str: clean and validated toponym
        self._when = None  # a derived LPFWhen object

    @property
    def citations(self) -> list:
        """
        Get the citations of the LPF Name
        """
        raise NotImplementedError()

    @property
    def lang(self) -> str:
        """
        Get the language of the LPF Name
        """
        if self._lang is None:
            self._clean_lang()
        return self._lang

    @property
    def toponym(self) -> str:
        """
        Get the toponym of the LPF Name
        """
        if self._toponym is None:
            self._toponym = clean_string(self._data["toponym"])
        return self._toponym

    @property
    def when(self):
        """
        Get the when of the LPF Name
        """
        raise NotImplementedError()

    def _clean_lang(self):
        """
        Clean and validate a language code
        """
        clean = clean_string(self._data["lang"])
        if not tags.check(clean):
            for err in tags.tag(clean).errors:
                try:
                    clean = getattr(self, f"_clean_lang_{err}")(clean)
                except AttributeError:
                    raise NotImplementedError(
                        f"LPFName._clean_lang_{err} for '{clean}'"
                    )
        self._lang = clean
