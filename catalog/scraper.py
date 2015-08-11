# -*- coding: utf-8 -*-

import requests
import xmltodict

import json

class Scraper(object):
    base_url = 'http://catalog.middlebury.edu/offerings/searchxml/catalog/catalog%2FMCUG?'

    def __init__(self, term):
        self.term = term
        self.url = Scraper.url_base + '&'.join([key + '=' + value
            for key, value in self.url_parts])

        self.xml = None

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

    def create_catalog(self):
        response = requests.get(self.url)
        self.xml = xmltodict.parse(response.content)
