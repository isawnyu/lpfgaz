#
# This file is part of lpfgaz
# by Tom Elliott for the Institute for the Study of the Ancient World
# (c) Copyright 2024 by New York University
# Licensed under the AGPL-3.0; see LICENSE.txt file.
#

"""
Test the lpfgaz.lpf module
"""
import pytest
from pathlib import Path
from lpfgaz.lpf import LPFFeature, LPFFeatureCollection

test_data_path = Path("tests/data")
example_lpf_file = test_data_path / "example_lpf.jsonld"


@pytest.fixture
def example_feature_data():
    return {
        "@id": "http://nowhere.org/places/example",
        "type": "Feature",
        "properties": {"title": "Example Feature", "ccodes": ["GB"], "fclasses": ["P"]},
    }


class TestLPFFeature:

    def test_initialization(self, example_feature_data):
        # Test the initialization of LPFFeature
        feature = LPFFeature(example_feature_data)
        assert isinstance(feature, LPFFeature)
        assert feature._data == example_feature_data
        assert feature.id == example_feature_data["@id"]
        assert feature.title == example_feature_data["properties"]["title"]
        assert feature.ccodes == example_feature_data["properties"]["ccodes"]
        assert feature.country_codes == example_feature_data["properties"]["ccodes"]
        assert feature.fclasses == example_feature_data["properties"]["fclasses"]
        assert feature.feature_classes == example_feature_data["properties"]["fclasses"]

    def test_countries_geonames(self, example_feature_data):
        # Test the countries_geonames property
        feature = LPFFeature(example_feature_data)
        assert feature.countries_geonames == [
            {"geonames_id": 2635167, "name": "United Kingdom"}
        ]


class TestLPFFeatureCollection:

    def test_initialization(self):
        # Test the initialization of LPFFeatureCollection
        lpf_fc = LPFFeatureCollection()
        assert isinstance(lpf_fc, LPFFeatureCollection)

    def test_read(self):
        # Test reading an LPF file
        lpf_fc = LPFFeatureCollection()
        lpf_fc.read(example_lpf_file)
        assert hasattr(lpf_fc, "lpf")
        assert (
            lpf_fc.lpf["@context"]
            == "https://raw.githubusercontent.com/LinkedPasts/linked-places/master/linkedplaces-context-v1.1.jsonld"
        )
        assert lpf_fc.lpf["type"] == "FeatureCollection"
        assert isinstance(lpf_fc.lpf["features"], list)
        assert len(lpf_fc.lpf["features"]) == 1
        assert lpf_fc.lpf["features"][0]["@id"] == "http://mygaz.org/places/p_12345"
