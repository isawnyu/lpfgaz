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
from os import environ
from pathlib import Path
from pprint import pformat
from requests import RequestException
from requests.models import PreparedRequest
from webiquette.webi import Webi

logger = logging.getLogger(__name__)
DEFAULT_HEADERS = {"User-Agent": "lpfgaz/0.1.0 (+https://github.com/isawnyu/lpfgaz)"}
FEATURE_CLASSES = {  # LFP Feature Classes
    "A": "Administrative entities (e.g. countries, provinces, municipalities)",
    "H": "Water bodies (e.g. rivers, lakes, bays, seas)",
    "L": "Regions, landscape areas (cultural, geographic, historical)",
    "P": "Populated places (e.g. cities, towns, hamlets)",
    "R": "Roads, routes, rail",
    "S": "Sites (e.g. archaeological sites, buildings, complexes)",
    "T": "Terrestrial landforms (e.g. mountains, valleys, capes)",
}


class LPFFeature:
    """
    Manage a Linked Places Format Feature
    """

    def __init__(self, data: dict, web_headers: dict = DEFAULT_HEADERS):
        """
        Initialize LPF Feature
        """
        self._data = data  # original Linked Places Format data
        self._geonames_country_info = None
        self._web_headers = web_headers
        self._web_interfaces = dict()

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
    def countries_geonames(self) -> dict:
        """
        Get the Geonames country info of the LPF Feature
        """
        return {ccode: self._get_country_geonames(ccode) for ccode in self.ccodes}

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
    def fclasses_info(self) -> dict:
        """
        Get the feature class info of the LPF Feature
        """
        return {fclass: FEATURE_CLASSES[fclass] for fclass in self.fclasses}

    @property
    def id(self) -> str:
        """
        Get the ID of the LPF Feature
        """
        return self._data["@id"]

    def is_valid_ccode(self, ccode: str) -> bool:
        """
        Check if a country code is valid
        """
        info = self._get_country_geonames(ccode)
        if info is None:
            return False
        return True

    @property
    def title(self) -> str:
        """
        Get the title of the LPF Feature
        """
        return self._data["properties"]["title"]

    def _fetch_country_geonames(self, ccode: str) -> dict:
        """
        Retrieve the Geonames country info for a given country code
        """
        url = "http://api.geonames.org/countryInfoJSON"
        try:
            w = self._web_interfaces["geonames"]
        except KeyError:
            w = Webi(
                netloc="api.geonames.org",
                headers=self._web_headers,
                respect_robots_txt=False,
            )
            # geonames disallows everyone everthing in robots.txt, so we have to ignore it
            self._web_interfaces["geonames"] = w
        params = {"country": ccode, "username": environ.get("GEONAMES_USER", "demo")}
        req = PreparedRequest()
        req.prepare_url(url, params)
        try:
            response = w.get(req.url)
            response.raise_for_status()
        except RequestException as e:
            logger.error(f"Error fetching Geonames country info for {ccode}: {e}")
            return None
        return response.json()["geonames"]

    def _get_country_geonames(self, ccode: str) -> dict:
        """
        Return the Geonames country info for a given country code
        """
        if self._geonames_country_info is None:
            self._geonames_country_info = {}
        try:
            info = self._geonames_country_info[ccode]
        except KeyError:
            info_list = self._fetch_country_geonames(ccode)
            if len(info_list) == 0:
                return None
            elif len(info_list) == 1:
                info = info_list[0]
                self._geonames_country_info[ccode] = info
            else:
                raise RuntimeError(
                    f"Multiple country info records found for {ccode}: {pformat(info_list, indent=4)}"
                )
        return info


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
