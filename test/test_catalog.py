#!/usr/bin/env python

import unittest
from catalog.scraper import Scraper

class CatalogTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        scraper = Scraper('201590')
        scraper.xml_from_file('test/test.xml')
        cls.catalog = scraper.create_catalog()

class TestSimpleCatalogCourse(CatalogTestCase):
    def setUp(self):
        self.course = TestSimpleCatalogCourse.catalog.courses[0]

    def test_title(self):
        self.assertEqual(self.course.title, u'Politics, Media, Pop. Culture')

    def test_link(self):
        self.assertEqual(self.course.link, u'http://catalog.middlebury.edu/offerings/view/catalog/catalog%2FMCUG/offering/section%2F201590%2F92348')

    def test_code(self):
        self.assertEqual(self.course.code, u'AMST0102A-F15')

    def test_description(self):
        self.assertEqual(self.course.description, u'<strong>Politics, Media, Popular Culture</strong><br />\nIn this course, we will examine U.S. politics and popular culture in the period 1941-2015. We will analyze political films ranging from the World War II propaganda series, <em>Why We Fight</em>, to more recent feature films such as <em>Wag the Dog</em> and <em>Good Night and Good Luck</em>.  We will consider television\u2019s impact on civic culture, focusing on entertainment programs (<em>I Led 3 Lives</em>, <em>24</em>, <em>Scandal</em>), the news (<em>See It Now</em>, <em>The O\u2019Reilly Factor</em>), campaign commercials, and political satire (<em>The Daily Show</em>, <em>The Colbert Report</em>). Finally, we will assess how online organizing and the blogosphere impact civic participation. 3 hrs. lect.')

    def test_type(self):
        self.assertEqual(self.course.type.id, u'LCT')
        self.assertEqual(self.course.type.text, u'Lecture')

    def test_term(self):
        self.assertEqual(self.course.term.id, u'201590')
        self.assertEqual(self.course.term.text, u'Fall 2015')
        self.assertEqual(self.course.term.href, u'http://catalog.middlebury.edu/terms/view/catalog/catalog%2FMCUG/term/term%2F201590')
        self.assertEqual(self.course.term.season, 'fall')
        self.assertEqual(self.course.term.year, '2015')

    def test_department(self):
        self.assertEqual(self.course.department.id, u'AMST')
        self.assertEqual(self.course.department.text, u'Program in American Studies')
        self.assertEqual(self.course.department.href, u'http://catalog.middlebury.edu/topics/view/catalog/catalog%2FMCUG/term/term%2F201590/topic/topic%2Fdepartment%2FAMST')

    def test_requirements(self):
        self.assertEqual(len(self.course.requirements), 2)

        his_requirement = self.course.requirements[0]
        self.assertEqual(his_requirement.id, u'HIS')
        self.assertEqual(his_requirement.text, u'HIS')
        self.assertEqual(his_requirement.href, u'http://catalog.middlebury.edu/topics/view/catalog/catalog%2FMCUG/term/term%2F201590/topic/topic%2Frequirement%2FHIS')

        nor_requirement = self.course.requirements[1]
        self.assertEqual(nor_requirement.id, u'NOR')
        self.assertEqual(nor_requirement.text, u'NOR')
        self.assertEqual(nor_requirement.href, u'http://catalog.middlebury.edu/topics/view/catalog/catalog%2FMCUG/term/term%2F201590/topic/topic%2Frequirement%2FNOR')

    def test_level(self):
        self.assertEqual(self.course.level.id, u'UG')
        self.assertEqual(self.course.level.text, u'Undergraduate')
        self.assertEqual(self.course.level.href, u'http://catalog.middlebury.edu/topics/view/catalog/catalog%2FMCUG/term/term%2F201590/topic/topic%2Flevel%2FUG')

    def test_instructor(self):
        self.assertEqual(len(self.course.instructors), 1)
        instructor = self.course.instructors[0]

        self.assertEqual(instructor.id, u'eb22314a852970f29d9c828dec3265d2')
        self.assertEqual(instructor.text, u'Holly Allen')
        self.assertEqual(instructor.href, u'http://catalog.middlebury.edu/resources/view/catalog/catalog%2FMCUG/resource/resource%2Fperson%2Feb22314a852970f29d9c828dec3265d2')
        self.assertEqual(instructor.name, u'Holly Allen')

if __name__ == '__main__':
    unittest.main()