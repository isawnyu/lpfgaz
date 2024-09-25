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
from requests import RequestException
from requests.models import PreparedRequest
from webiquette.webi import Webi

logger = logging.getLogger(__name__)
DEFAULT_HEADERS = {"User-Agent": "lpfgaz/0.1.0 (+https://github.com/isawnyu/lpfgaz)"}


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
        return [self._get_country_geonames(ccode) for ccode in self.ccodes]

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

    def _fetch_country_geonames(self, ccode: str) -> dict:
        """
        Retrieve the Geonames country info for a given country code
        """
        url = "http://api.geonames.org/countryInfoJSON"
        try:
            w = self._web_interfaces["geonames"]
        except KeyError:
            w = Webi(netloc="api.geonames.org", headers=self._web_headers)
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
        return response.json()

    def _get_country_geonames(self, ccode: str) -> dict:
        """
        Return the Geonames country info for a given country code
        """
        if self._geonames_country_info is None:
            self._geonames_country_info = {}
        try:
            info = self._geonames_country_info[ccode]
        except KeyError:
            info = self._fetch_country_geonames(ccode)
            self._geonames_country_info[ccode] = info
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
