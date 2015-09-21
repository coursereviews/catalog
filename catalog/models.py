# -*- coding: utf-8 -*-

from catalog.exceptions import CatalogException

class Catalog(object):
    def __init__(self, raw=None, link=None, courses=None):
        self.raw = raw
        self.link = link

        self.courses = courses or []

    def __len__(self):
        return len(self.courses)

    def __iter__(self):
        return iter(self.courses)

    @property
    def type_ids(self):
        return map(lambda i: i.id, self.types)

class Term(object):
    def __init__(self, raw_id=None, code=None):

        self.link = link
        self.rawid = raw_id
        self.courses = []

    @property
    def season(self):
        return {'90': 'fall',
                '10': 'winter',
                '20': 'spring'}.get(self.rawid[4:], 'unknown')

    @property
    def year(self):
        return self.rawid[:4]

    def __repr__(self):
        return '<Term: %s %s>' % (self.season, self.year)

class Course(object):
    def __init__(self, link=None, code=None, description=None, title=None,
                 alternate=None, _type=None,
                 department=None, requirements=None, instructors=None,
                 location=None, schedule=None, crn=None):

        # The Middlebury catalog link
        self.link = link

        # The course title code (eg. AMST0102A-F15)
        self.code = code

        # The full course description, stripped of html tags
        self.description = description

        # The full title of the course (eg. Politics, Media, Pop. Culture)
        self.title = title

        # An alternate catalog id this course is listed under
        self.alternate = alternate

        # The course type (eg. Lecture)
        self.type = _type

        self.department = department
        self.requirements = requirements or []
        self.instructors = instructors or []
        self.location = location
        self.schedule = schedule
        self.crn = crn

    def __repr__(self):
        return '<Course: %s>' % (self.crn)

class Schedule(object):
    def __init__(self, text=None, meetings=None):
        self.text = text
        self.meetings = meetings or []

    def __repr__(self):
        return '<Schedule: %s>' % '; '.join([meeting.__repr__ for meeting in self.meetings])

class Meeting(object):
    def __init__(self, raw, start_time=None, end_time=None,
                 start_date=None, end_date=None,
                 days=None, location=None):
        self.raw = raw
        self.start_time = start_time
        self.end_time = end_time
        self.start_date = start_date
        self.end_date = end_date
        self.days = days
        self.location = location

    def __repr__(self):
        return '<Meeting: %s>' % self.raw

class CourseInfo(object):
    def __init__(self, raw_id=None, href=None, text=None):
        self.raw_id = raw_id
        self.href = href
        self.text = text

    @property
    def id(self):
        return self.raw_id.split('/')[-1]

    def __repr__(self):
        return '<%s: %s>' % (self.__class__.__name__, self.id)

class Type(CourseInfo):
    pass

class Subject(CourseInfo):
    pass

class Department(CourseInfo):
    pass

class Level(CourseInfo):
    """
    The course level and corresponding code.

    Ex: UG, Undergraduate
    """
    pass

class Requirement(CourseInfo):
    pass

class CRN(CourseInfo):
    pass

class Location(CourseInfo):
    @property
    def room(self):
        if '/' in self.raw_id:
            return self.raw_id.split('/')[-1]
        else:
            raise CatalogException('Location %s has no room.' % self.id)

    @property
    def building(self):
        if '/' in self.raw_id:
            return self.raw_id.split('/')[-2]
        else:
            raise CatalogException('Location %s has no building.' % self.id)

    @property
    def id(self):
        try:
            return '/'.join([self.building, self.room])
        except IndexError:
            return CourseInfo.id.fget(self)

class Instructor(CourseInfo):
    pass
