import json
import pytest
from pathlib import Path
from lpf2pleiades.lpf import LPFFeatureCollection

test_data_path = Path("tests/data")
example_lpf_file = test_data_path / "example_lpf.jsonld"


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
