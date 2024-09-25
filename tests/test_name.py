#
# This file is part of lpfgaz
# by Tom Elliott for the Institute for the Study of the Ancient World
# (c) Copyright 2024 by New York University
# Licensed under the AGPL-3.0; see LICENSE.txt file.
#

"""
Test the lpfgaz.lpf_name module
"""
from lpfgaz.lpf_name import LPFName
import pytest


@pytest.fixture
def example_feature_data():
    return {
        "@id": "http://nowhere.org/places/example",
        "type": "Feature",
        "names": [
            {
                "toponym": "Abingdon",
                "lang": "en",
                "citations": [
                    {
                        "label": "Ye Olde Gazetteer (1635)",
                        "year": 1635,
                        "@id": "http://archive.org/details/yeoldegazetteer",
                    }
                ],
                "when": {"timespans": [{"start": {"in": "1600"}}]},
            },
            {
                "toponym": " Abingdon-on-Thames",  # leading space
                "lang": "en ",  # trailing space
                "when": {
                    "timespans": [{"start": {"in": "1600"}}],
                    "certainty": "certain",
                },
            },
        ],
    }


class TestLPFName:

    def test_initialization(self, example_feature_data):
        # Test the initialization of LPFName
        name = LPFName(example_feature_data["names"][0])
        assert isinstance(name, LPFName)
        assert name._data == example_feature_data["names"][0]
        assert name.toponym == "Abingdon"
        assert name.lang == "en"

        name = LPFName(example_feature_data["names"][1])
        assert isinstance(name, LPFName)
        assert name._data == example_feature_data["names"][1]
        assert name.toponym == "Abingdon-on-Thames"  # no leading space
        assert name.lang == "en"  # no trailing space
