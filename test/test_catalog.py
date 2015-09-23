#!/usr/bin/env python

from __future__ import unicode_literals
import unittest
from datetime import date, time
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
        self.assertEqual(self.course.title, 'Politics, Media, Pop. Culture')

    def test_link(self):
        self.assertEqual(self.course.link, 'http://catalog.middlebury.edu/offerings/view/catalog/catalog%2FMCUG/offering/section%2F201590%2F92348')

    def test_code(self):
        self.assertEqual(self.course.code, 'AMST0102A-F15')

    def test_description(self):
        self.assertEqual(self.course.description, '<strong>Politics, Media, Popular Culture</strong><br />\nIn this course, we will examine U.S. politics and popular culture in the period 1941-2015. We will analyze political films ranging from the World War II propaganda series, <em>Why We Fight</em>, to more recent feature films such as <em>Wag the Dog</em> and <em>Good Night and Good Luck</em>.  We will consider television\u2019s impact on civic culture, focusing on entertainment programs (<em>I Led 3 Lives</em>, <em>24</em>, <em>Scandal</em>), the news (<em>See It Now</em>, <em>The O\u2019Reilly Factor</em>), campaign commercials, and political satire (<em>The Daily Show</em>, <em>The Colbert Report</em>). Finally, we will assess how online organizing and the blogosphere impact civic participation. 3 hrs. lect.')

    def test_type(self):
        self.assertEqual(self.course.type.id, 'LCT')
        self.assertEqual(self.course.type.text, 'Lecture')

    def test_term(self):
        self.assertEqual(self.course.term.id, '201590')
        self.assertEqual(self.course.term.text, 'Fall 2015')
        self.assertEqual(self.course.term.href, 'http://catalog.middlebury.edu/terms/view/catalog/catalog%2FMCUG/term/term%2F201590')
        self.assertEqual(self.course.term.season, 'fall')
        self.assertEqual(self.course.term.year, '2015')

    def test_department(self):
        self.assertEqual(self.course.department.id, 'AMST')
        self.assertEqual(self.course.department.text, 'Program in American Studies')
        self.assertEqual(self.course.department.href, 'http://catalog.middlebury.edu/topics/view/catalog/catalog%2FMCUG/term/term%2F201590/topic/topic%2Fdepartment%2FAMST')

    def test_requirements(self):
        self.assertEqual(len(self.course.requirements), 2)

        his_requirement = self.course.requirements[0]
        self.assertEqual(his_requirement.id, 'HIS')
        self.assertEqual(his_requirement.text, 'HIS')
        self.assertEqual(his_requirement.href, 'http://catalog.middlebury.edu/topics/view/catalog/catalog%2FMCUG/term/term%2F201590/topic/topic%2Frequirement%2FHIS')

        nor_requirement = self.course.requirements[1]
        self.assertEqual(nor_requirement.id, 'NOR')
        self.assertEqual(nor_requirement.text, 'NOR')
        self.assertEqual(nor_requirement.href, 'http://catalog.middlebury.edu/topics/view/catalog/catalog%2FMCUG/term/term%2F201590/topic/topic%2Frequirement%2FNOR')

    def test_level(self):
        self.assertEqual(self.course.level.id, 'UG')
        self.assertEqual(self.course.level.text, 'Undergraduate')
        self.assertEqual(self.course.level.href, 'http://catalog.middlebury.edu/topics/view/catalog/catalog%2FMCUG/term/term%2F201590/topic/topic%2Flevel%2FUG')

    def test_instructor(self):
        self.assertEqual(len(self.course.instructors), 1)
        instructor = self.course.instructors[0]

        self.assertEqual(instructor.id, 'eb22314a852970f29d9c828dec3265d2')
        self.assertEqual(instructor.text, 'Holly Allen')
        self.assertEqual(instructor.href, 'http://catalog.middlebury.edu/resources/view/catalog/catalog%2FMCUG/resource/resource%2Fperson%2Feb22314a852970f29d9c828dec3265d2')
        self.assertEqual(instructor.name, 'Holly Allen')

    def test_location(self):
        self.assertEqual(self.course.location.id, 'AXN/229')
        self.assertEqual(self.course.location.text, 'Axinn Center 229')
        self.assertEqual(self.course.location.href, 'http://catalog.middlebury.edu/resources/view/catalog/catalog%2FMCUG/resource/resource%2Fplace%2Froom%2FAXN%2F229')
        self.assertEqual(self.course.location.building, 'AXN')
        self.assertEqual(self.course.location.room, '229')

    def test_schedule(self):
        self.assertEqual(self.course.schedule.text, '12:15pm-1:30pm on Monday, Wednesday (Sep 16, 2015 to Dec 11, 2015)')
        self.assertEqual(len(self.course.schedule.meetings), 1)

        meeting = self.course.schedule.meetings[0]
        self.assertEqual(meeting.start_time, time(12, 15))
        self.assertEqual(meeting.end_time, time(13, 30))
        self.assertEqual(len(meeting.days), 2)
        self.assertEqual(meeting.days[0], 'Monday')
        self.assertEqual(meeting.days[1], 'Wednesday')
        self.assertEqual(meeting.start_date, date(2015, 9, 16))
        self.assertEqual(meeting.end_date, date(2015, 12, 11))

    def test_crn(self):
        self.assertEqual(self.course.crn.id, '92348')

if __name__ == '__main__':
    unittest.main()