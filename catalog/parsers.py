from __future__ import unicode_literals
from six import string_types
import re
from datetime import datetime
from catalog.models import (Catalog,
                            Course,
                            Type,
                            Subject,
                            Department,
                            Level,
                            Requirement,
                            Location,
                            Instructor,
                            Schedule,
                            Meeting,
                            CRN,
                            Term)

def parse_catalog(catalog_dict):
    catalog = Catalog()

    catalog.raw = catalog_dict
    catalog.href = catalog_dict['rss']['channel']['link']
    catalog.term = parse_course_info(catalog_dict['rss']['channel']['catalog:chosen_term'], Term)

    for course in catalog_dict['rss']['channel']['item']:
        catalog.courses.append(parse_course(course))

    return catalog

def parse_course(course_dict):
    course = Course()

    course.code = course_dict.get('title')
    course.link = course_dict.get('link')
    course.description = course_dict.get('description')
    course.title = course_dict.get('catalog:title')

    course.type = parse_course_info(course_dict.get('catalog:genustype'), Type)
    course.location = parse_course_info(course_dict.get('catalog:location'), Location)
    course.term = parse_course_info(course_dict.get('catalog:term'), Term)
    course.schedule = parse_schedule(course_dict.get('catalog:schedule'))
    course.crn = parse_crn(course_dict.get('catalog:property'))

    # 'catalog:instructor' is a list if there are multiple instructors
    # and a dict if there is only one instructor
    instructors_list_or_dict = course_dict.get('catalog:instructor')
    if type(instructors_list_or_dict) is list:
        for instructor_dict in instructors_list_or_dict:
            course.instructors.append(parse_course_info(instructor_dict, Instructor))
    else:
        course.instructors.append(parse_course_info(instructors_list_or_dict, Instructor))

    for topic in course_dict.get('catalog:topic'):
        topic_type = topic.get('@type').split('/')[-1]

        if topic_type == 'subject':
            course.subject = parse_course_info(topic, Subject)

        elif topic_type == 'department':
            course.department = parse_course_info(topic, Department)

        elif topic_type == 'requirement':
            course.requirements.append(parse_course_info(topic, Requirement))

        elif topic_type == 'level':
            course.level = parse_course_info(topic, Level)

    return course

def parse_course_info(topic_dict, klass):
    if isinstance(topic_dict, string_types):
        return klass(raw_id=topic_dict)

    if topic_dict == None:
        return topic_dict

    topic = klass()
    topic.raw_id = topic_dict.get('@id')
    topic.href = topic_dict.get('@href')
    topic.text = topic_dict.get('#text')

    return topic

def parse_crn(crn_dict):
    return CRN(raw_id=crn_dict.get('catalog:value'))

def parse_schedule(schedule_string):
    regex = re.compile(r'(.+)-(.+) on (.+?) (at (.+) (.+) )?\((.+) to (.+)\)')
    time_format = '%I:%M%p'
    date_format = '%b %d, %Y'
    schedule = Schedule(text=schedule_string)

    for meeting_string in schedule_string.split('\n'):
        meeting = Meeting(meeting_string)

        meeting_match = re.match(regex, meeting_string)
        if not meeting_match:
            schedule.meetings.append(meeting)
            continue

        meeting_groups = meeting_match.groups()
        meeting.start_time = datetime.strptime(meeting_groups[0], time_format).time()
        meeting.end_time = datetime.strptime(meeting_groups[1], time_format).time()
        meeting.days = meeting_groups[2].split(', ')

        if meeting_groups[3]:
            meeting.location = Location(raw_id='/'.join((meeting_groups[4], meeting_groups[5])))

        meeting.start_date = datetime.strptime(meeting_groups[6], date_format).date()
        meeting.end_date = datetime.strptime(meeting_groups[7], date_format).date()

        schedule.meetings.append(meeting)

    return schedule
