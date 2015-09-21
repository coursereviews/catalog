#!/usr/bin/env python

from catalog.scraper import Scraper

def test_catalog():
    scraper = Scraper('201590')

    scraper.xml_from_file('test/test.xml')
    catalog = scraper.create_catalog()

    for course in catalog:
        print course.location

if __name__ == '__main__':
    test_catalog()