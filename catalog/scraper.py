# -*- coding: utf-8 -*-

import requests
import xmltodict

import json
from HTMLParser import HTMLParser

from catalog.parsers import parse_catalog

class Scraper(object):
    base_url = 'http://catalog.middlebury.edu/offerings/searchxml/catalog/catalog%2FMCUG?'

    def __init__(self, term):
        self.term = term
        self.url = Scraper.base_url + '&'.join([key + '=' + value
            for key, value in self.url_parts])

        self.xml = None
        self.catalog = None

    @property
    def url_parts(self):
        return [('term', 'term%2F' + self.term), ('department', ''),
                ('keywords', ''), ('time_start', '0'), ('end_time', '86400'),
                ('type%5B%5D', 'genera%3Aoffering%2FLCT'),
                ('type%5B%5D', 'genera%3Aoffering%2FLAB'),
                ('type%5B%5D', 'genera%3Aoffering%2FDSC'),
                ('type%5B%5D', 'genera%3Aoffering%2FDR1'),
                ('type%5B%5D', 'genera%3Aoffering%2FDR2'),
                ('type%5B%5D', 'genera%3Aoffering%2FPE'),
                ('type%5B%5D', 'genera%3Aoffering%2FPLB'),
                ('type%5B%5D', 'genera%3Aoffering%2FSCR'),
                ('type%5B%5D', 'genera%3Aoffering%2FSEM'),
                ('location%5B%5D', 'resource%2Fplace%2Fcampus%2FM'),
                ('search', 'Search')]

    def xml_from_url(self):
        response = requests.get(self.url)
        self.xml = xmltodict.parse(response.content)

    def xml_from_file(self, xml_file):
        with open(xml_file, "r") as f:
            self.xml = xmltodict.parse(f.read())

    def create_catalog(self):
        self.catalog = parse_catalog(self.xml)

        return self.catalog

    @staticmethod
    def strip_tags(html):
        return re.sub('<[^<]+?>', '', html)
