# -*- coding: utf-8 -*-

class Term(object):
    def __init__(self, link=None, raw=None):

        self.link = link
        self.raw = raw
        self.courses = []

    @property
    def season(self):
        return {'90': 'fall',
                '10': 'winter',
                '20': 'spring'}.get(self.raw[4:], 'unknown')

    @property
    def year(self):
        return self.raw[:4]

class Course(object):
    def __init__(self, link=None, code=None, description=None, title=None,
                 alternate=None, _type=None, start_date=None, end_date=None,
                 department=None, requirements=None, instructor=None,
                 location=None, schedule=None, crn=None):

        self.link = link
        self.code = code
        self.description = description
        self.title = title
        self.alternate = alternate
        self.type = _type
        self.start_date = start_date
        self.end_date = end_date
        self.department = department
        self.requirements = requirements
        self.instructor = instructor
        self.location = location
        self.schedule = schedule
        self.crn = crn

class CourseInfo(object):
    def __init__(self, _id=None, href=None, description=None):
        self._id = _id
        self.href = href
        self.name = name

class Type(CourseInfo):
    pass

class Subject(CourseInfo):
    pass

class Department(CourseInfo):
    pass

class Level(CourseInfo):
    pass

class Requirement(CourseInfo):
    pass

class Subject(CourseInfo):
    pass
